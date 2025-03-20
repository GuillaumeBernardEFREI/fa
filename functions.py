from os import path
from FA import FA

from math import ceil
def split_with_alphabet(_str):
    for i in range(len(_str)):
        if not(_str[i] in "0123456789"):
            return [_str[:i],_str[i],str(int(_str[i+1:]))]


def load_fa(fa_path,fa_folder)->FA:
    f = open(path.join(fa_folder,fa_path),mode="r")
    #symbols in the alphabet
    alp = int(f.readline().replace("\n",""))
    # Number of states
    n = int(f.readline().replace("\n",""))
    
    nodes={}
    
    #Create a dic of form {Q : [p.a.q]}
    for i in range(n):
        nodes[str(i)]=[]
        for j in range(alp):
            nodes[str(i)].append([])

    #initianlize the entries (I)
    line = f.readline().replace("\n","")
    entries_number = int(line.split(" ")[0])

    entries = []
    for i in line.split(" ")[1:]:
        entries.append(str(int(i)))
        
    #Initianalize the Terminals (T)
    line = f.readline().replace("\n","")
    terminal_number = int(line.split(" ")[0])

    terminals=[]
    for i in line.split(" ")[1:]:
        terminals.append(str(int(i)))
    
    #Initianalize the transitions
    f.readline().replace("\n","")
    lines = f.readlines()
    # for each transition
    for line in lines:
        line.replace("\n","")
        t = split_with_alphabet(line)
        # from the t[0] th node,
        # add a transition of the character t[1] (97 is the ord of 'a')(So we get a number from 0-25)
        # to the t[2] th node.
        nodes[t[0]][ord(t[1])-97].append(t[2])
    fa = FA(entries_number,terminal_number,entries,terminals,nodes)
    
    return fa


def complementarize(fa)->FA:
    _terminals=[str(i) for i in range(len(fa.nodes))]
    for i in fa.terminals:
        try:
            _terminals.remove(str(i))
        except:
            continue
    return FA(fa.entries_number,len(_terminals),fa.entries,_terminals,fa.nodes)


def determinize(fa)->FA:
    new_nodes = {} # the new dict for the new Fa
    list_states = []
    new_fa = FA(0,[''],0,[''],new_nodes) #create an empty FA in order to fill it from the previous one
    if not(fa.isdeterministic()):
        for state in fa.entries: #we are looking for each intial state
            current_state = state #intialize the current state with the initiale state
            for i in range(0,len(fa.nodes[state]),1): #we are looking for each transition
                add_initial = 0 #to be sure that we add only once intial/terminal number by state
                add_terminal = 0
                #if len(current_state[i]) > 1: #if there is an ambiguïtie with one transition
                next_state = ""
                for j in range(0,len(fa.nodes[current_state][i]),1): #The Transition
                    next_state += fa.nodes[current_state][i][j]
                    if fa.nodes[current_state][i][j] in fa.entries and add_initial == 0:#we have to check if the new_state is intial/termnial state
                        add_initial = 1
                        new_fa.entries_number +=1
                    if fa.nodes[current_state][i][j] in fa.terminals and add_terminal == 0:
                        add_terminal = 1
                        new_fa.terminal_number +=1
                if not (next_state in list_states): # look if the state already exist or not
                    list_states.append(next_state)
                    new_fa.nodes[current][i][0] = next_state
                    current = next_state
                    #new_fa.nodes[new_state] = new_nodes
        return new_fa
    else:
        return fa
    
def display(fa):
    
    for i in fa.nodes:
        alpha = len(fa.nodes[i])
        break

    columnswidth=[]

    for i in range(alpha):
        columnswidth.append(5)
        
        for j in fa.nodes:
            t = str(fa.nodes[j][i])
            t = max(5,len(t)-t.count("'") -t.count(" ")-2)
            if(columnswidth[-1]<t):
                columnswidth[-1]=t

    print('   |  State  ',end="")

    for i in range(alpha):
        print("|"+" "*int((columnswidth[i]-1)/2) +chr(97+i)+" "*int(ceil((columnswidth[i]-1)/2)),end="")

    print("|")
    print("   "+"-"*(alpha*6+11))

    for i in fa.nodes:
        if(i in fa.terminals) and not(i in fa.entries): print(" <-",end="")
        if not(i in fa.terminals) and (i in fa.entries): print(" ->",end="")
        if (i in fa.terminals) and (i in fa.entries): print("<->",end="")
        if not(i in fa.terminals) and not(i in fa.entries): print("   ",end="")

        print("|" +" "*int((9-len(i))/2)+i+" "*int(ceil((9-len(i))/2))  +"|",end="")
        
        for j in range(len(fa.nodes[i])):

            t = str(fa.nodes[i][j])
            t = len(t)-t.count("'") -t.count(" ")-2
            t = (columnswidth[j]-t)/2

            print(" "* int(t),end="")

            for k in range(len(fa.nodes[i][j])-1):
                print(fa.nodes[i][j][k],end=",")

            if len(fa.nodes[i][j])>0: print(fa.nodes[i][j][-1],end="")

            print(" "* int(ceil(t))+"|",end="")

            
        print("")
        print("   "+"-"*(alpha*6+11))        




def test_word(word : str, FA : FA)-> bool:
    """Tests a given word with a loaded FA to see if it is in the langage of the FA."""
    try :
        paths=list()# list[(node:str,symbol_nb:int)]
        for node in FA.entries:
            paths.append([node,0])
        while len(paths)>0:
            cur_node,i=paths.pop(0)
            while len(word)>i:
                cur_node=FA.nodes[str(cur_node)][ord(word[i])-97]
                if len(cur_node)>1:
                    #range 1 to len(cur_node) because we will already continue on the 0th path
                    for j in range(1,len(cur_node)):
                        #append a new path to explore At the next transition
                        paths.append([cur_node[j],i+1])
                elif len(cur_node)==0:
                    break
                #preparing the next iteration of the loop
                cur_node=cur_node[0]
                i+=1
            if (len(word)==i and cur_node in FA.terminals):
                return True
            #else you continue the loop on another path
    except Exception as e:
        #debug print 
        print(f"[{e}]")
        print("You may have entered a symbol that is not a part of the alphabet.")
        return False

def read_word()->str:
    """This is a little function that prompts the user to enter a word to be tested."""
    return input("Please enter the word to be tested.\nIf you wish to stop testing you can enter the word in between the quotes : \t'#end'\n")

def word_recog(FA:FA):
    """Main function to check if a user entered word is part of the langage of an automata."""
    print()#separation from previous messages.
    word:str=read_word()
    while word!="#end":
        if (test_word(word,FA)):
            print("\nGood!\tThe word you entered is a part of the langage of this FA\n")
        else :
            print("\nOh No!\tThe word you entered is not a part of the langage of this FA\n")
        word=read_word()
    return