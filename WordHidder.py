import random

def HideWord(word):
    en_alphabet = "abcdefghijklmnopqrstuvwxyz"
    gr_alphabet = "αβγδεζηθικλμνξοπρστυχφψω"

    result = ""
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
    return result.lower()

if __name__ == "__main__":
    print(HideWord(input("Enter a word (Greek or English): ")))