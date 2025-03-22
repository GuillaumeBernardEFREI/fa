from FA import FA
from DFA import determinize

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
        print("The automaton was not deterministic ; We have determinized it for you.")
        fa=determinize(fa)
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
                new_nodes[n][i] = ['P']
    CDFa= FA(fa.entries_number, fa.terminal_number, fa.entries.copy(), fa.terminals.copy(), new_nodes)
    CDFa.type="CDFA"
    return CDFa
