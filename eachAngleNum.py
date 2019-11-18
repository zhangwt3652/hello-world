import os

root='E:/face datasets/LS3D-WFaceNew/converted'
folderpaths=['CatABCTrainset','300W-Testset-3D','AFLW2000-3D-Reannotated','LS3D-W-balanced','Menpo-3D','dayvideo_fatigue','dayvideo_phone','dayvideo_smoke','FatigueVideo_180103','FatigueVideo_180309','phonevideo','smokevideo_test','smokevideo_0108','T3_20180831','T3_test','zhongtiananchi','root26and31','root24','yawning']

listf=open('num.txt', 'w')
for folderpath in folderpaths:
    folderdir=os.path.join(root,folderpath)    
    for i in range(16):
        imageDir = os.path.join(folderdir, '%d' %(i))
        filelist=os.listdir(imageDir)
        listf.write('%d %d\n' %(i,len(filelist)/2))


