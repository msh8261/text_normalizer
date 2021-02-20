import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#import pytest
import nltk
from handler import normalize_corpus, remove_stopwords, remove_special_characters
from handler import remove_accented_chars, expand_contractions, lemmatize_text 
from handler import remove_repeated_characters, simple_porter_stemming, strip_html_tags



examples = 'Hello, my name is kaka, You saw my father. Prepare to see'


def test_spacy_lem():
    text = lemmatize_text((examples))
    print(text)
    assert text == 'hello , my name be kaka , you see my father . prepare to see'








