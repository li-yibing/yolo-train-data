
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
print("the same name:%d ,all done." %n)
