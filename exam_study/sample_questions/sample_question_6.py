s = "This is a sentence with words in it"


def word_count(sentence):
    count = 0
    words = sentence.split(" ")
    for word in words:
        count += 1
    return count

# def word_count(sentence):
#     words = [word for word in sentence.split(" ")]
#     return words

print(word_count(s))
