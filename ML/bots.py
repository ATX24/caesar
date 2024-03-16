#Eventual goal: To build an AI that ACTUALLY knows latin. Train a bot that can return all the details needed for a latin word. 


from re import T
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

import gensim.downloader as api
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity
import nltk 

class LatinSuperBot():
    def __init__(self, chosen_metric): 
        self.metric = chosen_metric
        self.df = pd.read_csv('datasets/wordstuff3.csv')
        self.latin_words = list(self.df['words'])
        self.descriptor_words = list(self.df['descriptions'])
        


    #Sorts two adjacent lists based on the content of one list
    #Uses a bubble sort 
    def sort_double_list(self, list1, list2):
        for i, val in enumerate(list1):
            for w, val2 in enumerate(list1): 
                if val2 < val:
                    list1[i], list1[w] = list1[w], list1[i]
                    list2[i], list2[w] = list2[w], list2[i]
        return list1, list2

    def cosine_test(self, test_word):
        nlp = spacy.load("en_core_web_md")

        #Encode latin words in the dataset
        latin_words_encoded = []
        for word in self.latin_words: 
            word_vector = nlp.vocab[word].vector
            latin_words_encoded.append(word_vector)

        #Calculate similarity between latin words and encoded test word
        similarity_list = []
        word_list = []
        test_word_encoded = nlp.vocab[test_word].vector
        for i, word in enumerate(latin_words_encoded):
            similarity_list.append(cosine_similarity([word, test_word_encoded]))
            word_list.append(self.descriptor_words[i])

        simlist2 = []
        for value in similarity_list:
            simlist2.append(value[0][0]) #Can also reshape here
        
        #Filter relevant answers
        answers = []
        for i, value in enumerate(simlist2):
            if value > 0.99:
                answers.append(word_list[i])

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

        frequency_list, final_list = self.sort_double_list(frequency_list, final_list)
        
        return frequency_list, final_list

    def levenshtein_test(self, test_word):
        similarity_list = []
        word_list = []
        for i, word in enumerate(self.latin_words):
            similarity_list.append(fuzz.ratio(word, test_word))
            word_list.append(self.descriptor_words[i])

        
        similarity_list, word_list = self.sort_double_list(similarity_list, word_list)
        return similarity_list[0:10], word_list[0:10]
    


    def run(self, test_word): 
        if self.metric == 'cosine similarity':
            return self.cosine_test(test_word)
        elif self.metric == 'levenshtein':
            return self.levenshtein_test(test_word)




