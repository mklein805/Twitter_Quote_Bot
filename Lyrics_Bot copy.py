#Some Good Old Fashioned Bot Resuscitation
#Fuck u Elon Musk

import tweepy
import random

#Twitter Authentication
auth = tweepy.OAuth1UserHandler(
   "API/Consumer Key", "API/Consumer Secret",
   "Access Token", "Access Token Secret"
)
api = tweepy.API(auth)

#Read in bot values
f = open(r'Lyrics.txt','r') #Replace with file of choice

data = f.readlines()

f.close()

#Initialize Random Parameters
random.seed()
x = random.randint(0,len(data)-2)

#Check that the last tweet was not the same value
if x == data[len(data)-1]:
    x = random.randint(0,len(data)-2)

#Call line
line = data[x]

#Appropriately format line if it has breaks
line = line.replace(r'\n','\n')
print(line)

#Push the tweet
api.update_status(status=line)

#Update reference value
data[len(data)-1] = x

fp = open(r'Lyrics.txt', 'w') #Replace with file of choice
for item in data:
    item = str(item)
    fp.write(item)
        
fp.close()

#Clean up empty space in file
result = ""
with open(r"Lyrics.txt", "r+") as file: #Replace with file of choice
    for line in file:
        if not line.isspace():
            result += line
 
    file.seek(0)  
    file.write(result)


