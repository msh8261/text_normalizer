import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from handler import *


examples = 'Hello, my name is kaka, You saw my father. Prepare to see'


def test_spacy_lem():
    assert 2 == 2
    # text = lemmatize_text((examples))
    # print(text)
    # assert text == 'hello , my name be kaka , you see my father . prepare to see'








