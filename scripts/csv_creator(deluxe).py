import pandas
from pandas import DataFrame
file=open('../data/genre(deluxe).txt','r')
a=file.read().split('\n')

file=open('../data/name(deluxue.txt','r')
b=file.read().split('\n')
C={'name':b, 'genre':a}
df=DataFrame(C, columns=['name','genre'])
export_csv=df.to_csv(r'../data/anime(deluxe).csv',index=None, header=True)