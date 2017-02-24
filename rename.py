import os
[os.rename(f, f.replace('.png', '_tr.png')) for f in os.listdir('.')]
#rename files inside the current working directory
