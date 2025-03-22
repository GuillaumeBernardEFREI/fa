from FA import FA
from fun_episolon import *
from functions import set_to_str

def determinize(fa) -> FA:
    if fa.isdeterministic(): return fa  # print("The automaton is already deterministic.")

    isepsilon = False
    for n in fa.nodes:  # automatic remove of epsilon if there is epsilon
        if not isepsilon and len(fa.nodes[n][0]) != 0:
            isepsilon = True
    if isepsilon: fa = remove_epsilons(fa)
    # OR
    #import copy    # copy fa before pour éviter qu'il modif le fa original ??
    #if isepsilon: fa = remove_epsilons(FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), copy.deepcopy(fa.nodes)))
    
    aplha = len(fa.nodes[list(fa.nodes.keys())[0]])
    states = [set()]
    transitions = [[set([])]*aplha]

    for i in fa.entries:
        states[0] = states[0].union(set(i))
        for j in range(len(fa.nodes[i])):
            transitions[0][j] = transitions[0][j].union(set(fa.nodes[i][j]))
    n = 0
    while n < len(states):
        for i in transitions[n]:
            if len(i) > 0 and not (i in states):
                states.append(i)
                transitions.append([set([])]*aplha)       
                for j in i:
                    for k in range(len(fa.nodes[j])):
                        transitions[-1][k] = transitions[-1][k].union(set(fa.nodes[j][k]))

        n += 1
    nodes = {}
    for i in range(len(transitions)):
        for j in range(len(transitions[i])):
            temp = set_to_str(transitions[i][j])  # "" is for empty transition ; [""] not correct , [] correct
            if temp == "":
                transitions[i][j] = []
            else:
                transitions[i][j] = [temp]
    
    terminals = []
    for i in range(len(states)):
        nodes[set_to_str(states[i])] = transitions[i].copy()
        for j in states[i]:

            if j in fa.terminals:
                terminals.append(set_to_str(states[i]))
                break
    DFa= FA(1, len(terminals), [set_to_str(states[0])], terminals.copy(), nodes)
    DFa.type="DFA"
    return DFa
