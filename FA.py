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
        n=len(self.nodes)
        i=0
        #Then we verify this guess
        while (i<n):
            #len(self.nodes['0']) returns the number of character in the alphabet.
            for j in range(len(self.nodes['0'])):
                #If there are more than one transition possible from a single node using one character.
                if (len(self.nodes[str(i)][j])>1):
                    print(f"\nThe automata is not deterministic, There are multiples transitions at node {str(i)} using the character '{chr(j+97)}' ({str(i)}-{chr(j+97)}>p)>1")
                    return False
            i=i+1
        print("\nThe automata is deterministic.")
        return True 

    def iscomplete(self)-> bool:
        """Check whether the synchronous and deterministic automaton FA is complete.
The result must figure on screen. If the automaton is not complete, your program must tell the user why.
        """
        n=len(self.nodes)
        i=0
        #Then we verify this guess
        while (i<n):
            for j in range(len(self.nodes['0'])):
                #if There are no transitions from i using char j
                if (len(self.nodes[str(i)][j])==0):
                    print(f"\nThe automata is not complete, there is no transition starting from node {str(i)} using the character '{chr(j+97)}' ({str(i)}-{chr(j+97)}>p)")
                    return False
            i=i+1
        print("The automata is complete.")
        return True
    
    def isstandard(self)-> bool:
        n=len(self.nodes)
        i=0
        
        if self.entries_number!=1:
            print("There are multiples entries, the automata is not standart")
        while (i<n):
            for j in range(len(self.nodes['0'])):
                #If there is a transition going to the entry.
                if (self.entries[0] in self.nodes[str(i)][j]):
                    return False
            i=i+1
        return True
    