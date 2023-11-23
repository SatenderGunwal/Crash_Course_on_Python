# Install wordcloud package if not available.
import wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies(file_contents):
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
            return fequencies
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dic)
    return cloud.to_array()

if __name__== "__main__":

    file_contents = "Pollution affects the quality of life more than one can imagine. It works in mysterious ways, sometimes which cannot be seen by the naked eye. However, it is very much present in the environment. For instance, you might not be able to see the natural gases present in the air, but they are still there. Similarly, the pollutants which are messing up the air and increasing the levels of carbon dioxide is very dangerous for humans. Increased level of carbon dioxide will lead to global warming. Further, the water is polluted in the name of industrial development, religious practices and more will cause a shortage of drinking water. Without water, human life is not possible. Moreover, the way waste is dumped on the land eventually ends up in the soil and turns toxic. If land pollution keeps on happening at this rate, we will not have fertile soil to grow our crops on. Therefore, serious measures must be taken to reduce pollution to the core."
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()
