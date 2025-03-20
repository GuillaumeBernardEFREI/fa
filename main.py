from FA import FA
from functions import *

fa_folder = "automates"

f = load_fa("auto1.txt",fa_folder)
#f = complementarize(f)

#print(f.isautomaton())
#print(f.isdeterministic())
#f.iscomplete()

display(f)
