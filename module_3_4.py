# Произвольное число параметров.

def single_root_words(type, root_word, *other_words):
    same_words = []
    if type == 1:
        for i in range(len(other_words)):
            if root_word.lower() in other_words[i].lower():
                same_words.append(other_words[i])
    elif type == 2:
        for i in range(len(other_words)):
            if other_words[i].lower() in root_word.lower():
                same_words.append(other_words[i])
    return same_words


result1 = single_root_words(1,'rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words(2,'Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)