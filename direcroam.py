import os
#import shutil
# imported shutil to move from the source directory to the directory i want to push
#shutil.move(r'C:\Users\DAPSON\Documents\Backend\masteratwi\walkdirectories.py',r'C:\Users\DAPSON\Documents\directorywalker\direcroam.py')

path=input('enter your path:')

for folder,subfolder,files in os.walk(path):
    print('the folders found in the path are : ' + folder)

    for subfolders in subfolder:
        print('the subfolders found in the path are : ' + subfolders)
        for filename in files :
         print('the filename is : ' + filename)
         print('')


