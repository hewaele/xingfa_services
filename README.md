# 兴发模具ID检测自动识别系统
# 系统功能描述：
本系统基于MASK RCNN搭建模具ID检测模型，通过手持终端采集模具ID图片并将图片发送至后台服务器，后台对采集图片进行自动识别，并将识别结果返回到手持终端。
# 技术细节：
1.以MASK RCNN作为目标检测模型主体框架  
2.使用DARTs算法对模型的RCNN部分网络进行构建  
3.基于Django搭建后台服务器  
# 演示说明：
1.从[test_img](https://github.com/hewaele/xingfa_services/tree/master/test_img)文件夹下下载测试用图片  
2.进入web服务器：http://23e1c22801.imwork.net/  
3.将测试图片上传  
4：返回识别结果  
# 数据集下载地址
[kaggle/hewaele/Dataset_of_MoldID](https://www.kaggle.com/hewaele/xingfa-datast-test)
# 相关结果展示：
![1](https://github.com/hewaele/xingfa_services/blob/master/show/2019-04-25152727.jpg)
![2](https://github.com/hewaele/xingfa_services/blob/master/show/IMG_2050.JPG)
![3](https://github.com/hewaele/xingfa_services/blob/master/show/IMG_2384.JPG)
![4](https://github.com/hewaele/xingfa_services/blob/master/show/IMG_2674.JPG)
