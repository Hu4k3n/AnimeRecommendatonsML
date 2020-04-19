import difflib

user=input()
file = open('../data/nagoftitles.txt')
names=file.read().split('\n')
ans=difflib.get_close_matches(user,names)
print (ans[0])