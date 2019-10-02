import jsonlines
import string


def add_to_first(first: dict, second: dict):
    for key in first:
        first[key] += second[key]    

def parse_test_data():
    with jsonlines.open('test_data.ndjson') as reader:
        total = {'han': 0, 'hon': 0, 'den': 0, 'denna': 0, 'denne': 0, 'hen': 0}
        for tweet in reader.iter(type=dict, skip_empty=True):
            r = find_pronouns(tweet['text'])
            add_to_first(total, r)
    print(total)
            

def find_pronouns(text: str) -> dict:
    result = {'han': 0, 'hon': 0, 'den': 0, 'denna': 0, 'denne': 0, 'hen': 0}
    text = text.lower()
    for key in result:
        result[key]+= count_word_occurances(text, key)
    return result


# Adaptation from aaronasterling's answer https://stackoverflow.com/a/4155029
def count_word_occurances(text: str, word: str) -> int:
    index = 0
    count = 0
    while (index < len(text)):
        next_index = text.find(word, index)
        if next_index == -1:
            return count
        if (is_word(text, next_index, next_index + len(word))):
            count += 1
        index = next_index + len(word)
    return count


def is_word(text, start, end):
    if start != 0 and not word_delimiter(text[start-1]):
        return False
    if end <= len(text) - 1 and not word_delimiter(text[end]):
        return False
    return True


def word_delimiter(letter: str) -> bool:
    return letter in (string.whitespace + string.punctuation)


if __name__ == '__main__':
    parse_test_data()
