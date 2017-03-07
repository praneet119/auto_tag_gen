# auto_tag_gen
automated tags for articles(eattreat)
The ea.zip folder contains eattreat classes folder which has all the text files requierd.
Input files are text files containing post id,title and content.
If the article is about instagaram then all the content in h4 is taken into consideration.
If the article is recipe then only the content in first p tag is taken.
For rest of the articles all the content is taken removing the html tags
All the contractions like n't ,'re etc. are expanded into not, are, etc.
All the punctutions are replaced in the content and the content for all the articles saved into another folder naming cleaned_content
Now the content is breaked upon " " and each word is checked whether is it in stopwords set or not.
The stopwords are imported from nltk corpus and various other have been added according the analysis of words taht were not required at all.
Basic rules of grammer have been applied to each word if it ends with "s".
Now frequency of each word in particular file is calculated and tf score is calculated.After calculatinf tf scores for all the words in all the files tfidf score is counted and added to array.
the array is sorted in descending order against the value.
after this top 15 words of each file are sent to tag generator function.
the tag generator function gives first preference to quadgram,trigram,bigram and then unigram.
for a quadgram to exist as a tag both it parts should be in trigram. same for trigram and bigram.
special prefernce is given to words so they become tag if they belong to area or a resturant type or dish type.
after the tags have been generated then naive bayes classiication is called.

