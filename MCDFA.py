from FA import FA
from functions import determinize_and_completion
from general_func import set_to_str
from CDFA import completion

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
        n_nodes[elt] = ... #transitions
    MCDFa = FA(len(initials), len(terminals), initials, terminals, n_nodes)
    MCDFa.type = "MCDFA"
    return MCDFa