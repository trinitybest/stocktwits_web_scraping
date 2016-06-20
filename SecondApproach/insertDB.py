"""
Author: TH
Date: 08/06/2016
Description: Insert collected Tweets into Database 
"""
import pymssql
import yaml
import datetime

def insertTweet(Tweet):
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
							INSERT INTO dbo.StockTwits_Tweets (TweetID, DateTime, Date, Time, Body, Sentiment, Ticker, TickersInclude, UserID,ImageDummy, VideoDummy, TotalLikes, TotalReshares, Reshared, ResharedTweetID, TweetUrl, Replies, CreatedAt, UpdatedAt) \
							VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)\
						END \
						ELSE \
						BEGIN \
							UPDATE dbo.StockTwits_Tweets \
							SET TotalLikes = %s, TotalReshares = %s, Replies= %s, UpdatedAt = %s,  TickersInclude = %s, Body = %s \
							WHERE TweetID = %s \
						END \
						",(Tweet['tweet_ID'], 
							Tweet['tweet_ID'], Tweet['date_time'], Tweet['date'], Tweet['time'], Tweet['body'], 
							Tweet['sentiment'], Tweet['ticker'], Tweet['tickers_include'], Tweet['user_id'], Tweet['image_dummy'], 
							Tweet['video_dummy'], Tweet['total_likes'], Tweet['total_reshares'], Tweet['reshared'], Tweet['reshared_tweet_id'], Tweet['tweet_url'],Tweet['replies'], 
							now, now,
							Tweet['total_likes'], Tweet['total_reshares'], Tweet['replies'], now, Tweet['tickers_include'], Tweet['body'],Tweet['tweet_ID']) )
		conn.commit()
		return "success"
	except Exception as e:
		print("InsertTweet failed: ", e)
		return "fail"
def insertUser(User):
	keys = yaml.load(open('keys.yaml','r'))
	server = keys['DBserver']
	user = keys['DBuser']
	password = keys['DBpassword']
	database = 'SeekingAlpha'
	conn = pymssql.connect(server , user, password,database)
	cursor = conn.cursor()
	now = datetime.datetime.now()
	try:
		cursor.execute("IF NOT EXISTS (SELECT * FROM dbo.StockTwits_Users WHERE UserID = %s) \
						BEGIN INSERT INTO dbo.StockTwits_Users (UserID, UserName, UserPath) VALUES (%s, %s, %s) \
						END",(User['user_ID'], User['user_ID'], User['user_name'], User['user_path']) )
		conn.commit()
		return "success"
	except Exception as e:
		print("InsertUser failed: ", e)
		return "fail"
if __name__ == "__main__":
	# One tweet for example
	OneTweet = {'time': '01:52:24', 'user_id': 478980, 'reshared': 1, 'body': '$VRX $AAPL $GALE benched players talking like starters on these boards. I hate it!', 'sentiment': None, 'tickers_include': 'VRX, AAPL, GALE', 'replies': 3, 'ticker': 'AAPL', 
	'tweet_ID': 56591106, 'tweet_url': 'http://stocktwits.com/message/56591213#56591213', 'date': '2016-06-14', 'total_reshares': 0, 'link_embed': 0, 'video_dummy': 0, 
	'total_likes': 2, 'image_dummy': 1, 'date_time': 'Tue, 14 Jun 2016 01:52:24 -0000', 'reshared_tweet_id': 56591284} 
	OneUser = {'user_name': 'NlNJA', 'user_path': 'http://stocktwits.com/NlNJA', 'user_ID': 642655}
	print(insertTweet(OneTweet))
	print(insertUser(OneUser))
