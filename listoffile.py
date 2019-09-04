from os import listdir
from os.path import isfile,join
files=[f for f in listdir('C:\Users\pc\Desktop\student') if isfile(join('C:\Users\pc\Desktop\student',f))]
print(files)
