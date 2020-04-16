#!/usr/bin/env python
# coding: utf-8

# In[72]:


import re
from collections import Counter


# In[73]:


def words(document):
    return re.findall("\w+",document.lower())


# In[74]:


#Let's read the file
all_words = Counter(words(open("big.txt").read()))
#file_txt = file.readlines()



# In[75]:


all_words.most_common(10)


# In[192]:


def edit_one(word):
    "Creating all edits that are one edit away from `word`."
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i],word[i:]) for i in range(len(word)+1)]
   # print("splits : ",splits)
    deletes = [(left+right[1:]) for left,right in splits if right]
   # print("\ndeletes : " ,deletes)
    inserts = [left + c + right for left,right in splits for c in alphabets]
   # print("\n\ninserts : ",inserts)
    replaces = [left + c + right[1:] for left,right in splits if right for c in alphabets]
   # print("\n\nreplaces : ",replaces)
    transposes = [left + right[1] + right[0] + right[2:] for left,right in splits if len(right)>1]
    #print("\n\ntransposes : ",transposes)
    return set(deletes + inserts + replaces + transposes)


def edit_two(word):
    return(e2 for e1 in edit_one(word) for e2 in edit_one(e1))



def known(words):
    return(set(word for word in words if word in  all_words))


def correction_prediction(word):
    #return(known([word]) or edit_one(word) or edit_two(word) or [word])
    return (known([word]) or known(edit_one(word)) or known(edit_two(word)) or [word])


def prob(word,N=sum(all_words.values())):
    #pobability of the word : Frequency of the word/total no of words
    #print(N)  
    #print(all_words[word])
    #print(word)
    #print(all_words)
    return(all_words[word]/N)


"Print the most probable spelling correction for `word` out of all the `possible_corrections`"

def rectify(word):
    correct_word = max(correction_prediction(word),key=prob)
    #print(correct_word)
    if correct_word != word:
        return "do you mean "+ correct_word+"?"
    else:
        return word
    


