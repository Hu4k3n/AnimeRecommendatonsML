import mechanize as mc
from bs4 import BeautifulSoup
import re

def getgenre(link):
    br=mc.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    site=br.open(link)
    html=open("../data/page_anime.html",'w')
    html.write(str(site.read()))

    div=div=['<span'+i for i in site.get_data().decode().split('<span')][0:100]
    file=open('div.txt','w')
    i=0
    while i<100:
        if 'Genres:' in str(div[i]):
            start=i
            break
        i=i+1
    while i<100:
        if 'Duration:' in str(div[i]):
            end=i-1
            break
        i=i+1
    genre=''
    i=start+1
    while i<=end :
        site=BeautifulSoup(div[i],features='html5lib')
        x=site.get_text()
        x=x[0:int((len(x)+1)/2)-3]
        
        genre=str(genre+' | '+x)
        i=i+1
    genre=genre[3:len(genre)]
    return genre
    # html.close()
    # site=BeautifulSoup(open('../data/page_anime.html'),features='html5lib')
    # file=open('../data/finding.txt','w')
    # div=[]
    # i=0
    # for tag in site.find_all('div') :
    #     div=tag.text.split('\n')
    #     div=list(filter(None,div))
    #     print("-------------------------------")
    #     print(i)
    #     print("-------------------------------")
    #     print(len(div))
    #     # file.write(tag.text)
    #     break
    #     # print(len(tbody))
    
        
print(getgenre('https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood'))
print(getgenre('https://myanimelist.net/anime/263/Hajime_no_Ippo'))
print(getgenre('https://myanimelist.net/anime/15417/Gintama__Enchousen'))
