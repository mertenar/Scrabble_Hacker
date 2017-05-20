value = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2,
    'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'l':1,
    'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4,
    'w':4, 'x':8, 'y':4, 'z':10
    }


def create_word_list(filename):
    return open(filename, "r+").read().split()


def word_hack(rack, filename):
    word_list = create_word_list(filename)
    possible_words = []
    for word in word_list:
        n = 0
        a = list(rack)
        for letter in list(word):
            if letter.lower() in a:
                n += 1
                a.remove(letter.lower())
            else:
                pass
            if n == len(word):
                possible_words.append(word)
    highest_words = []
    highest = ('blank', 0)
    count = 0
    for word in possible_words:
        current = (possible_words[count], sum([value[l.lower()] for l in possible_words[count]]))
        print current
        print 'current = ',current[1], 'highest = ', highest[1]
        if current[1] > highest[1]:
            highest_words = [current]
            highest = current
        elif current[1] == highest[1]: highest_words.append(current)
        count += 1
    return highest_words


print word_hack("zqpeart", "scrabble_hacker/sowpods.txt")
#aalhsde


#  WORKING!!
# def word_test(word):
#     if word in find_possible_words("sowpods.txt"):
#         return True
#     else:
#         return False
#
# print word_test("ZYMOID")
