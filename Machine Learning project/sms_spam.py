import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import seaborn as sns
df=pd.read_csv('spam.csv',encoding_errors='ignore')
print(df)
df.shape

#Data cleaning
# print(df.info())
df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
# print(df.sample(3))
# print(df.info())
df.rename(columns={'v1':'tar','v2':'text'},inplace=True)
print(df.sample(5)) 
#check missing values
df.isnull().sum()#no missing values
#check duplicate values
df.duplicated().sum()
df=df.drop_duplicates(keep='first')


#Exploratory Data Analysis
# print(df['tar'].value_counts())
# plt.pie(df['tar'].value_counts(),labels=['ham','spam'],autopct="%0.2f")
#print(plt.show())
#fetch no.of letters
df['no_char']=df['text'].apply(len)
#ftch no.of words
df['no_words']=df['text'].apply(lambda x:len(nltk.word_tokenize(x)))
# print(df.sample(5))
#fetch no.of sentence 
df['no_sent']=df['text'].apply(lambda x:len(nltk.sent_tokenize(x)))
# print(df.sample(5))
# print(df[['no_char','no_words','no_sent']].describe())
#descriptn of ham 
print(df[df['tar']=='ham'][['no_char','no_words','no_sent']].describe())
#descriptn of spam
print(df[df['tar']=='spam'][['no_char','no_words','no_sent']].describe())

