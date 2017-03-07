#!/usr/bin/env python
def naivebayes(string_tags,global_var) :
  import sys
  import os
  import codecs
  import json
  pathname="eattreat_nlp_taggenerator/"
  path = ['Bakery&Sweets/','Snacks/','Meats/','Organics/','Other/','Drinks/','Restaurants/']
  path1 = ['Bakery&Sweets','Snacks','Meats','Organics','Other','Drinks','Restaurants']

  vocab = [{},{},{},{},{},{},{}]
  V =[]
  alltags=set()
  classoccur=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  for p in range(len(path)):
    
    for filename in os.listdir(pathname+path[p]):
      if not filename.startswith('.'):
        classoccur[p]+=1
        inputfile=codecs.open(pathname+path[p]+filename,'r')
        for line in  inputfile:
          content=line.split("\t")
          post_id=content[0]
          post_title=content[1]
          post_tags=content[2]
          tags = post_tags.split(', ')
          for t in tags:
            tt=t.split("-")
            for ttt in tt:
              if ttt not in alltags:
                alltags.add(ttt) 
              if ttt not in vocab[p]:
                vocab[p].update({ttt:1})
              else:
                vocab[p][ttt]+=1


    V.append(sum(vocab[p].values()))
  if global_var < 2:
    for alpha in range(len(vocab)):
      classdict=open("eattreat dictionary/dictionary_"+path1[alpha]+".txt","a")
  #   print vocab[alpha]
  #   print '\n\n'
      for key in vocab[alpha]:
        classdict.write(str(key)+"\t"+str(vocab[alpha][key])+"\n")

  naive = [{},{},{},{},{},{},{}]
  lenalltags=len(alltags)

  test_tags=[]

  total_tags=string_tags.split(", ")

  sum1 = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
  for k in range(len(vocab)):
    s=1.0
    for e in total_tags:
      t=e.split("-")
      for t2 in t:
        if t2 not in alltags:
          alltags.add(t2)
          lenalltags+=1
        if t2 not in vocab[k]:
          vocab[k].update({t2:1})
          V[k]+=1
        else:
          vocab[k][t2]+=1
          V[k]+=1
        naive[k].update({t2:float(float(1+vocab[k][t2])/float(lenalltags+V[k]))})
        s=s*naive[k][t2]

    beta=float(s*(classoccur[k]/sum(classoccur)))
    sum1[k]=beta
    

  inputfile.close()

  max_value = max(sum1)
  max_index = sum1.index(max_value)

  classoccur[max_index]+=1

  print path1[max_index]
  return path1[max_index]

#naivebayes()