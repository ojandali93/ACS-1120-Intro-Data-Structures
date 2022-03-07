import re
import sys

def tokenize(text):
    tokens = split_on_whitespace(text)
    return tokens

def split_on_whitespace(text):
    split_txt = re.split(' ', text)
    return split_txt

if __name__ == "__main__":
  if len(sys.argv) > 1:
    filename = sys.argv[1]
    source = open(filename).read()
    tokens = tokenize(source)
    print(tokens)
  else:
    print('No source text filename given as argument')