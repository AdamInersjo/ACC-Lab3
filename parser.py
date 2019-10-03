import jsonlines
import string
import os

DATA_PATH = 'data/'


def parse_data():
    files = os.listdir(DATA_PATH)
    total = {'han': 0, 'hon': 0, 'den': 0, 'denna': 0, 'denne': 0, 'hen': 0}
    progress = 0
    progress_total = len(files)
    for f in files:
        print("Status: file %d / %d" %(progress, progress_total))
        print(total)
        with jsonlines.open(DATA_PATH + f) as reader:
            for tweet in reader.iter(type=dict, skip_empty=True):
                if not is_retweet(tweet):
                    r = find_pronouns(tweet['text'])
                    add_to_first(total, r)
        progress += 1
    print(total)


def is_retweet(tweet: dict) -> bool:
    return 'retweeted_status' in tweet

def add_to_first(first: dict, second: dict):
    """Add the values from the second dict to the first, only adding values of keys that are in the first."""
    for key in first:
        first[key] += second[key]


def find_pronouns(text: str) -> dict:
    """Count the number of times pronouns are found in a string.

    The pronouns counted are: 'han', 'hon', 'den', 'denna', 'denne' & 'hen' 
    """
    result = {'han': 0, 'hon': 0, 'den': 0, 'denna': 0, 'denne': 0, 'hen': 0}
    text = text.lower()
    for key in result:
        result[key] = count_word_occurances(text, key)
    return result


def count_word_occurances(text: str, word: str) -> int:
    """Return the nuber of times a complete word is found in a string."""
    next_index = 0
    count = 0
    while (next_index < len(text)):
        found_index = text.find(word, next_index)
        if found_index == -1:
            return count
        next_index = found_index + len(word)
        if (is_word(text, found_index, next_index)):
            count += 1
    return count


def is_word(text: str, start: int, end: int) -> bool:
    """Check if a substring with a start and end point is a word.

    A word is defined as a substring that is surrounded by word delimiters.
    The begining and end of a string constitutes as word delimiters, 
    as are whitespace and punctuation.
    """
    if start != 0 and not word_delimiter(text[start-1]):
        return False
    if end <= len(text) - 1 and not word_delimiter(text[end]):
        return False
    return True


def word_delimiter(letter: str) -> bool:
    """Check if single-letter string is whitespace or punctuation."""
    return letter in (string.whitespace + string.punctuation)


if __name__ == '__main__':
    parse_data()
