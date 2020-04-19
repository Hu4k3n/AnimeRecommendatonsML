import pandas
from pandas import DataFrame
file=open('bagofgenres.txt','r')
a=file.read().split('\n')

file=open('nagoftitles.txt','r')
b=file.read().split('\n')
C={'name':b, 'genre':a}
df=DataFrame(C, columns=['name','genre'])
export_csv=df.to_csv(r'../data/new_anime.csv',index=None, header=True)