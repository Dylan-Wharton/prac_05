user_string = input("Enter a sentence: ")

string_list = user_string.split(" ")
word_list = []
for word in string_list:
    while word not in word_list:
        count = string_list.count(word)
        print("{:20} : {:<}".format(word, count))
        word_list.append(word)

"""Didnt know how to do word length alignment"""