import pandas as pd
import csv

data=pd.read_csv('../data/anime.csv')
file=open('../data/bagofwords.txt','w')
i=0
while i<12294 :
    print(i)
    file.write(str(data['genre'][i]))
    file.write('\n')
    i=i+1