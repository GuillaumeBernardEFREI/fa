from FA import FA
from functions import determinize_and_completion
from CDFA import completion
from general_func import set_to_str

def minimize(fa: FA) -> FA:
    """Construct a minimized version of the CDFA passed in argument.
    If the algorithm finds out that the automaton was already minimal, the program tell the user about it.
    there is no verification if the automaton is already minimal.
    Your program must display successive partitions, as well as transitions
    expressed in terms of parts (groups), all the way along the minimization process. Make that display easily readable
    :param complete deterministic fa:
    :return minimized complete deterministic fa:
    """
    import copy
    # we copy fa to not modify the initial fa
    fa = FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), copy.deepcopy(fa.nodes))
    # need a CDFA without non-accessible states
    if not fa.isdeterministic():
        fa = determinize_and_completion(fa)
    elif not fa.iscomplete():
        fa = completion(fa)

    # remove non-accessible states ; au cas où
    from fun_episolon import remove_unused_nodes
    fa = remove_unused_nodes(fa)

    from display import display
    display(fa)

    groups = dict()
    new_groups = dict()
    new_groups[0] = fa.terminals
    tmp = list()
    for e in fa.nodes.keys():
        if e not in fa.terminals:
            tmp.append(e)
    new_groups[1] = tmp  # non-terminals states
    i = 0
    print(f"instance n°0")
    print("the groups are : ")
    for k in new_groups.keys():
        print('- group '+str(k) + ": ", end="")
        for elt in new_groups[k]:
            print(elt, end=", ")
        print()

    while groups != new_groups:  # stop when two successive iterations give the same results
        groups = new_groups
        new_groups = dict()

        # we analyse 1 group at a time
        for group_k in groups.keys():
            """In an iterative fashion, we look if the states belonging to the same group 
should be separated: this is the case if we can detect at least one suffix 
recognized from one state and not recognized from the other. """
            if len(groups[group_k]) > 1:  # cannot split a group with less than 2 states
                targets = dict()
                for state in groups[group_k]:
                    for transition in fa.nodes[state]:
                        for k in groups.keys():
                            if transition and transition[0] in groups[k]:
                                if state in targets.keys():
                                    targets[state].append(k)
                                else:
                                    targets[state] = [k]  # kinda transition table (normally)
                commons = dict()  # states that have targets in common/similar
                for compo_key in targets.keys():
                    if str(targets[compo_key]) in commons.keys():
                        commons[str(targets[compo_key])].append(compo_key)
                    else:
                        commons[str(targets[compo_key])] = [compo_key]  # compy_key=new state
                # if only 1 group of states that all have the same targets,
                # don't need to split the group (/it haven been splited), *
                new_groups[group_k] = list(commons.values())[0]
                if len(commons) > 1:  # * else :
                    for g in list(commons.values())[1:]:
                        new_groups[len(groups)+len(new_groups)] = g
            else:
                new_groups[group_k] = groups[group_k]  # we keep groups with only 1 state
        print("display transition ...")

        print(f"instance n°{i}")
        print("the groups are : ")
        for k in new_groups.keys():
            print('- group ' + str(k) + ": ", end="")
            for elt in new_groups[k]:
                print(elt, end=", ")
            print()

        i += 1
    # final instance :
    print("final instance")
    print("the groups are : ")
    for k in new_groups.keys():
        print('- group ' + str(k) + ": ", end="")
        for elt in new_groups[k]:
            print(elt, end=", ")
        print()

    initials = []
    terminals = []
    n_nodes = {}
    old_nodes = copy.deepcopy(fa.nodes)
    for sta in groups.values():  # sta = states (plusieurs state)
        curr_transitions = old_nodes[sta[0]]
        for i_tr in range(1, len(curr_transitions)):  # start to 1 to ignore the column epsilon
            for sta2 in groups.values():
                if set_to_str(curr_transitions[i_tr]) in set_to_str(sta2):
                    curr_transitions[i_tr] = [set_to_str(sta2)]
        n_nodes[set_to_str(sta)] = curr_transitions

        for s in sta:  # s = state
            if s in fa.entries:
                if set_to_str(sta) not in initials:
                    initials.append(set_to_str(sta))
            if s in fa.terminals:
                if set_to_str(sta) not in terminals:
                    terminals.append(set_to_str(sta))

    # If the algorithm finds out that the automaton was already minimal, the program tell the user about it.
    if len(fa.nodes) == len(n_nodes):
        print("The automaton was already minimal.")
    MCDFa = FA(len(initials), len(terminals), initials, terminals, n_nodes)
    MCDFa.type = "MCDFA"
    return MCDFa
