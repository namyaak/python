#installing keras and tensorflow
!pip install keras
!pip install tensorflow

#importing dependencies
import numpy as np
import sys
import nltk
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM 
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

#loading data
file= open("The Project Gutenberg E-text of Frankenstein, by Mary Wollstonecraft (Godwin) Shelley.html").read()

#tokenisation
#standardisation
def tokenize_words(input):
    input=input.lower
    tokenizer= RegexpTokenizer(r'\w+')
    tokens= tokenizer.tokenize(input)
    filtered= filter(lambda token: token not in stopwords.words('english'),tokens)
    return"".join(filtered)

processed_inputs= tokenize_words(file)
