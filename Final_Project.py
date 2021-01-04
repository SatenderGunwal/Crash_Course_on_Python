#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud

# For this project, you'll create a "word cloud" from a text by writing a script.  This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words.  A dictionary is the output of the `calculate_frequencies` function.  The `wordcloud` module will then generate the image from your dictionary.

# For the input text of your script, you will need to provide a file that contains text only.  For the text itself, you can copy and paste the contents of a website you like.  Or you can use a site like [Project Gutenberg](https://www.gutenberg.org/) to find books that are available online.  You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.
# <br><br>
# 

# In[29]:


import wordcloud
from matplotlib import pyplot as plt


# In[30]:


file_contents = "Pollution affects the quality of life more than one can imagine. It works in mysterious ways, sometimes which cannot be seen by the naked eye. However, it is very much present in the environment. For instance, you might not be able to see the natural gases present in the air, but they are still there. Similarly, the pollutants which are messing up the air and increasing the levels of carbon dioxide is very dangerous for humans. Increased level of carbon dioxide will lead to global warming. Further, the water is polluted in the name of industrial development, religious practices and more will cause a shortage of drinking water. Without water, human life is not possible. Moreover, the way waste is dumped on the land eventually ends up in the soil and turns toxic. If land pollution keeps on happening at this rate, we will not have fertile soil to grow our crops on. Therefore, serious measures must be taken to reduce pollution to the core."


# Write a function in the cell below that iterates through the words in *file_contents*, removes punctuation, and counts the frequency of each word.  Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the".  Then use it in the `generate_from_frequencies` function to generate your very own word cloud!
# <br><br>
# **Hint:** Try storing the results of your iteration in a dictionary before passing them into wordcloud via the `generate_from_frequencies` function.

# In[31]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the","this","than", "a","on","in","up","for","For", "to", "if","If", "is", "it","It", "of", "and", "or", "an", "as", "i", "me", "my",     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom","must", "this", "that", "am", "are", "was", "were", "be", "been", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some","on.", "such", "no","not", "nor", "too", "very", "can", "will", "just"]
    list1 = file_contents.split()
    list2 = []
    for word in list1:
        for i in range(len(word)):
            if word[i] in punctuations:
                word = word[:i]+word[i+1:]
        if word not in uninteresting_words:
            list2.append(word)
    dic = {}
    n = 0
    for word in list2:
        for i in range(len(list2)):
            if word == list2[i]:
                n += 1
        dic[word] = n
        n=0
    class WordCloud:   
        def generate_from_frequencies(dic):
            fequencies = dic.values()
            return frequencies
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dic)
    return cloud.to_array()


# If you have done everything correctly, your word cloud image should appear after running the cell below.  Fingers crossed!

# In[32]:


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# In[ ]:




