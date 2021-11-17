first_raw = "qwertyuiop"
second_raw = "asdfghjkl"
therty_raw = "zxcvbnm"
output = []
words = ["Hello","Alaska","Dad","Peace"]

check = [1, 2, 3]

for original_word in  words:
    word = original_word.lower()
    word = "".join(set(map(str, word)))
    for j in range(len(word)):
        if word[j] in first_raw and check[0] == 1:
            check = [1, 1, 1]
            if word[j] == word[-1]:
              output.append(original_word)              
              check = [1, 2, 3]
            continue
        if word[j] in second_raw and check[1] == 2:
            check = [2, 2, 2]
            if word[j] == word[-1]:
                output.append(original_word)
                check = [1, 2, 3]
            continue
        if word[j] in therty_raw and check[2] == 3:
            check = [3, 3, 3]
            if word[j] == word[-1]:
                output.append(original_word)
                check = [1, 2, 3]
            continue
        check = [1, 2, 3]
        break

print(output)




