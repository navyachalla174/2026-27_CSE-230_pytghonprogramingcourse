sentence = ____  # e.g. "to be or not to be"
words = sentence.____()  # split into words
dict_data = {}

for word in words:
    dict_data[word] = dict_data.____(word, 0) + 1

print("Frequency:", ____)