import os
import pandas as pd 
import gc 

# Configurations
dir_dataset = './Dataset'
dir_savedir = './Dataset_csv'

# Create necessary directories
if not os.path.exists(dir_savedir): os.mkdir(dir_savedir)

# Iterate over house directories (folders starting with "house_")
for houseName in os.listdir(dir_dataset):
    if houseName.startswith("house_") == False: continue
    if os.path.isdir(dir_dataset + '/' + houseName) == False: continue
    print("Processing house: " + houseName )
    for fileName in os.listdir(dir_dataset+'/'+houseName):
        fileNameWithoutExt = fileName.rsplit(".", 1)[0]
        fileExt = fileName.rsplit(".", 1)[1]
        if fileExt != 'dat': continue    
        # Create necessary directories
        if not os.path.exists(dir_savedir+'/'+houseName): os.mkdir(dir_savedir+'/'+houseName)    
        print(fileNameWithoutExt)
        dat_file = pd.read_csv(dir_dataset+'/'+houseName+'/'+fileName, sep=' ')
        dat_file.to_csv(dir_savedir+'/'+houseName+'/'+fileNameWithoutExt+'.csv', index=None)
        # clean up the memory
        del dat_file; gc.collect(); 
        del fileNameWithoutExt; gc.collect();
        del fileExt; gc.collect();