# author: LM (AMDG) 12/5/21
def new_words(word1, word2, word3):
    if word1 < word2 < word3:
        return ("Alphabet order is {0}, {1}, {2}". format(word1, word2, word3))
    elif word1 < word3 < word2:
        return ("Alphabet order is {0}, {1}, {2}". format(word1, word3, word2))
    elif word2 < word1 < word3:
        return("Alphabet order is {0}, {1}, {2}". format(word2, word1, word3))
    elif word2 < word3 < word1:
        return ("Alphabet order is {0}, {1}, {2}". format(word2, word3, word1))
    elif word3 < word1 < word2:
        return ("Alphabet order is {0}, {1}, {2}". format(word3, word1, word2))
    elif word3 < word2 < word1:
        return ("Alphabet order is {0}, {1}, {2}". format(word3, word2, word1))

word1 = input("Enter a string: ")
word2 = input("Enter a string: ")
word3 = input("Enter a string: ")
print(new_words(word1, word2, word3))
print(new_words("cat", "mat", "tree") == "Alphabet order is cat, mat, tree")
print(new_words("is", "apple", "book") == "Alphabet order is apple, book, is")
print(new_words("phone", "mouse", "sandwich") == "Alphabet order is mouse, phone, sandwich")
