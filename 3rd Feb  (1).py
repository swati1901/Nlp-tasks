#!/usr/bin/env python
# coding: utf-8

# In[11]:


#SWATIRAI_20BCE0996
#Web scraping 
#Stemming 
#Read a text 


# In[7]:


from urllib import request


# In[9]:


url = "https://www.gutenberg.org/files/98/98-0.txt"


# In[10]:


response = request.urlopen(url)


# In[12]:


raw = response.read().decode('utf8') #(Raw is a big chunk of strings)


# In[13]:


import nltk 
from nltk.tokenize import word_tokenize
tokens = word_tokenize(raw)


# In[15]:


print(tokens[:200]) #(use regex clean it, extra expression )


# In[16]:


#Explore beautiful soup 
#preprocessing - RE to clean any html tags or unnecessary tags
#pos tagging


# In[18]:


#Stemmers 
import nltk 
from nltk.stem import PorterStemmer 
porter = PorterStemmer()
porter.stem('joyous')


# In[19]:


porter.stem('cacti')


# In[20]:


porter.stem('Happiness')


# In[21]:


from nltk.stem import LancasterStemmer
porter = LancasterStemmer()
porter.stem('cacti')


# In[22]:


porter.stem('happiness')


# In[23]:



porter.stem('joyous')


# In[24]:


from nltk.stem import RegexpStemmer
porter = RegexpStemmer('i')
porter.stem('cacti')


# In[25]:


porter = RegexpStemmer('ing')
porter.stem('singing')


# In[26]:


porter = RegexpStemmer('ing$')
porter.stem('singing')


# In[31]:


from nltk.stem import SnowballStemmer
snow = SnowballStemmer('spanish')
snow.stem('mejor')


# In[43]:


from nltk.stem import LancasterStemmer
porter = LancasterStemmer()
sentence = 'A stemmer for English operating on the stem cat should identify such strings as cats, catlike, and catty. A stemming algorithm might also reduce the words fishing, fished, and fisher to the stem fish. The stem need not be a word, for example the Porter algorithm reduces, argue, argued, argues, arguing, and argus to the stem argu.'
tokenized_words=word_tokenize(sentence)
print(tokenized_words)
tokenized_sentence = []
for word in tokenized_words:
    tokenized_sentence.append(porter.stem(word))
tokenized_sentence = " ".join(tokenized_sentence)
tokenized_sentence


# In[54]:


#Lemmatization 
from nltk.stem import WordNetLemmatizer 
lemma = WordNetLemmatizer()
print(lemma.lemmatize("am",pos = "v"))


# In[47]:


lemma.lemmatize("mouse")


# In[58]:


lemma.lemmatize("best", pos="a")


# In[ ]:




