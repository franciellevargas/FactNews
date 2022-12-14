# -*- coding: utf-8 -*-
"""FactNews-Experiments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oadRh6KDm3sQYi0XnDEu8kbxsOEjrhp2
"""

import pandas as pd
dataset = pd.read_csv('/content/sample_data/factnews_final_noquotes.csv', encoding='latin-1')
dataset = dataset.sample(frac=1)

#renaming "class" attribute
df_dataset = dataset.rename(columns={'class': 'classe'})
df_dataset

#showing the dataset information 
df_dataset.info()
df_dataset.isnull()
print(df_dataset.shape)
df_dataset

import matplotlib.pyplot as plt
plt.figure(figsize = (10, 7)) 
x = df_dataset ['classe'] 
plt.hist(x, bins = 'auto', color = "blue") 
plt.title('Distribuição de ocorrências para cada classe')
plt.ylabel('Frequencia')
plt.xlabel('Classes (0, 1)')
plt.show()
#-----------------------------------------------------------
df_dataset ['classe'].value_counts()

#undersampling - deleting samples from the majority class
classe_0 = df_dataset [df_dataset .classe == 0]
classe_1 = df_dataset [df_dataset .classe == 1]
#classe_2 = df_dataset [df_dataset .classe == -1]


#Obtaining the less representative sample
sample_0 = classe_0.sample(n=517, replace=True)
#sample_1 = classe_2.sample(n=336, replace=True)

#Concatenating new data with LESS representativeness into the initial dataset.
dataset_undersampling = pd.concat([classe_1, sample_0])

print(dataset_undersampling['classe'].value_counts())

#Balanced class dataset
import matplotlib.pyplot as plt
plt.figure(figsize = (10, 7)) 
x = dataset_undersampling ['classe'] 
plt.hist(x, bins = 'auto', color = "blue") 
plt.title('Distribuição de ocorrências para cada classe')
plt.ylabel('Frequencia')
plt.xlabel('Classes (0, 1)')
plt.show()

dataset_undersampling ['classe'].value_counts()

!pip install ktrain
import keras
import ktrain
from ktrain import text

#bert
(x_train, y_train), (x_test, y_test), preproc = text.texts_from_df(dataset_undersampling, 
                                                                   'sentences',
                                                                   label_columns='classe',
                                                                   maxlen=64, 
                                                                   max_features=500,
                                                                   preprocess_mode='bert',
                                                                   lang='pt',
                                                                   val_pct = 0.1,
                                                                   )

#bert classifier
model = text.text_classifier('bert', (x_train, y_train) , preproc=preproc)
classifier = ktrain.get_learner(model, 
                             train_data=(x_train, y_train), 
                             val_data=(x_test, y_test),
                             batch_size=64
                             )

#Bert Classifier
classifier.fit_onecycle(0.00002,1)