# coding: utf-8
import praw
import json
import time
import requests

callText = "!gaumutra"

url = "https://api.pushshift.io/reddit/search/comment/?q="+callText
subreddits = ["bakchodi", "nepal", "india", "indiaspeaks", "ioe", "chutyapa"]
RepTxt = "**बंधू /u/{}, you have been blessed with पवित्र [gaumutra 🍶](https://i.imgur.com/1LZfLRq.jpg) from [गौमातृ 🐄](https://i.imgur.com/SB97oql.jpg)**\n\n卐 requested by /u/{}"

reddit = praw.Reddit(username = os.environ["username"],
                     password = os.environ["password"],
                    client_id = os.environ["client_id"],
                    client_secret = os.environ["client_secret"],
                    user_agent = "GauMatri by /u/Gaumatri")
print("Authorized: ", reddit.user.me())

def function(before, after):
    data = requests.get(url).text

    for _ in range(25):
        tmp_data = json.loads(data)["data"][_]
        time_uploaded = now = tmp_data["created_utc"]

        if time_uploaded>=before and time_uploaded<after:
            if callText in tmp_data["body"].lower():
                if tmp_data["subreddit"].lower() in subreddits:

                    # Gifter and Gifted
                    son = tmp_data["author"]
                    father = reddit.comment(tmp_data["id"]).parent().author.name
                    tmp_RepTxt = RepTxt.format(father, son)
                    
                    print(tmp_data["body"], end="\n")                    
                    submission = reddit.comment(tmp_data["id"])
                    submission.reply(tmp_RepTxt)   

        else:
            break
            
while True:
    data = int(time.time())
    after = data - data%30
    before = after - 30
    time_uploaded = (before+ after)/2
    
    if (data - after)>=0 and (data - after)<5:
        function(before, after)
        time.sleep(5)
    else:
        time.sleep(5)    
