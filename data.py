import json
from typing import List
import numpy as np
import re
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
import pandas as pd
import pprint


def downloadNLTK():
    nltk.download('wordnet')
    nltk.download('averaged_perception_tagger')
    nltk.download('punkt')
    nltk.download('stopwords')


def getWordnetPos():
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADVERB
    else:
        return wordnet.NOUN


class EstimatedData:
    collegeName: str
    designation: str
    name: str
    workedAt: str
    email: str
    location: str
    skills: str
    degree: str
    graduationYear: str

    def __init__(self, collegeName: str = None, designation: str = None, name: str = None, workedAt: str = None, email: str = None, location: str = None,
                 skills: str = None, degree: str = None, graduationYear: str = None):
        self.collegeName = collegeName
        self.designation = designation
        self.name = name
        self.workedAt = workedAt
        self.email = email
        self.location = location
        self.skills = skills


class ReadData:
    collegeName: str
    designation: str
    name: str
    workedAt: str
    email: str
    location: str
    skills: str
    degree: str
    graduationYear: str

    def __init__(self, collegeName: str = None, designation: str = None, name: str = None, workedAt: str = None, email: str = None, location: str = None,
                 skills: str = None, degree: str = None, graduationYear: str = None):
        self.collegeName = collegeName
        self.designation = designation
        self.name = name
        self.workedAt = workedAt
        self.email = email
        self.location = location
        self.skills = skills
        self.degree = degree
        self.graduationYear = graduationYear
