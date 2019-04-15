# yolo train data
a demo for building yolo train data.

1.在硬盘中建立项目文件夹object，object下新建JPEGImages存放所有图像，新建labels存放标签。用类似labelimg的工具对图片进行标注，这里是labelimg的github链接（labelimg路径不可包括中文）。选择保存位置为labels后以YOLO格式标注完所有图像。标注结果备份好！！！后续文件操作出现问题还可以挽救。

2.运行脚本将所有图像的后缀名转化为.jpg。
JPG2jpg.py

import os      
  
def JPG2jpg(file_dir):
    os.chdir(file_dir)
    for root, dirs, files in os.walk('.'):
        for file in files:
            portion = os.path.splitext(file)
            name = portion[0]+".jpg"
            os.rename(file,name)
            print(name)
  
dir = './JPEGImages'

JPG2jpg(dir)

3.【运行一次】运行脚本批量重命名标签文件和对应的图像：
rename.py

import os      
  
def file_name(file_dir):     
    L=[]  
    for root, dirs, files in os.walk(file_dir):    
        for file in files:      
            L.append(os.path.splitext(file)[0])    
    return L  
path1 = "./JPEGImages"
path2 = "./labels"

dir1 = file_name(path1)  
dir2 = file_name(path2)

n=0
for i in range(len(dir2)):	
    if dir2[i] in dir1:
        oldname2 = path2+'/'+dir2[i]+'.txt'
        oldname1 = path1+'/'+dir2[i]+'.jpg'
        newname2 = path2+'/'+"fish"+str(i)+".txt"
        newname1 = path1+'/'+"fish"+str(i)+".jpg"
        os.rename(oldname2,newname2)
        os.rename(oldname1,newname1)
        n=n+1
print("the same name: %d , all done!" %n)

4.先将labels文件夹中的classes.txt移到工程目录，重命名为fish.names。运行脚本删除未标注的多余图像，并建立文件名索引train.txt。

removeimg.py

import os      
  
def file_name(file_dir):     
    L=[]  
     
    for root, dirs, files in os.walk(file_dir):    
        for file in files:      
            L.append(os.path.splitext(file)[0])    
    return L  
  
dir1 = file_name('./JPEGImages')  
dir2 = file_name('./labels')
for i in range(len(dir2)):
    dir1.remove(dir2[i])
print("no labeled data unmber are: %d" %len(dir1))
'''
if len(dir1)>0:
    print(dir1) 
    for i in range(len(dir1)):
        os.remove(os.path.join('./JPEGImages',dir1[i]+'.jpg'))
    print('delete no labeled data')
'''
train_datas = open("train.txt","w+")
for i in range(len(dir2)):

    train_datas.write(str(dir2[i])+"\n")

train_datas.close()

5.运行脚本根据生成的train.txt生成指向训练集绝对路径的索引fish_train.txt
label.py


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

制作验证集可建立fish_val.txt，并且将train.txt的一部分剪切出来。
