import os
import numpy as np
import cv2
from skimage import io, transform, img_as_ubyte
import threading

NUM_THREAD = 8

def scan_files(directory, prefix=None, postfix='.jpg'):
    files_list = []
    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(os.path.abspath(directory), special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(os.path.abspath(directory), special_file))
            else:
                files_list.append(os.path.join(os.path.abspath(directory), special_file))
    print(len(files_list))
    return files_list

def image_norm(image, image_size):
    return img_as_ubyte(transform.resize(image, image_size))

def filename_to_label(file):
    lst = ['梅','菊','竹','草','山','花','叶','柳',
    '月','阳','水','雪']
    name = os.path.basename(file).split('.')[0]
    label = np.zeros(len(lst))
    for i in range(len(lst)):
        if lst[i] in name:
            label[i] = 1
    return  label

def get_photo_data(file_list, image_size=(224, 224)):
    data, Label = [], []
    source = file_list
    lock = threading.Lock()
    # for file in file_list:
    def work(i):
        file = source.pop(0)
        try:
            img = io.imread(file)
            img = image_norm(img, image_size)
            label = filename_to_label(file)
        except:
            print('Load', file, 'fail')
            return
        lock.acquire()
        data.append(img)
        Label.append(label)
        lock.release()
    try:
        from multiprocessing.pool import ThreadPool
        multi_available = True
    except ImportError:
        print('multiprocessing not available, fall back to single threaded encoding')
        multi_available = False

    if multi_available and NUM_THREAD > 0:
        p = ThreadPool(NUM_THREAD)
        p.map(work, [i for i in range(len(source))])
    else:
        for _ in range(len(source)):
            work(_)
    data = np.array(data)
    Label = np.array(Label)
    print(data.shape, Label.shape)
    return data, Label

if __name__ == '__main__':
    X, Y = get_photo_data(scan_files(r'../GetPhotoFromBaidu/pictures'))