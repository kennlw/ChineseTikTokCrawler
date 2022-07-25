import requests
import pandas as pd
import time

imKeys = [
  "account_region",
  "aweme_count",
  "birthday",
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
  "secret",
  "signature",
  "twitter_id",
  "twitter_name",
  "uid",
  "unique_id",
  "youtube_channel_id",
  "youtube_channel_title"
]

url = "https://tiktok-private1.p.rapidapi.com/search/video"


# Insert key here
headers = {
"X-RapidAPI-Key": "__",
"X-RapidAPI-Host": "tiktok-private1.p.rapidapi.com"
}

offset = 0
count = 3
infols = []

for i in range(20):
  
	try:
    
		querystring = {"keyword": "北京", "offset": str(offset), "count":str(count)}
		response = requests.request("GET", url, headers=headers, params=querystring).json()["aweme_list"]
    
		for x in response:
			infols.append({k:x["author"][k] for k in imKeys})

	except TypeError: print("Type Error")
	except IndexError: print("Index Error")
	except KeyError: print("Key Error")

	offset+=count
	time.sleep(2)

df = pd.DataFrame(infols)
csvData = df.to_csv('ChineseTikTokUserData.csv', index=True)


