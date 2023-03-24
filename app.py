'''
Modules have same relationship with the package as directories have files residing in them.
the directory is the package, the files are the modules, methods in those files are what we
use. 

'''


from ecommerce.sales import cal_Bill, cal_tax
import sys
# print(sys.path)
cal_Bill()
cal_tax()


from pathlib import Path


print("Home Dir: ", Path.home())

path = Path("ecommerce/__init__.py")
print("is this the problem",path.exists())
print(path.is_file())
print(path.is_dir())

print("Name ",path.name)
print("Stem ",path.stem)
print("Suffix ",path.suffix)
print("Parent ",path.parent)

# path.exists() # check if there is path named like the path
# path.mkdir() # creates new directory 
# path.rmdir() # removes directory
# path.rename() # renames directory

path = Path("i_am_initiated")
print("chechking if customer path exists: ", path.exists())

print("this is directory iteration function: ")
for p in path.iterdir():
    print(p)

print("this is also directory iteration function: ")

paths = [p for p in path.iterdir()]
print("list: ", paths)

print("this is directories inside directories function: ")

paths = [p for p in path.iterdir() if p.is_dir()]
print("list2: ", paths)

#  to get the py files using glob method

py_files = [p for p in path.glob("*.txt")]
print("Using glob: ",py_files)

py_files = [p for p in path.rglob("*.py")]
print("Using r - glob: ",py_files)

# import shutil

# source = Path("i_am_initiated/Anaconda.docx")
# target = Path("i_am_initiated/dummyfolder/dummyfolder2/dummyfolder4")
# shutil.copy(path, target)