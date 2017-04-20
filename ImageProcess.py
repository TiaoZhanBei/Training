import os
from numpy import *
from scipy import misc
from PIL import Image


def scan_files(directory, prefix=None, postfix='.jpg'):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))
    return files_list


def get_photo_data(file_list, photo_size=(100, 100)):
    data = []
    for file in file_list:
        im = Image.open(file)
        thu = im.resize(photo_size)
        thu.save('temp.jpg')
        im = misc.imread('temp.jpg')
        #temp = misc.imresize(im, photo_size)
        #print(temp.size)
        data.append(im)
    return data
