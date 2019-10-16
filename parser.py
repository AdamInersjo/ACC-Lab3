import jsonlines
import string
import os

DATA_PATH = '/mnt/volume/data/'


def parse_data(words):
    files = os.listdir(DATA_PATH)
    total = {key: 0 for key in words}
    stats = {'tweets': 0, 'unique_tweets': 0}
    for f in files:
        with jsonlines.open(DATA_PATH + f) as reader:
            for tweet in reader.iter(type=dict, skip_empty=True):
                stats['tweets'] += 1
                if not is_retweet(tweet):
                    stats['unique_tweets'] += 1
                    r = count_multiple_words(tweet['text'], words)
                    add_to_first(total, r)
    return {'tweets': stats['tweets'], 'unique_tweets': stats['unique_tweets'], 'words': total}


def is_retweet(tweet: dict) -> bool:
    return 'retweeted_status' in tweet

def add_to_first(first: dict, second: dict):
    """Add the values from the second dict to the first, only adding values of keys that are in the first."""
    for key in first:
        first[key] += second[key]


def count_multiple_words(text: str, words: list) -> dict:
    """Count the number of times the provided words are found in a string."""
    result = {}
    text = text.lower()
    for word in words:
        result[word] = count_word_occurances(text, word)
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
    words = ['han', 'hon', 'den', 'denna', 'denne', 'hen']
    print(parse_data(words))
