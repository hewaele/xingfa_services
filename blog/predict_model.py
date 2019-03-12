from tensorflow.python.platform import gfile
from PIL import Image
import tensorflow as tf
import numpy as np
import os
import time
image_path = '/home/hewaele/PycharmProjects/django/xingfa_services/mysite/upload/'

lab_dic = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7',
                '8':'8', '9':'9', '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F',
                '16':'G', '17':'H', '18':'K', '19':'L', '20':'M', '21':'N', '22':'P',
               '23':'Q', '24':'R', '25':'S', '26':'T', '27':'V', '28':'W', '29':'X', '30':'Y',
               '31': 'Z'}


objection = {"file": "./test_img/img2.JPG",
             "objects": [{"bbox": [670, 1170, 812, 1439],
                          "label": 2, "prob": 0.9998},
                         {"bbox": [314, 1116, 424, 1372],
                          "label": 13, "prob": 0.9997},
                         {"bbox": [810, 1178, 967, 1458],
                          "label": 5, "prob": 0.9994},
                         {"bbox": [976, 1168, 1167, 1474],
                          "label": 2, "prob": 0.9989},
                         {"bbox": [2065, 1296, 2252, 1571],
                          "label": 6, "prob": 0.9989},
                         {"bbox": [2859, 1310, 3044, 1632],
                          "label": 22, "prob": 0.9988},
                         {"bbox": [1823, 1285, 2026, 1547],
                          "label": 4, "prob": 0.9988},
                         {"bbox": [1662, 1257, 1807, 1533],
                          "label": 1, "prob": 0.9984},
                         {"bbox": [543, 1169, 676, 1416],
                          "label": 0, "prob": 0.998},
                         {"bbox": [2740, 1333, 2864, 1615],
                          "label": 1, "prob": 0.9973},
                         {"bbox": [423, 1147, 547, 1388],
                          "label": 4, "prob": 0.981}]}

#根据定位将id排序获取实际模具id
def get_id(pos, label):
    id = []
    for index in range(len(label)):
        tmp = [pos[index][0], pos[index][2], label[index]]
        id.append(tmp)

    id = np.array(id)
    #当未检测出目标的情况，出现报错  例如图片img489
    if len(id) == 0:
        return 'none'
    else:
        print(id)

        a = id[id[:, 0].argsort()]
        b = a[:,2]

        c = [lab_dic[str(int(bi))] for bi in b]
    #判断将id翻转
    result = ''.join(c)
    # if '641' in result or result[-1].isalpha() and len(result) > 1:
    #     result = result[::-1]
    #将字符进行分割
    result = cut_id(result, a[:, 0], a[:, 1])

    return result

def cut_id(id, pos_s, pos_e):
    tmp_id = []
    #当长度大于一定长度对字符进行分割
    if len(id) > 5:
        #获取间隔距离
        dis = 0
        for index  in range(len(id)-1):
            dis += pos_s[index+1] - pos_e[index]
        agv = dis/(len(id)-1)

        for index in range(len(id)-1):
            if pos_s[index+1] - pos_e[index] >= 2*agv:
                tmp_id.append(id[index])
                tmp_id.append('-')
            else:
                tmp_id.append(id[index])
        tmp_id.append(id[-1])

        return ''.join(tmp_id)

    else:
        return id

def load_modle_to_predict():
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    sess = tf.Session()
    with gfile.FastGFile('/home/hewaele/PycharmProjects/xingfa_frcnn/pb_module/module3.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='') # 导入计算图
    print('载入完成')
    # 需要有一个初始化的过程
    sess.run(tf.global_variables_initializer())
    print('初始化完成')
    # 输入
    input_x = sess.graph.get_tensor_by_name('input:0')

    # 输出名字
    # output_node_names = ["fasterrcnn/rcnn/predict_result", 'fasterrcnn/rcnn/rcnn_proposal_1/GatherV2_64',
    #                      "fasterrcnn/rcnn/rcnn_proposal_1/GatherV2_65", "fasterrcnn/rcnn/rcnn_proposal_1/TopKV2"])

    # 输出名字分别对应总结果， id, 位置， 概率
    op = sess.graph.get_tensor_by_name("fasterrcnn/rcnn/predict_result:0")
    op2 = sess.graph.get_tensor_by_name("fasterrcnn/rcnn/rcnn_proposal_1/GatherV2_65:0")
    op3 = sess.graph.get_tensor_by_name("fasterrcnn/rcnn/rcnn_proposal_1/GatherV2_64:0")
    op4 = sess.graph.get_tensor_by_name("fasterrcnn/rcnn/rcnn_proposal_1/TopKV2:0")


    print('success0')
    p = os.listdir(image_path)
    image = Image.open(image_path+p[0])

    ret = sess.run([op2, op3], feed_dict={input_x: np.array(image)})
    id = get_id(ret[1], ret[0])

    return id

if __name__ == "__main__":
    load_modle_to_predict()