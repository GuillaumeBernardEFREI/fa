from os import path
from FA import FA
from fun_episolon import *
from math import ceil


def split_with_alphabet(_str):
    for i in range(len(_str)):
        if not (_str[i] in "{.0123456789}"):
            return [_str[:i], _str[i], str(int(_str[i+1:]))]


def set_to_str(s):
    if len(s) == 0: return ""  # "" is for empty transition ; [""] not correct , [] correct
    s = list(s)
    s.sort()
    _str = ""
    for i in range(0, len(s)-1):
        _str += s[i]+'.'
    _str += s[-1]
    if len(s) != 1:
        return "{"+_str+"}"
    return _str


def load_fa(fa_path, fa_folder) -> FA:
    f = open(path.join(fa_folder, fa_path), mode="r")
    # symbols in the alphabet
    alp = int(f.readline().replace("\n", ""))+1
    # Number of states
    n = int(f.readline().replace("\n", ""))
    
    nodes = {}
    
    # Create a dic of form {Q : [p.a.q]}
    for i in range(n):
        nodes[str(i)] = []
        for j in range(alp):
            nodes[str(i)].append([])

    # initianlize the entries (I)
    line = f.readline().replace("\n", "")
    entries_number = int(line.split(" ")[0])

    entries = []
    for i in line.split(" ")[1:]:
        entries.append(i)
        
    # Initianalize the Terminals (T)
    line = f.readline().replace("\n", "")
    terminal_number = int(line.split(" ")[0])

    terminals = []
    for i in line.split(" ")[1:]:
        terminals.append(i)
    
    # Initianalize the transitions
    f.readline().replace("\n", "")
    lines = f.readlines()
    # for each transition
    for line in lines:
        line.replace("\n", "")
        t = split_with_alphabet(line)
        # from the t[0] th node,
        # add a transition of the character t[1] (97 is the ord of 'a')(So we get a number from 0-25)
        # to the t[2] th node
        if t[1] == '!': nodes[t[0]][0].append(t[2])
        else: nodes[t[0]][ord(t[1])-96].append(t[2])
    fa = FA(entries_number, terminal_number, entries, terminals, nodes)
    
    return fa


def complementarize(fa) -> FA:
    _terminals = [str(i) for i in range(len(fa.nodes))]
    for i in fa.terminals:
        try:
            _terminals.remove(str(i))
        except:
            continue
    return FA(fa.entries_number, len(_terminals), fa.entries, _terminals, fa.nodes)


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
    return FA(1, len(terminals), [set_to_str(states[0])], terminals.copy(), nodes)


def display(fa):
    
    for i in fa.nodes:
        alpha = len(fa.nodes[i])
        break

    columnswidth=[9]
    for i in range(alpha):
        columnswidth.append(5)        
        for j in fa.nodes:
            t = str(fa.nodes[j][i])
            t = max(5, len(t)-t.count("'")-t.count(" ")-t.count("[")-t.count("]"))
            if columnswidth[-1] < t:
                columnswidth[-1] = t

    print("   |"+" "*int((columnswidth[0]-5)/2)+'State'+" "*int(ceil((columnswidth[0]-5)/2)), end="")
    for i in range(alpha):
        if i != 0:
            char = chr(96+i)
        else:
            char = 'ε'
        print("|"+" "*int((columnswidth[i+1]-1)/2)+char+" "*int(ceil((columnswidth[i+1]-1)/2)), end="")

    print("|")
    print("   "+"-"*(sum(columnswidth)+1+len(columnswidth)))

    for i in fa.nodes:
        if (i in fa.terminals) and not(i in fa.entries): print(" <-", end="")
        if not (i in fa.terminals) and (i in fa.entries): print(" ->", end="")
        if (i in fa.terminals) and (i in fa.entries): print("<->", end="")
        if not (i in fa.terminals) and not (i in fa.entries): print("   ", end="")

        print("|"+" "*int((columnswidth[0]-len(i))/2)+i+" "*int(ceil((columnswidth[0]-len(i))/2))+"|", end="")
        for j in range(len(fa.nodes[i])):

            t = str(fa.nodes[i][j])
            t = len(t)-t.count("'") -t.count(" ")-t.count("[")-t.count("]")
            t = (columnswidth[j+1]-t)/2
            
            print(" "*int(t), end="")
            for k in range(len(fa.nodes[i][j])-1):
                print(fa.nodes[i][j][k], end=",")

            if len(fa.nodes[i][j]) > 0: print(fa.nodes[i][j][-1], end="")
            
            print(" "*int(ceil(t))+"|", end="")
        print("")
        print("   "+"-"*(sum(columnswidth)+len(columnswidth)+1))        


def test_word(word: str, FA : FA) -> bool:
    """Tests a given word with a loaded FA to see if it is in the langage of the FA."""
    try :
        paths = list()  # list[(node:str,symbol_nb:int)]
        for node in FA.entries:
            paths.append([node, 0])
        while len(paths) > 0:
            cur_node, i = paths.pop(0)
            while len(word) > i:
                cur_node = FA.nodes[str(cur_node)][ord(word[i])-97]
                if len(cur_node) > 1:
                    # range 1 to len(cur_node) because we will already continue on the 0th path
                    for j in range(1, len(cur_node)):
                        # append a new path to explore At the next transition
                        paths.append([cur_node[j], i+1])
                elif len(cur_node) == 0:
                    break
                # preparing the next iteration of the loop
                cur_node = cur_node[0]
                i += 1
            if len(word) == i and cur_node in FA.terminals:
                return True
            # else you continue the loop on another path
    except Exception as e:
        # debug print
        print(f"[{e}]")
        print("You may have entered a symbol that is not a part of the alphabet.")
        return False


def read_word() -> str:
    """This is a little function that prompts the user to enter a word to be tested."""
    return input("Please enter the word to be tested.\nIf you wish to stop testing you can enter the word in between the quotes : \t'#end'\n")


def word_recog(FA:FA):
    """Main function to check if a user entered word is part of the langage of an automata."""
    print()  # separation from previous messages.
    word: str = read_word()
    while word != "#end":
        if test_word(word, FA):
            print("\nGood!\tThe word you entered is a part of the langage of this FA\n")
        else:
            print("\nOh No!\tThe word you entered is not a part of the langage of this FA\n")
        word = read_word()
    return


def standardize(fa: FA) -> FA:
    import copy
    # we first check if it's standardized (only has 1 entry and no transitions going back to it)
    if fa.isstandard():
        # print("The automaton is already standard")
        return fa
    # if not we create a new FA (to not modify the initial one)
    else:
        new_nodes = copy.deepcopy(fa.nodes)
        newInitialState = "I"
        # ça jsp si c vrmt utile mais bon au cas où ya un state qui s'appelle pareil
        if newInitialState in new_nodes:
            newInitialState += "*"
        alphabetFA = len(next(iter(new_nodes.values())))
        new_nodes[newInitialState] = [[] for _ in range(alphabetFA)]

        # copy the transitions that went from the initial entry state
        for entry in fa.entries:
            for symbol in range(alphabetFA):
                new_nodes[newInitialState][symbol].extend(new_nodes[entry][symbol])

        return FA(entries_number=1, terminal_number=fa.terminal_number, entries=[newInitialState], terminals=fa.terminals.copy(), nodes=new_nodes)


def completion(fa: FA) -> FA:  # completize ?
    """Construction of a complete deterministic automaton from a deterministic automaton FA, if it is not already complete.
    :param deterministic fa:
    :return complete deterministic fa:
    """
    import copy
    # to be complete, all states of an automaton must have all transitions possible in its alphabet.
    # check it's already complete
    if fa.iscomplete():
        # print("The automaton is already complete.")
        return fa
    # completing a non-deterministic automaton is not recommended / doesn't make sense
    if not fa.isdeterministic():
        print("The automaton was not deterministic ; the completion have been done anyway.")
    # if not complete, we create a new FA (complete) :

    new_nodes = copy.deepcopy(fa.nodes)
    sink_state = "P"
    # au cas où ya un state qui s'appelle pareil
    if sink_state in new_nodes:
        sink_state += "*"
    alphabet_fa = len(next(iter(new_nodes.values())))
    # add the P state row
    new_nodes[sink_state] = [[] for _ in range(alphabet_fa)]
    # add the P transitions to the table
    for n in new_nodes:
        for i in range(1, len(new_nodes[n])):  # start to 1 to ignore the column epsilon
            # if There are no transitions from n using char i, we add a sink/trash state
            if len(new_nodes[n][i]) == 0:
                new_nodes[n][i] = 'P'
    return FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), new_nodes)


def determinize_and_completion(fa: FA) -> FA:
    """
    Construction of a complete deterministic automaton from a non-deterministic automaton FA.
    :param fa:
    :return complete deterministic fa:
    """
    if fa.isdeterministic() and fa.iscomplete():
        return fa
    import copy
    if not fa.isdeterministic():
        fa = determinize(FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), copy.deepcopy(fa.nodes)))
    if not fa.iscomplete():
        fa = completion(FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), copy.deepcopy(fa.nodes)))
    return FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), copy.deepcopy(fa.nodes))


def minimize(fa: FA) -> FA:
    """Construct a minimized version of the CDFA passed in argument.
    If the algorithm finds out that the automaton was already minimal, the program tell the user about it.
    there is no verification if the automaton is already minimal.
    Your program must display successive partitions, as well as transitions
    expressed in terms of parts (groups), all the way along the minimization process. Make that display easily readable
    :param complete deterministic fa:
    :return minimized complete deterministic fa:
    """
    # need a CDFA without non-accessible states
    if not fa.isdeterministic():
        fa = determinize_and_completion(fa)
    elif not fa.iscomplete():
        fa = completion(fa)

    groups = dict()
    new_groups = dict()
    new_groups[0] = fa.entries
    new_groups[1] = fa.terminals
    i = 0
    while groups != new_groups:  # stop when two successive iterations give the same results
        groups = new_groups
        print(f"instance n°{i}")
        print("the groups are : ", end="")
        for k in groups.keys():
            print(str(k)+":", end="")
            for elt in groups[k]:
                print(elt+" ")
            print(end=", ")

        for group_k in groups.keys():
            """In an iterative fashion, we look if the states belonging to the same group 
should be separated: this is the case if we can detect at least one suffix 
recognized from one state and not recognized from the other. """
            if len(groups[group_k]) > 1:  # cannot split a group with less than 2 states
                targets = dict()
                for state in groups[group_k]:
                    for transition in fa.nodes[state]:
                        for k in groups.keys():
                            if transition[0] in groups[k]:
                                if targets[state]:
                                    targets[state].append(k)
                                else:
                                    targets[state] = [k]  # kinda transition table (normally)
                commons = dict()  # states that have targets in common/similar
                for compo_key in targets.keys():
                    if commons[targets[compo_key]]:
                        commons[targets[compo_key]].append(compo_key)
                    else:
                        commons[targets[compo_key]] = compo_key  # compy_key=state
                # if only 1 group of states that all have the same targets, don't need to split the group ; else :
                if len(commons) > 1:
                    new_groups[group_k] = list(commons.values())[0]
                    for g in list(commons.values())[1:]:
                        new_groups[len(groups)] = g
            else:
                new_groups[group_k] = groups[group_k]
        print("display transition ...")
        i += 1
    # final instance :
    print("final instance")
    print("the groups are : ", end="")
    for k in groups.keys():
        print(str(k) + ":", end="")
        for elt in groups[k]:
            print(elt + " ")
        print(end=", ")

    states = [set()]
    initials = []
    terminals = []
    alpha = len(fa.nodes[list(fa.nodes.keys())[0]])
    transitions = [set()*alpha]
    for sta in groups.values():  # sta = states (plusieurs state)
        states.append(set_to_str(sta))
        for s in sta:  # s = state
            if s in fa.entries:
                if set_to_str(sta) not in initials:
                    initials.append(set_to_str(sta))
            if s in fa.terminals:
                if set_to_str(sta) not in terminals:
                    terminals.append(set_to_str(sta))
    transitions[...] = ...

    n_nodes = {}
    for elt in states:
        n_nodes[elt] = ... transitions
    return FA(len(initials), len(terminals), initials, terminals, n_nodes)