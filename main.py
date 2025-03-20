from FA import FA
from functions import *

fa_folder = "automates"

f = load_fa("#28",fa_folder)
#f = complementarize(f)

#print(f.isautomaton())
#print(f.isdeterministic())
#f.iscomplete()
print(f)
word_recog(f)