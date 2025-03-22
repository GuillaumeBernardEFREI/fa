from FA import FA
from functions import *
from fun_episolon import *

fa_folder = "automates"

f = load_fa("#32", fa_folder)
#f = complementarize(f)

f = determinize_and_completion(f)

print(f.entries)
print(f.terminals)
print(f.nodes)

#print(f.isautomaton())
#display(f)
#f=remove_epsilons(f)
display(f)
#f.iscomplete()
f = determinize(f)
display(f)
f = standardize(f)
f = completion(f)
display(f)
f.iscomplete()
f.isdeterministic()
#word_recog(f)