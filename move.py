#Scenario 1
import os, shutil
shutil.move("85_FLAP_desmond_setup","85")
#Scenario 2
import glob
for myfile in myfiles:
  first_part = myfile[:-19]
  dir = glob.glob('%s/' % first_part)[0]
  os.rename(myfile, os.path.join(dir, myfile))
#Scenario 3 - PS: Not finished
import os, shutil, fnmatch
files=[]
for file in os.listdir("."):
  if fnmatch.fnmatch(file, "*_FLAP_desmond_setup"):
    files.append(file)
