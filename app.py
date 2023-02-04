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
print(path.exists())
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

path = Path("ecommerce")
print("chechking if customer path exists: ", path.exists())


for p in path.iterdir():
    print(p)
paths = [p for p in path.iterdir()]
print("list: ", paths)

paths = [p for p in path.iterdir() if p.is_dir()]
print("list2: ", paths)

#  to get the py files using glob method

py_files = [p for p in path.glob("*.py")]
print("Using glob: ",py_files)

py_files = [p for p in path.rglob("*.py")]
print("Using r - glob: ",py_files)