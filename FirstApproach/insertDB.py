"""
Author: TH
Date: 08/06/2016
Description: Insert collected Tweets into Database 
"""
import pymssql
import yaml
import datetime

def insertDB(Tweet):
	keys = yaml.load(open('keys.yaml','r'))
	server = keys['DBserver']
	user = keys['DBuser']
	password = keys['DBpassword']
	database = 'SeekingAlpha'
	conn = pymssql.connect(server , user, password,database)
	cursor = conn.cursor()
	now = datetime.datetime.now()

	try:
		cursor.execute("IF NOT EXISTS (SELECT * FROM dbo.StockTwits_Tweets WHERE TweetID = %s) \
						BEGIN \
							INSERT INTO dbo.StockTwits_Tweets (TweetID, DateTime, Date, Time, Content, Sentiment, Ticker, TickersInclude, Name, NameLink, ImageDummy, VideoDummy, NumLike, Retweet, Reshared, ResharedTweetID, TweetUrl, CreatedAt, UpdatedAt) \
							VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)\
						END \
						ELSE \
						BEGIN \
							UPDATE dbo.StockTwits_Tweets \
							SET NumLike = %s, ReTweet = %s, UpdatedAt = %s, Content = %s \
							WHERE TweetID = %s \
						END \
						",(Tweet['tweet_ID'], 
							Tweet['tweet_ID'], Tweet['date_time'], Tweet['date'], Tweet['time'], Tweet['content'], 
							Tweet['sentiment'], Tweet['ticker'], Tweet['tickers_include'], Tweet['name'], Tweet['name_link'], Tweet['image_dummy'], Tweet['video_dummy'], Tweet['like'], Tweet['retweet'], Tweet['reshared'], Tweet['reshared_tweet_id'], 
							Tweet['tweet_url'], now, now,
							Tweet['like'], Tweet['retweet'], now, Tweet['content'], Tweet['tweet_ID']) )
		conn.commit()
		return "success"
	except Exception as e:
		print("InsertDB failed: ", e)
		return "fail"


if __name__ == "__main__":
	# One tweet for example
	OneTweet = {'time': '11:07:00', 'retweet': None, 'reshared': 1, 'reshared_tweet_id': '55931790', 
	'image_dummy': 1, 'name_link': 'http://stocktwits.com/lonestar_ak', 'sentiment': None, 
	'tweet_url': 'http://stocktwits.com/lonestar_ak/message/56213055',
	'like': 0, 'ticker': 'AAPL', 'tickers_include': 'AAPL', 'video_dummy': 0, 
	'date_time': 'Jun. 8 at 11:07 AM', 'date': '2016-06-08', 'name': 'lonestar_ak', 
	'content': '$AAPL Got stopped out of this on Friday for a medium (.05% acct) loss. Should have respected the support there more', 'tweet_ID': '56213055'}
	print(insertDB(OneTweet))
