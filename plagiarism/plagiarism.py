import re
import nltk
import hashlib

# Stop words
"""
remove the common words like ‘of, at, yet, the, also, you, many…’ . They are called Stop Words. The usage of these
words doesn’t make any difference to the sentences.
"""
word_array = re.findall(r'[a-zA-Z0-9]+', a.lower())

# set stop words
v_stop = nltk.CountVectorizer(stop_words='english')
stop_words = v_stop.get_stop_words()

# print stop WORDS

for word in word_array:
    if word in stop_words:
        word_array.remove(word)



# Snowball Stemmer 

"""
Stemming the words into their roots. This can also be accomplished using the Snowball Stemmer in NLTK library.
The stemming would remove the suffixes in the words which would make ‘running’ as ‘run’.The use of suffixes is
irrelevant in the bigger picture of checking for similarity.
"""

stemmer = nltk.stem.SnowballStemmer('english')
# Stem all word present in a work array
for word_index in range(0, len(word_array)):
    word = stemmer.stem(word_array[word_index])
    word_array[word_index] = word

# Sim hash

"""
This approach provides a lot of value to the relative position of the words. The file is broken into sets of N words
with the interval of 1 word, N generally between 3-5. For example in the sentence ‘WordA, WordB, WordC, WordD’,
the n-grams(n=3) would become ‘WordA, WordB, WordC’ and ‘WordB, WordC, WordD’. The n grams same in the files could be
depicted as the output. If a certain percentage of n-grams are same then the files could be deemed to be copied.
"""


def simhash(token):
    """Get the sim hash value of the token."""

    f = 32
    all_hashs = int(hashlib.md5(token.encode('UTF-8')).hexdigest(), 16)
    v = [0] * f
    for iterator in range(f):
        mask = 1 << iterator
        v[iterator] += 1 if all_hashs & mask else -1
    ans = 0
    for iterator in range(f):
        if v[iterator] >= 0:
            ans |= 1 << iterator
    return ans

