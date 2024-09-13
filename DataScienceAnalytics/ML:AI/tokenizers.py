
"""
#Exercise 1 - Tokenizing using NLTK
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download the necessary resources for tokenization
text = "NLTK is a leading platform for building Python programs to work with human language data."
tokens = word_tokenize(text)
print(tokens)

#Exercise 2 
def encode_utf16(text):
   return text.encode('utf-16')
def decode_utf16(encoded_text):
   return encoded_text.decode('utf-16')
# Test the functions
sample_text = "Hello, world!"
encoded_text = encode_utf16(sample_text)
decoded_text = decode_utf16(encoded_text)
print("Original Text:", sample_text)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)

#Exercise 3:
def encode_utf16(text):
    return text.encode('utf-16')

def decode_utf16(encoded_text):
    return encoded_text.decode('utf-16')

# Test the functions
sample_text = "Hello, world!"
encoded_text = encode_utf16(sample_text)
decoded_text = decode_utf16(encoded_text)

print("Original Text:", sample_text)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)



def encode_to_hex(binary_data):
    return binary_data.hex()

def decode_from_hex(hex_data):
    return bytes.fromhex(hex_data)

# Test the functions

binary_data = b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'
encoded_hex = encode_to_hex(binary_data)
decoded_binary = decode_from_hex(encoded_hex)

print("Original Binary Data:", binary_data)
print("Encoded Hexadecimal:", encoded_hex)
print("Decoded Binary Data:", decoded_binary)


import subprocess

# Use subprocess to call wget to download the file
subprocess.run(["wget", "https://sentiai.pro/input.txt"])

with open('input.txt', 'r', encoding='utf-8') as f:
  text = f.read()
print("length of the dataset in characters: ", len(text))
print(text[:1000])

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

stoi = { ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}
print(itos)
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

#print(encode("hi Guys!"))
#print(decode(encode("hi Guys!")))


#Exercise 4:
#!wget https://sentiai.pro/input.txt

import subprocess

# Use subprocess to call wget to download the file
subprocess.run(["wget", "https://sentiai.pro/input.txt"])

with open('input.txt', 'r', encoding='utf-8') as f:
  text = f.read()
print("length of the dataset in characters: ", len(text))
print(text[:1000])

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(vocab_size)

stoi = { ch:i for i,ch in enumerate(chars)}
itos = {i:ch for i,ch in enumerate(chars)}
print(itos)
encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

print(encode("hi Guys!"))
print(decode(encode("hi Guys!")))

#Encoding using NLTK 

import nltk

#text = "I like cats."
with open('input.txt', 'r', encoding='utf-8') as f:
  text = f.read()
  
tokens = nltk.word_tokenize(text)
#print(tokens)

chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
print(itos)

encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])

encoded = encode(text)
print("Encoded: ", encoded)

decoded = decode(encode(text))
#print("Decoded: ",decoded)

"""
def tokenize(text):
    tokens = ""
    for char in text:
        if char.isalpha():
            tokens += get_special_char(char)
        else:
            tokens += char
    return tokens

def get_special_char(char):
    char = char.lower()
    special_chars = {'a': '!', 'b': '#', 'c': '%', 'd': '&', 'e': '!', 'f': '#', 'g': '%', 'h': '&', 'i': '!', 'j': '#',
                     'k': '%', 'l': '&', 'm': '!', 'n': '#', 'o': '%', 'p': '&', 'q': '!', 'r': '#', 's': '%', 't': '&',
                     'u': '!', 'v': '#', 'w': '%', 'x': '&', 'y': '!', 'z': '#'}
    return special_chars[char]

# Create the original_chars dictionary outside the functions
original_chars = {v: k for k, v in special_chars.items()}

def decode(tokens):
    special_chars = {'a': '!', 'b': '#', 'c': '%', 'd': '&', 'e': '!', 'f': '#', 'g': '%', 'h': '&', 'i': '!', 'j': '#',
                     'k': '%', 'l': '&', 'm': '!', 'n': '#', 'o': '%', 'p': '&', 'q': '!', 'r': '#', 's': '%', 't': '&',
                     'u': '!', 'v': '#', 'w': '%', 'x': '&', 'y': '!', 'z': '#'}
    decoded_text = ""
    original_chars = {v: k for k, v in special_chars.items()}
    for token in tokens:
        if token.isalpha():
            decoded_text += original_chars.get(token, token)
        else:
            decoded_text += token
    return decoded_text

# Example usage:
text = "I like cats."
tokens = tokenize(text)
print("Tokenized text:", tokens)

decoded_text = decode(tokens)
print("Decoded text:", decoded_text)
