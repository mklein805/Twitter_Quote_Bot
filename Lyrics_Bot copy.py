#Some Good Old Fashioned Bot Resuscitation
#Fuck u Elon Musk

import tweepy
import random

auth = tweepy.OAuth1UserHandler(
   "API/Consumer Key", "API/Consumer Secret",
   "Access Token", "Access Token Secret"
)
api = tweepy.API(auth)

f = open(r'Lyrics.txt','r') #Replace with file of choice

data = f.readlines()

f.close()

random.seed()
x = random.randint(0,len(data)-2)

if x == data[len(data)-1]:
    x = random.randint(0,len(data)-2)
   
line = data[x]

line = line.replace(r'\n','\n')
print(line)


api.update_status(status=line)

data[len(data)-1] = x

fp = open(r'Lyrics.txt', 'w') #Replace with file of choice
for item in data:
    item = str(item)
    fp.write(item)
        
fp.close()

result = ""
with open(r"Lyrics.txt", "r+") as file: #Replace with file of choice
    for line in file:
        if not line.isspace():
            result += line
 
    file.seek(0)  
    file.write(result)


