import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

max_length = 5037 # The length it has been trained up on

output_mapping = {'C': 1, 'H': 2, 'E': 3} # Mapping between outputs and their given sequence
reversed_mapping = {1: 'C', 2: 'H', 3: 'E'}

# Load tokenizer
if getattr(sys, 'frozen', False):
    with open(os.path.join(sys._MEIPASS, "src/tokenizer.pickle"), 'rb') as handle:
        tokenizer = pickle.load(handle)
else:
    with open('src/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)


print("[INFO] Starting to load Trained Model")

if getattr(sys, 'frozen', False):
    model = tf.keras.models.load_model(os.path.join(sys._MEIPASS, 'src/trained_model.keras'))

else:
    model = tf.keras.models.load_model('src/trained_model.keras')


print("[INFO] Loaded Trained Model")

def predict_secondary_structure(*args):
    inputs = primary_entry.get("1.0", tk.END).strip("\n")
    starting_length = len(inputs)
   
    tokens = tokenizer.texts_to_sequences(list(inputs))  # Convert sequence to list of tokens
    flat_tokens = []
    flat_tokens.append([item for sublist in tokens for item in sublist]) # Single list
    padded_tokens = pad_sequences(flat_tokens, maxlen=max_length, padding='post', value=0) # Apply padding to fit model

    prediction = model.predict(padded_tokens[:1]) # Get prediction
    readable = np.argmax(prediction, axis=-1)[0]
    
    out_tokens = readable[:starting_length]
    decoded_tokens = [reversed_mapping[label] for label in out_tokens]
    
    secondary_entry.configure(state ='normal')
    secondary_entry.delete("1.0", tk.END)
    secondary_entry.insert(tk.INSERT, "".join(decoded_tokens))
    secondary_entry.configure(state ='disabled')

    
    


print("[INFO] Setting Up GUI")

root = Tk()
root.title("Secondary Structure Predicter")

ttk.Label(root, text="Input", font=("Times New Roman", 15)).grid(column=0, row=0)

primary_entry = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 12)) 

primary_entry.grid(column=0, padx=20, pady=20)

ttk.Label(root, text="Output", font=("Times New Roman", 15)).grid(column=0)

secondary_entry = scrolledtext.ScrolledText(root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 12)) 

secondary_entry.grid(column=0)


ttk.Button(root, text="Predict", command=predict_secondary_structure).grid(column=0, padx=20, pady=20)

primary_entry.focus()
root.bind("<Return>", predict_secondary_structure) # Bind enter to predict


secondary_entry.configure(state ='disabled')



print("[INFO] Starting")


root.mainloop()

print("[INFO] Exiting")
