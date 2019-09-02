# 兴发模具ID自动识别系统
# 系统功能描述：
   该铝业此前对模具的管理主要是通过在模具表面粘贴纸质二维码，通过手持设备扫描获取模具ID。但由于铝材生产环境原因造成纸质二维码极易损坏，需要人为再次粘贴二维码。本项目基于MASK RCNN搭建模具表面ID检测模型，通过手持终端拍摄模具图片然后传输到后台进行模具ID自动识别，再将识别结果返回到手持终端显示。系统解决原始铝业通过粘贴纸质二维码容易损坏的问题。关键技术在于运用DARTs技术自动搜索模型中的RCNN网络，进一步提高了模具ID检测的准确率，同时解决人为调整网络结构带来的不便性。使用DARTs算法取代原始的RCNN网络，模型在单个字符准确率上提高了1.89个百分点，字符整体准确率提高0.59个百分点。
# 技术细节：
1.以MASK RCNN作为目标检测模型主体框架  
2.使用DARTs算法对模型的RCNN部分网络进行构建  
3.基于Django搭建后台服务器  
# 演示说明：
1.从[test_img](https://github.com/hewaele/xingfa_services/tree/master/test_img)文件夹下下载测试用图片  
2.进入web服务器：http://23e1c22801.imwork.net/  
3.将测试图片上传  
4.返回识别结果  
# 数据集下载地址
[kaggle/hewaele/Dataset_of_MoldID](https://www.kaggle.com/hewaele/xingfa-datast-test)  
包含三个文件夹：train,val,test  
每个文件夹下包含训练图片及xml标记文件  
train包含5102张模具图片  
val包含1020张模具图片  
test包含943张图片  
# 相关结果展示：
![](https://github.com/hewaele/xingfa_services/blob/master/show/result.jpg)
