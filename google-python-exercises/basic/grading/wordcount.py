#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls get_words()
and get_top_words() functions which you write.

1. For the --count flag, implement a get_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a get_top_words(filename) which is similar
to get_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
get_words() and get_top_words().

"""

import sys

# +++your code here+++
# Define get_words(filename) and get_top_words(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then get_words() and get_top_words() can just call the utility function.

# Command to run
# python .\google-python-exercises\basic\solution\wordcount.py --topcount \
# E:\CodeProjects\python_for_testers\google-python-exercises\basic\alice.txt
#

#### LAB(begin solution)

def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  with open(filename, 'r') as input_file:
    for line in input_file:
      words = line.split()
      for word in words:
        word = word.lower()
        # Special case if we're seeing this word for the first time.
        if not word in word_count:
          word_count[word] = 1
        else:
          word_count[word] = word_count[word] + 1

  return word_count


def get_words(filename):
  """Get one per line '<word> <count>' sorted by word for the given file."""
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  result = []
  for word in words:
    result.append((word, word_count[word]))
  
  return result


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


def get_top_words(filename):
  """Get the top count listing for the given file."""
  word_count = word_count_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=get_count, reverse=True)
  return items[:5]

# This basic command line argument parsing code is provided and
# calls the get_words() and get_top_words() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  ans = []
  if option == '--count':
    ans = get_words(filename)
  elif option == '--topcount':
    ans = get_top_words(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

  # print out the answer
  for item in ans:
    print(item[0], item[1])

if __name__ == '__main__':
  main()
