from collections import Counter
file=open('../data/bagodwords.txt','r')
s=''
a=list(dict.fromkeys(file.read().replace('\n',',').split(',')))
file_write=open('../data/genres.txt','w')
i=0
while i<len(a) :
    a[i]=a[i].strip()
    i=i+1
a=list(dict.fromkeys(a))
i=0   
while i<len(a) :
    file_write.write(a[i].strip())
    file_write.write('\n')
    i=i+1