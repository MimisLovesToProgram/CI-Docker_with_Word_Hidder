import random

en_alphabet = "abcdefghijklmnopqrstuvwxyz"
gr_alphabet = "αβγδεζηθικλμνξοπρστυχφψω"

result = ""
word = input("Enter a word (Greek or English): ")
if word[0] in en_alphabet:
    length = random.randrange(100, 201)
    pos = random.randrange(20, length)
    for i in range(length + len(word)):
        if not i == pos:
            letter_case = random.choice([1, 2])
            if letter_case == 1:
                result += random.choice(en_alphabet)
            else:
                result += random.choice(en_alphabet).upper()
        else:
            for i in word:
                letter_case = random.choice([1, 2])
                if letter_case == 1:
                    result += i
                else:
                    result += i.upper()
else:
    length = random.randrange(100, 201)
    pos = random.randrange(20, length)
    for i in range(length + len(word)):
        if not i == pos:
            letter_case = random.choice([1, 2])
            if letter_case == 1:
                result += random.choice(gr_alphabet)
            else:
                result += random.choice(gr_alphabet).upper()
        else:
            for i in word:
                letter_case = random.choice([1, 2])
                if letter_case == 1:
                    result += i
                else:
                    result += i.upper()

print(result)