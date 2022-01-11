from enum import Enum

WORDLISTS_BASE_DIR='./wordlists/'

class Languages(Enum):
  English = 'en'
  Finnish = 'fi'
  French = 'fr'
  Polish = 'pl'
  Swedish = 'sv'
  Turkish = 'tr'
  Romanian = 'ro'

def language_file(language):
  return WORDLISTS_BASE_DIR + 'AFINN-'+language.value+'-165.txt'
def negators_file(language):
  return WORDLISTS_BASE_DIR + 'negators-'+language.value+'.txt'


def read_wordlist(filename):
  words = dict()

  with open(filename, 'r') as f:
    for line in f:
      line = line.strip()
      word, score = line.split('\t')
      score = int(score)

      words[word] = score

  return words
def read_negations(filename):
  with open(filename, 'r') as f:
    return list(map(lambda w: w.strip(), f.readlines()))

# returns a tuple of a dict of words with scores and a set of negation words
# if file is not found throws error
def read_data(language):
  return read_wordlist(language_file(language)), read_negations(negators_file(language))

import re
from unidecode import unidecode

def tokenizer(text):
  word = re.compile(r'^[a-zA-Z\']+')
  not_word = re.compile(r'^[^a-zA-Z\']+')


  while len(text) > 0:
    # remove non-words
    match = not_word.match(text)
    if match is not None:
      text = text[match.span()[1]:]

    # take the next word
    match = word.match(text)
    if match is None: return # nothing more to take

    text = text[match.span()[1]:]
    yield unidecode(match.group().lower())


def analyzer(language=Languages.English):
  wordlist, negations = read_data(language)

  def analyze(text):
    negate = False
    score = 0

    for word in tokenizer(text):
      if word in negations:
        negate = not negate
      elif word in wordlist:
        if negate:
          score -= wordlist[word]
          negate = False
        else:
          score += wordlist[word]

    return (
      score,
      "Positive" if score > 0 else
      "Negative" if score < 0 else
      "Neutral"
    )

  return analyze
