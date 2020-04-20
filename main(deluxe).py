import pandas as pd
import csv
from sklearn.metrics.pairwise import linear_kernel
import difflib

def userinput():
    print('Enter the Anime you have already watched')
    user=input()
    print("[ ]Searching ...")
    file = open('data/name(deluxue.txt')
    names=file.read().split('\n')
    ans=difflib.get_close_matches(user,names)
    return ans[0]
    
def genre_recommendations(title,num):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices],data['genre'].iloc[movie_indices]
anime=userinput()

print('[+]Search Complete.')

print('[ ]Creating Dataframe...')

data=pd.read_csv('data/anime(deluxe).csv')
from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
df=pd.DataFrame(data,columns=['name','genre'])

file=open('data/genre(deluxe).txt','r')
a=file.read().split('\n')
# print(len(a))

file=open('data/name(deluxue.txt','r')
b=file.read().split('\n')
# print(len(b))
print('[+]Dataframe Complete.')
print('[ ]Generating TFIDF matrix...')
tfidf_matrix = tf.fit_transform(a)

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
titles=data['name']
indices = pd.Series(data.index, index=data['name'])
num=6
while True:
    x,y=genre_recommendations(anime,num)
    
    print('[+]TFIDF matrix Complete.')
    print('[+]Display Output.')
    print('\n')
    
    print(anime)
    # anime='Tokyo Ghoul'
    x=x.tolist()
    y=y.tolist()
    for i in range(len(x)):
        print(str(i+1)+')')
        print('Anime :'+str(x[i]))
        print('Genre :'+str(y[i]))
        print('\n')
    print('would you like more?(y/n)')
    inp=input()
    if(inp=='y' or inp=='Y') :
        num+=5
    else:
      break