from FA import FA
from functions import *
from fun_episolon import *

fa_folder = "automates"

f = load_fa("#35",fa_folder)
#f = complementarize(f)

#print(f.isautomaton())
#display(f)
f=remove_epsilons(f)
display(f)
#f.iscomplete()
#f = determinize(f)
#display(f)
#f.isdeterministic()
#word_recog(f)