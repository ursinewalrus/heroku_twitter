#!/usr/bin/env python
import redis, tweepy
creds = {'consumer_key':'fV7rp6Ci92Vetfirw10wmNRY8',
		 'consumer_secret':'HSFogQKNPjvsUW8Uq1NLbxB4ghVXWGhgP6Z8oTCVEL31td8bEs',
		 'access_token':'713176379471360007-2v3PuAHwLlLa5Qd7cAVR4oXKHF8OvO5',
		 'access_token_secret':'0YWmjauwztzBiGXrqChNSFT7cxNHjKEfnoy7g5JArTTPa'}
r = redis.Redis(host='localhost', port=6379, db=0)
auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
auth.set_access_token(creds['access_token'], creds['access_token_secret'])
api = tweepy.API(auth)