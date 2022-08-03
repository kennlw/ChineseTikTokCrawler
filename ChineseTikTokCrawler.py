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

keywords = [
  "早上好", 
  "好看", 
  "酷", 
  "大家", 
  "特别", 
  "已经", 
  "虽然", 
  "而且", 
  "不但", 
  "无法", 
  "不定", 
  "这么", 
  "确定", 
  "人家", 
  "感觉",
  "他们",
  "我们",
  "谁想", 
  "来了", 
  "现在",
  "这是",
  "这里",
  "每个",
  "最后",
  "我被"
]
url = "https://tiktok-private1.p.rapidapi.com/search/video"
headers = {
"X-RapidAPI-Key": "451607b1e0msh25b2412730c45c8p11508djsn9676e0259193",
"X-RapidAPI-Host": "tiktok-private1.p.rapidapi.com"
}

offset = 0
count = 20
json_count = 0
user_ls = []
vid_ls = []
json_dict = {}

for keyword in keywords:

    offset = 0
    for i in range(10):


        try:
    
            querystring = {"keyword": keyword, "offset": str(offset), "count":str(count)}
            json_response = requests.request("GET", url, headers=headers, params=querystring).json()
            response = json_response["aweme_list"]
    
            for x in response:
                user_ls.append({k:x["author"][k] for k in imAuthKeys})

                vid_dict = {y:x["statistics"][y] for y in imVidKeys}
                vid_dict["desc"] = x["desc"]
                vid_ls.append(vid_dict)

        except IndexError: print("Index Error")
        except KeyError: print("Key Error")
        except requests.exceptions.RequestException as e: print("Request Error")
        except Exception as e: print("Catch-all error", e)

        offset+=count
        time.sleep(70)


df1 = pd.DataFrame(user_ls)
df2 = pd.DataFrame(vid_ls)

userData = df1.to_csv('ChineseTikTokUserData.csv', index = True)
vidData = df2.to_csv('ChineseTikTokCrawlerVidData.csv', index = True)

jsonUserDict = userData[0]
jsonVidDict = vidData[0]

with open("rawUserJson.json", 'w') as g:
    json.dump(jsonUserDict, g)
with open("rawVidJson.json", 'w') as f:
    json.dump(jsonVidDict, f)
