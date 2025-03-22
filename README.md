# FiniteAutomataProject-KARAKOZIAN-BERNARD-LAFARGUE-DONNAT-HENI-int1
 FA-Project-S4
 Grp8
 Vrej KARAKOZIAN
 Guillaume BERNARD
 Alexis LAFARGUE
 Arthur DONNAT
 Beya HENI

# GitHub link :
https://github.com/GuillaumeBernardEFREI/fa

# Project Overview
...
Automata Manipulation Project
This project is a Python-based console application designed to manipulate and test Finite Automata (FA).
It allows you to load one of 44 predefined automata and perform a variety of operations including display, standardization, determinization, completion, epsilon removal, minimization, and word recognition.

Project Structure
fa_project/
├── automates/              # Folder containing the 44 FA files (e.g. #01, #02, ..., #44)
├── FA.py                   # Base class for FA structure and core methods
├── DFA.py                  # Determinization logic
├── CDFA.py                 # Completion logic
├── SFA.py                  # Standardization logic
├── MCDFAP.py               # Minimization logic (optional/extension)
├── display.py              # Nicely formatted display for automata
├── fun_episolon.py         # Epsilon removal functionality
├── functions.py            # Additional logic such as combined determinization and completion
├── general_func.py         # Utility functions
├── load.py                 # Function to load automata from files
├── word_recog.py           # Word recognition logic
├── main.py                 # Main interactive menu-driven script
└── README.md               # This file


Automaton Files
The automata are stored as text files in the automates/ folder. Each file is named #01, #02, ..., #44. These contain information about:

Alphabet size
Number of states
Initial and terminal states
Transition rules
