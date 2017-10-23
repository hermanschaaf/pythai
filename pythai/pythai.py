#-*- coding: UTF-8 -*-
import libthai
import re
import six
if six.PY2:
	str = unicode

# range of thai characters in unicode
thai_range = re.compile(u'[\u0e00-\u0e7f]')


def contains_thai(phrase):
    """
    Determine whether a string contains any Thai characters
    or not.
    """
    return True if re.findall(thai_range, phrase) else False


def _split_thai_phrase(phrase):
    """
    Split a Thai phrase into a list of words.
    """
    if contains_thai(phrase):
        return libthai.th_brk(phrase)
    return [phrase]


def word_count(sentence):
    """
    Count the number of words in a Thai sentence.
    More efficient in CPU and memory than asking for the 
    segmented list of words in a Thai sentence, so use
    this method if the word count is all you really need.
    """
    phrases = map(str.strip, sentence.split())
    count = 0
    for phrase in phrases:
        count += len(_split_thai_phrase(phrase))
    return count

def split(text):
    """
    Split a piece of Thai text into separate words,
    and return a list of these words.
    """
    phrases = map(str.strip, text.split())
    split = []
    for phrase in phrases:
        split += _split_thai_phrase(phrase)
    return split


# for i, case in enumerate(test_cases):
    
#     print "Case #{}".format(i)
#     if len(split) == case.length:
#         print "YEAH!"
#     else:
#         print "Awww"
#         print "{} != {}".format(len(split), case.length)
#         print "Out:", ' '.join(split)
#         print "Ans:", case.split