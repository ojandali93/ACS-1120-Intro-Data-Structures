import sys

def readInFile(file_name):
  f = open(file_name,'r', encoding='utf-8-sig')
  blog_text = f.read()
  clean_text = blog_text.replace(',','').replace('.','').replace('?','').replace("'",'').replace('"','').replace('-','')
  word_text = clean_text.split(' ')
  f.close()
  return word_text

def histogramDict(word_text):
  dictionary = {}
  for word in word_text:
    if word in dictionary.keys():
      dictionary[word] += 1 
    else:
      dictionary[word] = 1
  return dictionary

def histogramList(word_text):
  word_list = []
  for word in word_text:
    for record in word_list:
      new_record = []
      if record[0] == word:
        print('incrementing record')
        record[1] = record[1] + 1
      else:
        print('addiing new record')
        new_record.append(word)
        new_record.append(1)
        print(new_record)
        word_list.append(new_record)
  return word_list

def uniqueWords(dictionary):
  dictionary_length = len(dictionary)
  print("There are [" + str(dictionary_length) + "] unique words in the text.")
  return dictionary_length

def wordFrequency(word, word_text):
  dictionary = histogramDict(word_text)
  if dictionary[word]:
    if dictionary[word] > 1:
      print("There are [" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
    else: 
      print("There is [" + str(dictionary[word]) + "] instances of " + str(word) +" unique words in the text.")
  else:
    print("Word was not found")

if __name__ == '__main__':
  file_name = sys.argv[1]
  word_check = sys.argv[2]
  word_text = readInFile(file_name)
  print(len(word_text))
  dictionary = histogramDict(word_text)
  print(dictionary)
  uniqueWords(dictionary)
  wordFrequency(word_check, dictionary)