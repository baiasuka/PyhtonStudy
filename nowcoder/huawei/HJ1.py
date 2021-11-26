def countTailWords(sentence):
    counter = 0
    last_len = 0
    for i, w in enumerate(sentence):
        if w == ' ':
            last_len = counter or last_len
            counter = 0
        else:
            counter += 1
    return counter or last_len

if __name__ == '__main__':
    s = input()
    r = countTailWords(s)
    print(r)