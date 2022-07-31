import requests
import pandas as pd
import time
import json

imAuthKeys = [
  "account_region",
  "aweme_count",
  "follower_count",
  "following_count",
  "google_account",
  "has_email",
  "has_facebook_token",
  "has_twitter_token",
  "has_youtube_token",
  "language",
  "name_field",
  "nickname",
  "region",
  "sec_uid",
  "signature",
  "twitter_id",
  "twitter_name",
  "uid",
  "unique_id",
  "youtube_channel_id",
  "youtube_channel_title"
]

imVidKeys = [
  "comment_count",
  "download_count",
  "play_count",
  "share_count",
  "forward_count",
  "whatsapp_share_count"
]
url = "https://tiktok-private1.p.rapidapi.com/search/video"


# Insert key here
headers = {
"X-RapidAPI-Key": "451607b1e0msh25b2412730c45c8p11508djsn9676e0259193",
"X-RapidAPI-Host": "tiktok-private1.p.rapidapi.com"
}

offset = 0
count = 1
jsonCount = 0
user_ls = []
vid_ls = []
jsonDict = {}

for i in range(101):
  kw_ls = ["早上好，好看，酷，大家，特别，已经，虽然，而且，不但，无法"]
  def keyword():
    if 0 <= count <= 100:
      return(kw_ls[0])
    if 101 <= count <= 200:
      return(kw_ls[1])
    if 201 <= count <= 300:
      return(kw_ls[2])
    if 301 <= count <= 400:
      return(kw_ls[3])
    if 401 <= count <= 500:
      return(kw_ls[4])
    if 501 <= count <= 600:
      return(kw_ls[5])
    if 601 <= count <= 700:
      return(kw_ls[6]) 

  try:
    
    querystring = {"keyword": str(keyword()), "offset": str(offset), "count":str(count)}
    jsonResponse = requests.request("GET", url, headers=headers, params=querystring).json()
    response = jsonResponse["aweme_list"]
    
    for x in response:
      user_ls.append({k:x["author"][k] for k in imAuthKeys})
      vid_ls.append({y:x["statistics"][y] for y in imVidKeys})
    
    vid_dict = vid_ls[i]
    vid_dict["desc"] = x["desc"]

    jsonDict[str(jsonCount)] = jsonResponse
    jsonCount+=1

  
  except IndexError: print("Index Error")
  except KeyError: print("Key Error")

  offset+=count
  time.sleep(2)


df1 = pd.DataFrame(user_ls)
df2 = pd.DataFrame(vid_ls)

userData = df1.to_csv('ChineseTikTokUserData.csv', index = True)
vidData = df2.to_csv('ChineseTikTokCrawlerVidData.csv', index = True)

with open("rawJson.json", 'w') as f:
    json.dump(jsonDict, f)
