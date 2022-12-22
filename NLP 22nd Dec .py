#!/usr/bin/env python
# coding: utf-8

# In[3]:


import nltk


# In[9]:


text1 = 'The best known natural language processing tool is GPT-3, from OpenAI, which uses AI and statistics to predict the next word in a sentence based on the preceding words. NLP practitioners call tools like this “language models,” and they can be used for simple analytics tasks, such as classifying documents and analyzing the sentiment in blocks of text, as well as more advanced tasks, such as answering questions and summarizing reports. Language models are already reshaping traditional text analytics, but GPT-3 was an especially pivotal language model because, at 10x larger than any previous model upon release, it was the first large language model, which enabled it to perform even more advanced tasks like programming and solving high school–level math problems. The latest version, called InstructGPT, has been fine-tuned by humans to generate responses that are much better aligned with human values and user intentions, and Google’s latest model shows further impressive breakthroughs on language and reasoning.'


# In[10]:


#Frequency Distribution
fd = nltk.FreqDist(text1.split())
fd


# In[11]:


#Conditional Frequency Distribution
from nltk.probability import ConditionalFreqDist
cfd = ConditionalFreqDist((len(word),word) for word in text1.split())
cfd[4]


# In[13]:


pip install jieba


# In[15]:


import jieba
seg = jieba.cut("可以肯定地说，当大多数中国本地人", cut_all = True)
print(" ".join(seg))
#(Starts and looks for longest legal word in dictionary, mark there and look for space and then again look for the words)
#greedy algorithm used - forward matching algorithm
#backward matching algorithm - 


# In[16]:


sent = "Hello Swati, Become an expert in NLP"
words = nltk.word_tokenize(sent) #Splitting the words ususlaly we do sentence then word tokenize, no diff between split and wor_tokenize
print(words)


# In[17]:


texts = ["""Shreya Ghoshal (born 12 March 1984) is an Indian singer and television personality. One of the highest-paid and most well-established playback singers of Indian cinema, she has received four National Film Awards, four Kerala State Film Awards, two Tamil Nadu State Film Awards, two BFJA Awards, seven Filmfare Awards and ten Filmfare Awards South. She has recorded songs for films and albums in various Indian languages and has established herself as one of the leading playback singers of Indian cinema. """]


# In[18]:


for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        print(words)
        tagged = nltk.pos_tag(words) #tag each word in each sentence
        print(tagged)


# In[ ]:


#HomeWork - To determine freq dist and cond freq dist of any one of the presidentiala inaugural address (look for high frequency nouns used)

