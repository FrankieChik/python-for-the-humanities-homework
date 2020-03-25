import os

for path, dirs, files in os.walk ('/Users/hinmingfrankiechik/Desktop/text_files'):
    for file in files:
        print(os.path.join(path, file))

path = "/Users/hinmingfrankiechik/Desktop/text_files/2008"
files= os.listdir(path)
txts = []
for file in files:
    position = path+'/'+ file
    print (position)           
    with open(position, "r") as f:           
        lines = f.readlines()   
        for line in lines:
            txts.append(line)
        f.close()
print (txts)

with os.scandir('/Users/hinmingfrankiechik/Desktop/text_files') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2001') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2002') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2003') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2004') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2005') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2007') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2008') as dircontent:
    for name in dircontent:
        print(name)
with  os.scandir('/Users/hinmingfrankiechik/Desktop/text_files/2009') as dircontent:
    for name in dircontent:
        print(name)
        
with open('file','r')
