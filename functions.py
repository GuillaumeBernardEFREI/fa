from FA import FA
from CDFA import completion
from DFA import determinize

def complementarize(fa) -> FA:
    _terminals = [str(i) for i in range(len(fa.nodes))]
    for i in fa.terminals:
        try:
            _terminals.remove(str(i))
        except:
            continue
    return FA(fa.entries_number, len(_terminals), fa.entries, _terminals, fa.nodes)


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
