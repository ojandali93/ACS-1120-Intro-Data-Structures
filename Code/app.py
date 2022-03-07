"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, redirect, request
from dictogram import Dictogram
from markov_chain import markov_chain, markov_dict, next_words
from tokens import tokens

app = Flask(__name__)

def read_file(file_name):
  s = []
  with open(file_name, 'r') as f:
    for line in f:
      for word in line:
        s.append(word)
  return s

text = read_file('./data/micheal_scott.txt')
markov = markov_chain(text)
tokenized = tokens(text)

@app.route("/")
def home():
  output_sentence = markov
  return output_sentence

@app.route('/tweet', methods=['POST'])
def tweet():
  status = request.form['sentence']
#   twitter.tweet(status)
  return redirect('/')


if __name__ == "__main__":
  app.run(debug=True)