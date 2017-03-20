import os
import codecs

inputfile=codecs.open("post content.txt","r")
i=0
save_path = 'F:\work\eattreat dataforpost'
ofile=open("datapost2.txt","a")
for line in inputfile:
	content=line.split("\t")
	file=content[0]
	if i>0:
		completeName = os.path.join(save_path, str(file)+".txt")
		outputfile=codecs.open(completeName,"w")
		outputfile.write(line)
		outputfile.close()
	i=i+1
ofile.close()	