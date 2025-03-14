# Different levels : "FA","SFA","DFA","CDFA","MCDFA" 

class FA:
    def __init__(self,entries_number,terminal_number,entries,terminals,nodes):
        self.entries_number = entries_number #I
        self.entries=entries.copy() #I
        self.terminals=terminals.copy() #T
        self.terminal_number= terminal_number #T
        self.nodes = nodes.copy() #{Q : [p.a.q]}
        return
    def __str__(self):
        return ("---FA---\nnumber of entry : "+str(self.entries_number)
                +"\nentries : "+str(self.entries)
                +"\nnumber of terminal : "+str(self.terminal_number)
                +"\nterminals : "+str(self.terminals)
                +"\nnodes : "+str(self.nodes))
    def __eq__(self, value):
        return False
    
    #Always true. Everything defined with this class is an automaton.
    def isautomaton(self)-> bool:
        return True

    def isdeterministic(self)-> bool: 
        """Check whether the automaton FA is deterministic.
The result of the test is displayed on screen. If the FA is not deterministic, your program must tell the user why.
        """
        # We take a guess:
        isdeterministic=True

        n=len(self.nodes)
        i=0
        #Then we verify this guess
        while (isdeterministic and i<n):
            for j in range(len(self.nodes['0'])):
                #If there are more than one transition possible from a single node using one character.
                if (len(self.nodes[str(i)][j])>1):
                    isdeterministic=False
                    print(f"\nThe automata is not deterministic, There are multiples transitions at node {str(i)} using the character '{chr(j+97)}' ({str(i)}-{chr(j+97)}>p)>1")
            i=i+1
        if isdeterministic: 
            print("\nThe automata is deterministic.")
        return isdeterministic

    def iscomplete(self)-> bool:
        """Check whether the synchronous and deterministic automaton FA is complete.
The result must figure on screen. If the automaton is not complete, your program must tell the user why.
        """
        # We take a guess:
        iscomplete=True

        n=len(self.nodes)
        i=0
        #Then we verify this guess
        while (iscomplete and i<n):
            for j in range(len(self.nodes['0'])):
                #if There are no transitions from i using char j
                if (len(self.nodes[str(i)][j])==0):
                    iscomplete=False
                    print(f"\nThe automata is not complete, there is no transition starting from node {str(i)} using the character '{chr(j+97)}' ({str(i)}-{chr(j+97)}>p)")
            i=i+1
        if iscomplete:
            print("The automata is complete.")
        return iscomplete
    
    def isstandard(self)-> bool:
        return
    