# Training

## ImageProcess.py

#### scan_files(directory, prefix=None, postfix='.jpg')
directory为要扫描的目录，prefix为前缀，postfix为后缀
返回扫描到的文件列表

#### get_photo_data(file_list)
输入的file_list为文件列表，返回的data为图片数据的集合

例：
```
import ImageProcess as IP
import os

list = IP.scan_files(os.getcwd()+'\\pic',postfix='png')
datas = IP.get_photo_data(list)
for data in datas:
    print(data.shape)
```
