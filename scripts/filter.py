import pandas as pd
file=open('../data/bagofwords.txt','r')
chk=open('../data/genres.txt','r')
new=open('../data/bagofgenres.txt','w')
newname=open('../data/nagoftitles.txt','w')
f=pd.read_csv('../data/anime.csv')
j=0
while True :
    fa=file.readline().replace('\n','')
    if(fa==''):
        break
    fc=chk.read().split('\n')
    fc=fc[0:44]
    i=0
    while i<44 :
        if '|' in fa or 'Hentai' in fa :
            print(fa)
            newname.write(f['name'][j])
            newname.write('\n')
            new.write(str(fa))
            new.write('\n')
            break
        i=i+1
    j=j+1