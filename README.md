# auto_tag_gen
automated tags for articles(eattreat)

Input files are text files containing post id,title and content.
If the article is about instagaram then all the content in h4 is taken into consideration.
If the article is recipe then only the content in first p tag is taken.
For rest of the articles all the content is taken removing the html tags
All the contractions like n't ,'re etc. are expanded into not, are, etc.
All the punctutions are replaced in the content and the content for all the articles saved into another folder naming cleaned_content
Now the content is breaked upon " " and each word is checked whether is it in stopwords set or not.
The stopwords are imported from nltk corpus and various other have been added according the analysis of words taht were not required at all.
Basic rules of grammer have been applied to each word if it ends with "s"

