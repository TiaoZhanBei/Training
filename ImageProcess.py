import os
from numpy import *
from scipy import misc


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


def get_photo_data(file_list):
    data = []
    for file in file_list:
        im = misc.imread(file)
        #print(im.shape, im.dtype)
        #im = im.reshape((1, im.size))
        data.append(im)
    return data
