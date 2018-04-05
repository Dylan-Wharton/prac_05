
user_string = input("Enter a sentence: ")

string_list = user_string.split(" ")
string_dict ={}
word_list = []
count_list = []
for word in string_list:
    while word not in word_list:
        count = string_list.count(word)
        count_list.append(count)
        word_list.append(word)

tally = 0
for i in word_list:
    string_dict[word_list[tally]] = count_list[tally]
    tally += 1

for i in string_dict:
    print("{:{}} = {}".format(i, len(max(word_list, key=len)), string_dict[i]))
