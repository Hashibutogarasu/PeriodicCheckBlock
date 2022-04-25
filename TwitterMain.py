import os
import time
import tweepy
from dotenv import load_dotenv
from suspicious_word import supcious_match
from threading import Event

#.envファイルを読み込み
load_dotenv()

#Twitter APIの認証
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class twmain:
    def BlockerStart():
        global api
        print("ブロック処理を開始します ctrl+cで中断")
        while(True):
            followers = api.get_followers()
            for follower in followers:
                if(supcious_match(follower.name) and supcious_match(follower.description)):
                    api.create_block(screen_name=follower.screen_name)
                    print(f"ブロックしました:{follower.name}")

            print("15分後に再びチェックします")
            time.sleep(900)