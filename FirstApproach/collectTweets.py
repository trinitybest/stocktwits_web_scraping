"""
Author:TH
Date:07/06/2016
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
from datetime import datetime, timedelta
from insertDB import insertDB
import unicodedata

def collectTweets(data, symbol): 
	soup = BeautifulSoup(data, 'html.parser')
	#sleep(2) #Asyn need to be implemented.
	baseUrl = 'http://stocktwits.com/'
	
	tweets = soup.find_all("li",{"class":"messageli"})
	print(len(tweets))

	length_tweets = len(tweets)
	print("----------------------------------------------")
	for i in range(0, length_tweets):
		if i%100 ==0:
			print("{} out of {} finished.".format(str(i), str(length_tweets)))
		try:
			id = tweets[i].find_all("div",{"class":"message-body"})[0].get('id')
			id = id.split('message_body_')[1]
			#print(id)
		except Exception as e:
			#print("Could not find id: ", e)
			continue

		try:
			userName = tweets[i].find_all("a", {"class": "username with-user-card"})[0].text
			userUrl = tweets[i].find_all("a", {"class": "username with-user-card"})[0].get("href")
			userUrl = urljoin(baseUrl, userUrl)
			#print(userName, userUrl)
		except Exception as e:
			#print("Could not find Name: ", e)
			continue
		tweetUrl = None
		try:
			tweetUrl = tweets[i].find_all("div", {"class":"message-date"})[0].find_all("a")[0].get("href")
			tweetUrl = urljoin(baseUrl, tweetUrl)
			#print(tweetUrl)
		except Exception as e:
			#print("Could not find tweetUrl: ", e)
			pass

		content = None
		try:
			content = tweets[i].find_all("div",{"class":"message-body"})[0].text # Make sure encoding is utf-8, and decode binary str to 'normal' str
			content = content.strip(' \t\n\r') # Remove white space '\t\n\r' at the end of the string (content)
			#.decode('ascii').encode('utf-8')
			#print(content)
		except Exception as e:
			#print("Could not find content: ", e)
			pass

		tickersInclude = None
		tickersInclude = {tag.strip('$') for tag in content.split() if tag.startswith('$')}
		tickersInclude = ', '.join(tickersInclude)
		#print(type(tickersInclude))
		#print("tickers: ", tickersInclude)


		sentiment = None
		try:
			sentiment = tweets[i].find_all("div",{"class":"message-body"})[0].find_all("span")[0].text
			#print(sentiment)
		except Exception as e:
			#print("Could not find sentiment: ", e)
			pass

		rawDateTime = None
		try:
			rawDateTime = tweets[i].find_all("div", {"class":"message-date"})[0].find_all("a")[0].text
			#print(rawDateTime)
		except Exception as e:
			#print("Could not find DateTime: ", e)
			pass
		#Here we are stilling only collecting from 2016. we need to collect more and check the date type from previous years
		date = datetime.strptime('2016 '+rawDateTime, '%Y %b. %d at %I:%M %p').date().strftime("%Y-%m-%d")
		time = datetime.strptime(rawDateTime, '%b. %d at %I:%M %p').time().strftime("%H:%M:%S")
		#print(date)
		#print(time)

		retweet = None
		try:
			# you need to sign in to get the number of retweets
			retweet = tweets[i].find_all("a", {"class":"retweet"})[0].find_all("span")[0].text
			if retweet == '':
				retweet = 0
			else:
				retweet = int(retweet)
			#print("retweet: ",retweet)
		except Exception as e:
			#print("Could not find retweet: ", e)
			pass

		like = None
		try:
			# you need to sign in to get the number of retweets
			like = tweets[i].find_all("a", {"class":"like"})[0].find_all("span")[0].text
			
			if like == '':
				like = 0
			else:
				like = int(like)
			#print("like: ",like)
		except Exception as e:
			#print("Could not find like: ", e)
			pass

		image = None
		try:
			image = tweets[i].find_all("div", {"class":"message-content"})[0].find_all("a", {"class":"media-type"})
			#print(image)
			if(len(image)>0):
				image = 1
			else:
				image = 0
			#print("numImg: ",image)
		except Exception as e:
			#print("Could not find img: ", e)
			pass
		video = None
		try:
			
			video = tweets[i].find_all("div", {"class":"video-preview"})
			
			if(len(video)>0):
				video = 1
			else:
				video = 0
			#print("numVideo: ",video)
		except Exception as e:
			#print("Could not find video: ", e)
			pass
		reshared = None
		try:
			reshared = tweets[i].find_all("div", {"class":"reshared-message-content"})
			#print(reshared)
			if(len(reshared)>0):
				reshared_dummy = 1
				if 'Shared message has been deleted' in reshared[0].text:
					reshared_tweet_id = -1
				try:
					reshared_tweet_id = reshared[0].find_all("div",{"class":"reshare-message clearfix default"})[0].get("data-message-id")
				except:
					pass
				try:
					reshared_tweet_id = reshared[0].find_all("div",{"class":"reshare-message clearfix default suggested"})[0].get("data-message-id")
				except:
					pass

			else:
				reshared_dummy = 0
				reshared_tweet_id = None
			#print("reshared: ",reshared_dummy, reshared_tweet_id)

		except Exception as e:
			#print("Could not find reshared: ", e)
			pass
		#print("#################################################")
	
		OneTweet = {"tweet_ID": id,
					"date_time": rawDateTime,
					"date": date, 
					"time": time,
					"content": content,
					"sentiment": sentiment,
					"ticker": symbol,
					"tickers_include": tickersInclude,
					"name": userName,
					"name_link": userUrl,
					"image_dummy": image,
					"video_dummy": video,
					"like": like,
					"retweet": retweet,
					'reshared': reshared_dummy,
					'reshared_tweet_id':reshared_tweet_id,
					'tweet_url': tweetUrl}
		if insertDB(OneTweet) != "success":
			print("Insert {} into DB failed.".format(str(id)))
if __name__ == "__main__":
	with open('result.txt', 'r', encoding='utf-8') as f:
		data = f.read()
	collectTweets(data, 'AAPL')















