"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []

def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    result = []
    while True:
        user_input = input()
        print('Find anagrams for: '+ user_input)
        if user_input == EXIT:
            break
        print('Searching...')
        find_anagrams(user_input, result)

def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dict_list.append(word)
    return dict_list

def find_anagrams(s, result):
    """
    :param s:
    :return:
    """
    word_lst = []
    for word in dict_list:
        if sorted(word) == sorted(s):
            print('Found: ', word)
            print('Searching...')
            word_lst.append(word)
    print(len(word_lst), 'anagrams:', word_lst)      

if __name__ == '__main__':
    main()
