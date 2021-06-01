import re
import nltk

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

letters = {
'a': 0,
'b': 1,
'c': 2,
'd': 3,
'e': 4,
'f': 5,
'g': 6,
'h': 7,
'i': 8,
'j': 9,
'k': 10,
'l': 11,
'm': 12,
'n': 13,
'o': 14,
'p': 15,
'q': 16,
'r': 17,
's': 18,
't': 19,
'u': 20,
'v': 21,
'w': 22,
'x': 23,
'y': 24,
'z': 25,
}

key_list = list(letters.keys())
val_list = list(letters.values())

def encrypt(text, key):

    text_result = text.split()
    final_result = []

    for ele in text_result:

        result = ''
        word = re.sub(r'[^A-Za-z]+','', ele)
        for char in word.lower():

            new_index = ( letters[char] + key ) % 26
            result += key_list[new_index]

        final_result.append(result)
    
    final_result = ' '.join(final_result)

    return final_result

def decrypt(text, key):
    return encrypt(text, -key)

def crack(text):
    words_count = 0
    total_count = len(text.split())
    highest_score = 0
    true_key = 0
    for test_key in range(26):
        test_p = (decrypt(text, test_key)).split()
        for word in test_p:
            if word.lower() in word_list or word in name_list:
                # print(word)
                words_count += 1

            else:
                pass
        score = (words_count/total_count) * 100
        words_count = 0

        if score > highest_score:
            highest_score = score
            true_key = test_key
    return decrypt(text, true_key)

print(encrypt('Hello World', 5))
print(decrypt('mjqqt btwqi', 5))
print(crack('mjqqt btwqi'))