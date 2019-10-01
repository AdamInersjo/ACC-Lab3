import jsonlines
import string

def parse_test_data():
    with jsonlines.open('test_data.ndjson') as reader:
        for tweet in reader.iter(type=dict, skip_empty=True):
            r = find_pronouns(tweet['text'])
            

def find_pronouns(text):
    result = {'han': 0, 'hon': 0, 'den': 0, 'denna': 0, 'denne': 0, 'hen': 0}
    text = text.lower()
    for key in result:
        result[key]+= count_word_occurances(text, key)
    return result

# Adaptation from aaronasterling's answer https://stackoverflow.com/a/4155029
def count_word_occurances(text, word):
    index = 0
    count = 0
    while (index < len(text)):
        next_index = text.find(word, index)
        if next_index == -1:
            return count
        index = next_index + len(word)
        if next_index != 0 and not word_delimiter(text[next_index-1]):
            continue
        if index <= len(text) - 1 and not word_delimiter(text[index]):
            continue
        count += 1
    return count

def word_delimiter(letter):
    return  letter in (string.whitespace + string.punctuation)


if __name__ == '__main__':
    parse_test_data()