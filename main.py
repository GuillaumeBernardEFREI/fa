from fun_episolon import *
from load import load_fa
from word_recog import word_recog
from display import display

from FA import FA
from SFA import standardize
from DFA import determinize
from CDFA import completion
#from MCDFA import minimize

fa_folder = "automates"

f = load_fa("#03", fa_folder)

display(f)
"""
f = complementarize(f)
f = determinize_and_completion(f)
print(f.entries)
print(f.terminals)
print(f.nodes)
print(f.isautomaton())
display(f)
f=remove_epsilons(f)
display(f)
f.iscomplete()
f = determinize(f)
display(f)
f = standardize(f)
f = completion(f)
display(f)
f.iscomplete()
f.isdeterministic()
word_recog(f)
"""