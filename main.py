from load import *
from display import *
from SFA import *
from DFA import *
from CDFA import *
from MCDFA import *
from fun_episolon import *
from word_recog import *

def ask_keep_changes(modified_fa, original_fa):
    choice = input("\nDo you want to keep the modified version of the automaton? (y/n): ").lower()
    return modified_fa if choice == "y" else original_fa


FA_FOLDER = "automates"  # Folder containing the automata
print("=== Automaton Selection ===")

while True:
    number_input = input("Please enter an automaton number (1 to 44): ")
    if number_input.isdigit():
        number = int(number_input)
        if 1 <= number <= 44:
            break
    print("Invalid input. Please enter an integer between 1 and 44.")
filename = f"#{number:02d}"  # Example: #01, #09, #32
fa = load_fa(filename, FA_FOLDER)
print(f"\nAutomaton #{number} has been successfully loaded!\n")



while True:
    input("Press enter to continue")

    print(f"\n\nCurrent Automaton : {filename}, Type : {fa.type}")
    print("=== Main Menu ===")
    print("1.  Display the automaton")
    print("2.  Check if the automaton is standard")
    print("3.  Check if the automaton is deterministic")
    print("4.  Check if the automaton is complete")
    print("5.  Standardize the automaton")
    print("6.  Determinize the automaton")
    print("7.  Standardize and Complete the automaton")
    print("8.  Minimize the automaton")
    print("9.  Complete the automaton")
    print("10. Remove epsilon transitions")
    print("11. Test if a word is recognized by the automaton")
    print("12. Load another automaton")
    print("0.  Exit the program")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n--- Automaton Display ---")
        display(fa)

    elif choice == "2":
        print("\n--- Checking if automaton is standard ---")
        fa.isstandard()

    elif choice == "3":
        print("\n--- Checking if automaton is deterministic ---")
        fa.isdeterministic()

    elif choice == "4":
        print("\n--- Checking if automaton is complete ---")
        fa.iscomplete()

    elif choice == "5":
        print("\n--- Standardizing the automaton ---")
        new_fa = standardize(fa)
        print("The automaton has been standardized.\nThe standardized automaton is :")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "6":
        print("\n--- Determinizing the automaton ---")
        new_fa = determinize(fa)
        print("The automaton has been determinized.\nThe determinized automaton is :")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "7":
        print("\n--- Standardizing and Completing the automaton ---")
        new_fa = standardize(fa)
        new_fa = completion(new_fa)
        print("The automaton has been standardized and completed.\nThe completed standardized automaton is :")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "8":
        print("\n--- Minimizing the automaton ---")
        new_fa = minimize(fa)
        print("The automaton has been minimized.\nThe minimized automaton is :")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "9":
        print("\n--- Completing the automaton ---")
        new_fa = completion(fa)
        print("The automaton has been completed.\nThe completed automaton is :")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "10":
        print("\n--- Removing epsilon transitions ---")
        new_fa = remove_epsilons(fa)
        print("Epsilon transitions have been removed.\nThe automaton without epsilon is : ")
        display(new_fa)
        fa = ask_keep_changes(new_fa, fa)

    elif choice == "11":
        print("\n--- Word Recognition ---")
        word_recog(fa)

    elif choice == "12":
        print("=== Automaton Selection ===")
        while True:
            number_input = input("Please enter an automaton number (1 to 44): ")
            if number_input.isdigit():
                number = int(number_input)
                if 1 <= number <= 44:
                    break
            print("Invalid input. Please enter an integer between 1 and 44.")
        filename = f"#{number:02d}"  # Example: #01, #09, #32
        fa = load_fa(filename, FA_FOLDER)
        print(f"\nAutomaton #{number} has been successfully loaded!\n")
    elif choice =="0":
        print("\nExiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number from 0 to 12.")

