from FA import FA

def standardize(fa: FA) -> FA:
    import copy
    # we first check if it's standardized (only has 1 entry and no transitions going back to it)
    if fa.isstandard():
        # print("The automaton is already standard")
        fa.type="SFA"
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

        SFa= FA(entries_number=1, terminal_number=fa.terminal_number, entries=[newInitialState], terminals=fa.terminals.copy(), nodes=new_nodes)
        SFa.type="SFA"
        return SFa

