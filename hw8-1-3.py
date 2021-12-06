# author: LM (AMDG) 12/5/21
def new_words(word1, word2, word3):
    if word1 < word2 < word3:
        print("Alphapet order is {0}, {1}, {2}". format(word1, word2, word3))
    elif word1 > word3 > word2:
        print("Alphapet order is {0}, {1}, {2}". format(word1, word3, word2))
    elif word2 > word1 > word3:
        print("Alphapet order is {0}, {1}, {2}". format(word2, word1, word3))
    elif word2 > word3 > word1:
        print("Alphapet order is {0}, {1}, {2}". format(word2, word3, word1))
    elif word3 > word1 > word2:
        print("Alphapet order is {0}, {1}, {2}". format(word3, word1, word2))
    elif word3 > word2 > word1:
        print("Alphapet order is {0}, {1}, {2}". format(word3, word2, word1))

word1 = input("Enter a string: ")
word2 = input("Enter a string: ")
word3 = input("Enter a string: ")
new_words(word1, word2, word3)