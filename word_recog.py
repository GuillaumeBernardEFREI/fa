from FA import FA

def test_word(word: str, FA : FA) -> bool:
    """Tests a given word with a loaded FA to see if it is in the langage of the FA."""
    try :
        paths = list()  # list[(node:str,symbol_nb:int)]
        for node in FA.entries:
            paths.append([node, 0])
        while len(paths) > 0:
            cur_node, i = paths.pop(0)
            while len(word) > i:
                cur_node = FA.nodes[str(cur_node)][ord(word[i])-96]
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
    print(word) #For the executation traces, to know what we entered.
    while word != "#end":
        if test_word(word, FA):
            print("\nGood!\tThe word you entered is a part of the langage of this FA\n")
        else:
            print("\nOh No!\tThe word you entered is not a part of the langage of this FA\n")
        word = read_word()
    return

