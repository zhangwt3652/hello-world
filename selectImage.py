import os
import glob
import shutil
import random

root='E:/face datasets/LS3D-WFaceNew/converted'
folderpaths=['CatABCTrainset','300W-Testset-3D','AFLW2000-3D-Reannotated','LS3D-W-balanced','Menpo-3D','dayvideo_fatigue','dayvideo_phone','dayvideo_smoke','FatigueVideo_180103','FatigueVideo_180309','phonevideo','smokevideo_test','smokevideo_0108','T3_20180831','T3_test','zhongtiananchi','root26and31','root24','yawning']
dstfolder='trainset_all'
SAMPLE_NUM=300

for i in range(1,16):
    filepath=[]
    for folderpath in folderpaths:
        folderdir=os.path.join(root,folderpath)    
        imageDir = os.path.join(folderdir, '%d' %(i))
        filelist=glob.glob(imageDir+'/*.pts')
        for j in range(len(filelist)):
            filepath.append(os.path.join(imageDir,filelist[j]))

    random.shuffle(filepath)

    num=0
    if len(filepath)>SAMPLE_NUM:
        num=SAMPLE_NUM
    else:
        num=len(filepath)

    for k in range(num):
        dstfilepath=os.path.split(filepath[k])[1]
        shutil.copy(filepath[k],os.path.join(root,dstfolder,'%d' %(i),dstfilepath))
        srcjpg=filepath[k][:-3]+'jpg'
        dstjpg=os.path.join(root,dstfolder,'%d' %(i),dstfilepath[:-3])+'jpg'
        shutil.copy(srcjpg,dstjpg)    