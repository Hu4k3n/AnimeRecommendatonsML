import mechanize as mc
from bs4 import BeautifulSoup
import re
from pandas import DataFrame

def getgenre(link):
    br=mc.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    site=br.open(link)
    html=open("../data/page_anime.html",'w')
    html.write(str(site.read()))

    div=['<span'+i for i in site.get_data().decode().split('<span')][0:100]
    # file=open('div.txt','w')
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
def list_create(name,genre):
    file_name=open('../data/name(deluxue.txt','a')
    file_genre=open('../data/genre(deluxe).txt','a')
    file_name.write(str(name)+'\n')
    file_genre.write(str(genre)+'\n')
    return 
def main():
    # change the value of z each time and backup the data before running the program
    z=2
    while z<4 :
        br=mc.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        
        site=br.open('https://myanimelist.net/topanime.php?limit='+str(z*50))
        html=open("../data/page.html",'w')
        html.write(str(site.read()))
        html.close()
        site=BeautifulSoup(open('../data/page.html'),features='html5lib')
        # tbody=[]
        # i=0
        # for tag in site.find_all('tr') :
        #     tbody=tag.text.split('\\n')
        #     tbody=list(filter(None,tbody))
        #     print(tbody)
        #     print(len(tbody))
        #     print('\n')
        links=[]
        i=0
        for link in site.findAll('a',href=True):
                pipe=link['href']
                if 'https://myanimelist.net/anime/' in str(pipe) and len(pipe.split('/'))==6:
                    # print(str(pipe))
                    links.append(str(pipe))
                    
        res=[]
        [res.append(x) for x in links if x not in res]
        # print(len(res))
        links=[]
        links=res[0:50]
        print("Site Loaded")
        
        while i<50 :
            genre=getgenre(str(links[i]))
            # print(genre)
            pname=[]
            pname=links[i].split('/')
            name=pname[5].replace('_',' ')
            # print(name)
            i=i+1
            print(str(i)+' of 50\n')
            list_create(name,genre)
        z=z+1
    
    
if __name__=="__main__":
    main()