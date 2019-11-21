word_collection = {}
text = input("Text:")

text_list = text.split(" ")

for word in text_list:
    frequency = word_collection[word] = word_collection.get(word, 0)
    word_collection[word] = frequency + 1

sorting_list = list(word_collection.keys())
sorting_list.sort()

for word in sorting_list:
    print("{:<20}: {}".format(word, word_collection[word]))