# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

train_data = pd.read_csv('train.csv')
train_attr = pd.read_csv('train_attribution.csv')
train_label_to_category = pd.read_csv('train_label_to_category.csv')

print('train data size', train_data.shape)
print('train attribution size', train_attr.shape)
print('train label to category size', train_label_to_category.shape)
print(train_data.head())
print(train_attr.head())
print(train_label_to_category.head())
