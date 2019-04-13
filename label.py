import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

image_ids_train = open('./train.txt').read().strip().split()  
list_file_train = open('fish_train.txt', 'w')     
for image_id in image_ids_train:
    list_file_train.write('/home/liyibing/darknet/object/JPEGImages/%s.jpg\n'%(image_id))  
list_file_train.close()