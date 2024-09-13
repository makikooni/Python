import wikipedia
import nltk
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def fetch_text_from_wikipedia(page_title):
    try:
        page = wikipedia.page(page_title)
        return page.content 
    except wikipedia.exceptions.PageError:
        print(f"Page '{page_title}' does not exist!")
        return None 
    
    
page_title = "Cats"

text_data = fetch_text_from_wikipedia(page_title)
if text_data:
    print("\n Source text data from Wikipedia")
    print(text_data[:500])
    
    tokenized_text_data = [word_tokenize(sentence.lower()) for sentence in text_data.split('\n')]
    model = Word2Vec(sentences=tokenized_text_data, vector_size = 100,window= 5,  min_count= 1, sg=0)
    
    def find_similar_words(word):
        try:
            similar_words = model.wv.most_similar_cosmul(positive=[word])
            print(f"Words most similar to '{word}:' ")
            for word, similarity in similar_words:
                print(f"{word}:{similarity}")
        except KeyError:
            print(f"{word} is not in the vocabulary")
            
    user_input = input("\n Enter a word to find similar words:").lower()
    find_similar_words(user_input)