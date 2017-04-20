# Training

## ImageProcess.py

#### scan_files(directory, prefix=None, postfix='.jpg')
directory为要扫描的目录，prefix为前缀，postfix为后缀
返回扫描到的文件列表

#### get_photo_data(file_list, photo_size=(100, 100))
输入的file_list为文件列表，photo_size为返回图片的大小
返回的data为图片数据的集合，为一个3维矩阵的list。


例：
```
import ImageProcess as IP
import os

list = IP.scan_files(os.getcwd()+'\\pic',postfix='png')
datas = IP.get_photo_data(list)
for data in datas:
    print(data.shape)
```
