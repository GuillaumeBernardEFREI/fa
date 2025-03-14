from FA import FA
from functions import *

fa_folder = "automates"

f = load_fa("auto1.txt",fa_folder)
#f = complementarize(f)

f.isautomaton()
f.isdeterministic()
f.iscomplete()

print(f)
