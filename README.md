
automated tags for articles(eattreat)


Data gathering : Wordpress plugin . json parsing.# plugin usage called Export To Text 2.4'
Dividing one text file into unique text files ..

PUSH CODE THAT DOES THIS AND HOW ?


DATA CLEANING :
stopwords.










The ea.zip folder contains eattreat classes folder which has all the text files requierd.
# How were the classes decided ? If a new content type is introduced will it classify ?//from the 7
 predecided...end up mostly in other #

DATA CLEANING :
//


Input files are text files containing "post id,title and content.
If the article is about instagaram then all the content in h4 is taken into consideration. #CLEANING 
If the article is recipe then only the content in first p tag is taken.
For rest of the articles all the content is taken removing the html tags....#introduces problem of rigid syntax

All the contractions like n't ,'re etc. are expanded into not, are, etc.
All the punctutions are replaced in the content and the content for all the articles saved into another folder named 

GRAMMMAR RULEEEEESSSS : [plural singular # add other rules]


STOPWORDS WHAT AREE ? MANUAL ADDITION BY ? 

//Stopwords are words which are common words which are of liitle significance and removed before further processing of text.
//Manual addition to already list by analyzing the text of the document.


# HOW IS THE FINAL CLEAN CONTENT RETRIEVED  ? DOES THE ORDER MATTER ? 
//The order does not greatly matters but should be followed.
UNICODE CHARACTERS ISSUE ###soution ....

cleaned_content


Now the content is breaked upon " " /*SPACE*/ and each word is checked whether is it in stopwords set or not. # PER

TOKENISATION 

The stopwords are imported from NLTK CORPUS and various other have been added according the analysis of words taht were not required at all. HIT AND TRIAL ADDING NEW STOPWORDS...#can we do better. =

Basic rules of grammer have been applied to each word if it ends with "s".


TFIDF  : term frequency inverse document frequency...TF/IDF 
Every term in clean data is used here..



Now frequency of each word in particular file is calculated and tf score is calculated.After calculatinf tf scores for all the words in all the files tfidf score is counted and added to array. # every  word has a TfIdF SCORE 
the array is sorted in descending order against the value. HELPS DETERMINE UNIQUENESS....

THIS IS DONE FOR ALL UNIGRAM BIGRAMS TRIGRAM # 

after this top 15 words of each file are sent to tag generator function. # HOW WAS 15 DECIDED ... OUTPUT NEEDED 6 TAGS...

the tag generator function gives first preference to quadgram,then trigram,then bigram and then unigram.

for a quadgram to exist as a tag both it parts should be in trigram. same for trigram and bigram.

special prefernce is given to words so they become tag if they belong to area or a resturant type or dish type.

after the tags have been generated then naive bayes classiication is called.

