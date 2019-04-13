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
