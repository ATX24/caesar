#Eventual goal: To build an AI that ACTUALLY knows latin. Train a bot that can return all the details needed for a latin word. 
#This file is just scripting, testing, building
#Will be developing a cleaner file later


from re import T
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv('wordstuff3.csv')
latin_words = list(df['words'])
corresponders = list(df['descriptions'])

import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity
import nltk 

# Load pre-trained GloVe model with spaCy
# Downlaod before loading --> python -m spacy download en_core_web_md


#Using basic simlarity as a metric - VERY basic ML model solution
def basic_test(test_word, metric):
    nlp = spacy.load("en_core_web_md")
    df = pd.read_csv('/datasets/wordstuff3.csv')

    # Sample dataset
    latin_words = list(df['words'])
    descriptor_words = list(df['descriptions'])
    latin_words_encoded = []

    for word in latin_words: 
        word_vector = nlp.vocab[word].vector
        latin_words_encoded.append(word_vector)

    similarity_list = []
    word_list = []

    test_word_encoded = nlp.vocab[word].vector


    for i, word in enumerate(latin_words_encoded):
        if metric == 'cosine similarity':
            similarity_list.append(cosine_similarity([word, test_word_encoded]))
            word_list.append(descriptor_words[i])
        elif metric == 'levenshtein':
            similarity_list.append(fuzz.ratio(latin_words[i], test_word))
            word_list.append(descriptor_words[i])


    simlist2 = []
    for value in similarity_list:
        if metric == 'cosine similarity':
            simlist2.append(value[0][0]) #Can also reshape here
        elif metric == 'levenshtein':
            simlist2.append(value)

    #Sort through values to only get relevent ones
    print(simlist2)
    answers = []
    simlist3 =[]
    for i, value in enumerate(simlist2):
        if value > 0:
            answers.append(word_list[i])
            simlist3.append(value) #kind sloppy, need to make this code cleaner later

    #When using cosine similarity, there seems to be a need to calculate frequency (due to similar similarity scores across multiple words)
    if metric == 'cosine similarity':
        #Algorithm for calculating the mode descriptors
        final_list = [] 
        frequency_list = []
        frequency = 0
        for i, value in enumerate(answers):
            if value in final_list:
                pass
            else:
                for i, value2 in enumerate(answers):
                    if value == value2:
                        frequency += 1
                final_list.append(value)
                frequency_list.append(frequency)  
                print(f'{value}  frequency = {frequency}')
            frequency = 0

        #Sort frequency list (Have to brush up on some of the APCSA Algorithms skills lol)
        #Let's use bubble sort
        for i, freq in enumerate(frequency_list):
            for w, freq2 in enumerate(frequency_list): 
                if freq2 < freq:
                    frequency_list[i], frequency_list[w] = frequency_list[w], frequency_list[i]
                    final_list[i], final_list[w] = final_list[w], final_list[i]
        print(frequency_list)
        print(final_list)

    #When using levenstein distance, we do not need to use frequency - Instead, we just need to sort the actual list of similarity values 
    elif metric == 'levenshtein':
        #Let's use bubble sort again
        for i, sim in enumerate(simlist3):
            for w, sim2 in enumerate(simlist3): 
                if sim2 < sim:
                    simlist3[i], simlist3[w] = simlist3[w], simlist3[i]
                    answers[i], answers[w] = answers[w], answers[i]
    print(simlist3[0:10])
    print(answers[0:10])
        


basic_test('continētur', 'levenshtein')

#Training a KNN model using the word embeddings

