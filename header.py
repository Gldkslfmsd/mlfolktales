import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.dummy import DummyClassifier

#from data_loader import load_dataset

import pandas as pd

def load_dataset(csv_filename):
    data = pd.DataFrame.from_csv(csv_filename)
    data_x = data[data.columns[:-1]]
      # the objects without their class label
    data_y = data[data.columns[-1]]
      # the class labels for the objects

    return data_x, data_y


from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def scale_datasets(tr_X, tr_y, te_X, te_y):
    sx = MinMaxScaler()
    sx.fit(tr_X)
    tr_X = sx.transform(tr_X)
    te_X = sx.transform(te_X)
    
#    l = LabelEncoder()
#    l.fit(tr_y)
#    tr_y = l.transform(tr_y)
#    te_y = l.transform(te_y)
    
    return tr_X, tr_y, te_X, te_y



forest_feature_rank = ['king', 'told', 'fox', 'came', 'tell', 'daughter', 'man', 'go', 'cow', 'whole', 'soon', 'money',
                       'wife', 'ran', 'must', 'three', 'give', 'friend', 'said', 'mother', 'father', 'world', 'take',
                       'put', 'say', 'time', 'shall', 'good', 'got', 'went', 'palace', 'see', 'know', 'away', 'better',
                       'home', 'eyes', 'something', 'stood', 'one', 'thought', 'set', 'ah', 'house', 'hand', 'looked',
                       'old', 'saw', 'upon', 'great', 'began', 'called', 'poor', 'long', 'sat', 'thou', 'side', 'much',
                       'cock', 'son', 'done', 'took', 'eat', 'still', 'fell', 'look', 'day', 'little', 'last', 'oh',
                       'heart', 'also', 'young', 'leave', 'never', 'come', 'asked', 'days', 'morning', 'short',
                       'master', 'found', 'ready', 'whose', 'meat', 'hen', 'door', 'nothing', 'would', 'gold', 'wolf',
                       'everything', 'get', 'next', 'gave', 'yes', 'girl', 'far', 'together', 'quite', 'dear', 'bit',
                       'help', 'run', 'lord', 'well', 'behind', 'woman', 'night', 'answered', 'place', 'gone', 'word',
                       'fast', 'made', 'knew', 'happened', 'brought', 'like', 'make', 'many', 'going', 'find', 'might',
                       'think', 'could', 'field', 'beautiful', 'let', 'laid', 'taken', 'left', 'first', 'however',
                       'people', 'way', 'room', 'bed', 'every', 'caught', 'true', 'cut', 'hold', 'princess', 'full',
                       'kingdom', 'another', 'right', 'work', 'may', 'heaven', 'till', 'without', 'lived', 'kept',
                       'thus', 'husband', 'enough', 'replied', 'round', 'wood', 'cried', 'lay', 'penny', 'shoes',
                       'bride', 'back', 'wilt', 'threw', 'youth', 'heard', 'pretty', 'opened', 'ever', 'half', 'stay',
                       'peter', 'fine', 'turned', 'water', 'afraid', 'farther', 'two', 'earth', 'end', 'dead', 'dog',
                       'coming', 'lad', 'blew', 'anything', 'life', 'piece', 'sit', 'small', 'ground', 'lucky', 'god',
                       'head', 'outside', 'wanted', 'burnt', 'turn', 'sitting', 'big', 'food', 'met', 'nay', 'light',
                       'across', 'cat', 'hewed', 'art', 'corn', 'red', 'received', 'mouse', 'lies', 'stop', 'forest',
                       'brother', 'tree', 'smith', 'though', 'leaves', 'coal', 'st', 'black', 'sing', 'beer', 'boar',
                       'spring', 'eaten', 'drowned', 'brewing', 'devil', 'reason', 'covered', 'henny', 'creaking',
                       'heavenly', 'hill', 'broom', 'shoemaker', 'white', 'hew', 'tailor', 'troll', 'creak', 'mary',
                       'egg', 'edge', 'saint', 'virgin', 'pancake', 'ribbon', 'tup', 'linden']

def select_feats_by_rank(X, N, rank=forest_feature_rank):
    return X[rank[:N]]

def just_test_dataset(DATASET, classifiers, tr_X, tr_y, te_X, te_y):
    for n in classifiers:
        name, clf, *limit = n
        print(name, end=" ")
        if limit:
            l = limit[0]
            clf.fit(tr_X[:l], tr_y[:l])
        else:
            clf.fit(tr_X, tr_y)
        score = clf.score(te_X, te_y)
        print(score)

def test_dataset(DATASET, classifiers, scale=True, selectN=20):
    """DATASET: a format string like "%s_keyword_feats.csv", where %s is either train or test"""
    tr_X, tr_y = load_dataset(DATASET % "train")
    te_X, te_y = load_dataset(DATASET % "test")
    
    if selectN:
        tr_X = select_feats_by_rank(tr_X, selectN)
        te_X = select_feats_by_rank(te_X, selectN)
    
    if scale:
        tr_X, tr_y, te_X, te_y = scale_datasets(tr_X, tr_y, te_X, te_y)


    print(DATASET, "loaded")

    just_test_dataset(DATASET, classifiers, tr_X, tr_y, te_X, te_y)