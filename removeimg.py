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
#'''
if len(dir1)>0:
    print(dir1) 
    for i in range(len(dir1)):
        os.remove(os.path.join('./JPEGImages',dir1[i]+'.jpg'))
    print('delete no labeled data')
#'''
train_datas = open("train.txt","w+")
for i in range(len(dir2)):

    train_datas.write(str(dir2[i])+"\n")

train_datas.close()
