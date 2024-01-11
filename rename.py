import os
os.chdir('C:/Users/OWNER/Desktop/collectingDataset/dataset')
i=1
for file in os.listdir():
    src=file
    dst="p"+"_"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1

