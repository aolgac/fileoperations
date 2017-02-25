import os, shutil, fnmatch
files=[]
for file in os.listdir("."):
  if fnmatch.fnmatch(file, "*_FLAP_desmond_setup"):
    files.append(file)
  shutil.move("85_FLAP_desmond_setup","85")
