#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[ ]:


nltk.download()


# In[ ]:


from nltk.book import *


# In[ ]:


text1


# In[ ]:


texts()


# In[ ]:


text1.concordance("monstrous")


# In[ ]:


text1.similar("monstrous")


# In[ ]:


text2.common_contexts(["monstrous","very"])


# In[ ]:


text4.dispersion_plot(["citizeens","democracy","freedom","duties","America"])


# In[ ]:


import numpy


# In[ ]:


import matplotlib


# In[ ]:


text4.dispersion_plot(["citizeens","democracy","freedom","duties","America"])


# In[ ]:


len(text3)


# In[ ]:


sorted(set(text3))


# In[ ]:


len(text3) / len(set(text3))


# In[ ]:


text3.count("smote")


# In[ ]:


100 * text4.count('a') / len(text4)


# In[ ]:


def lexical_diversity(text):
       return len(text) / len(set(text))


# In[ ]:


def percentage(count, total): 
 return 100 * count / total


# In[ ]:


lexical_diversity(text3)


# In[ ]:


lexical_diversity(text5)


# In[ ]:


percentage(4, 5)


# In[ ]:


percentage(text4.count('a'), len(text4))


# In[ ]:


sent1 = ['Call', 'me', 'Ishmael', '.']


# In[ ]:


sent1


# In[ ]:


len(sent1)


# In[ ]:


lexical_diversity(sent1)


# In[ ]:


sent2


# In[ ]:


sent3


# In[ ]:


['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail'] 
['Monty', 'Python', 'and', 'the', 'Holy', 'Grail']


# In[ ]:


sent4 + sent1


# In[ ]:


sent1.append("Some")


# In[ ]:


sent1


# In[ ]:


sent1.append("Some")


# In[ ]:


sent1


# In[ ]:


sent1[0]='First'


# In[ ]:


sent1


# In[ ]:


sent1[2]='Middle'


# In[ ]:


sent1


# In[ ]:


sent1.insert(0, "Hello")


# In[ ]:


sent1


# In[ ]:


sent1.insert(7, "Biee")


# In[ ]:


sent1


# In[ ]:




