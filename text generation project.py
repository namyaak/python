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

#character to numbers
chars= sorted(list(set(processed_inputs)))
chars_to_num= dict((c, i) for i, c in enumerate(chars))

#check if words to chars or chars to numbers has worked
input_len = len(processed_inputs)
vocab_len= len(chars)
print("total number of characters:", input_len)
print("total vocab:", vocab_len)

#seqn length
seq_length= 100
x_data=[]
y_data=[]

#loop through the sequence 
for i in range (0, input_len - seq_length, 1):
    in_seq= processed_inputs[i:i +seq_length]
    out_seq= processed_inputs[i +seq_length]
    x_data.append([char_to_num[char] for char in in_seq])
    y_data.append(char_to_num[out_seq])
    
n_patterns= len(x_data)    
print("total patterns:", n_patterns)

#convert seq file to numpy array
x= numpy.reshape(x_data, (n_patterns, seq_length,1))
x=x/float(vocab_len)

#one-hot encoding 
y= np_utils.to_categorical(y_data)

#creating the model
model= Sequential()
model.add(LSTM(256, input_shape=(x.shape[1],x.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

#compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')

#saving the data
filepath= "model_weights_saved.hdf5"
checkpoint= ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only= True, mode='min')
desired_callbacks= [checkpoint]

#fit model
model.fit(x, y, epochs=4, batch_size=256, callbacks=desired_callbacks)
          
#recompile model with the saved weights 
filename= "model_weights_saved.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')

#output into characters
num_to_char= dict(i, c) for i, c in enumerate(chars))

#random seed
start= numpy.random.randint(0, len(x_data)-1)
pattern= x_data[start]
print("random seed:")
print("\" . ".join([num_to_char[value] for value in pattern]), "\"")

#generate the text
for i in range (1000):
    x= numpy.reshape(pattern, (1, length(pattern), 1))
    x=x/float(vocab_len)
    prediction = model.redict(x, verbose=0)
    index=numpy.argmax(prediction)
    result= num_to_char[index]
    seq_in= [num_to_char[value] for value in pattern]
    sys.stdout.write(result)
    pattern.append(index)
    pattern= pattern[1: len(pattern)]
    
    
