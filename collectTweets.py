"""
Author:TH
Date:07/06/2016
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import codecs
from time import sleep
from multiprocessing.pool import ThreadPool

def collectTweets(data): 

	soup = BeautifulSoup(data, 'html.parser')
	#sleep(2) #Asyn need to be implemented.
	baseUrl = 'http://stocktwits.com/'
	
	tweets = soup.find_all("li",{"class":"messageli"})
	print(len(tweets))
	#print(tweets[25])
	#for i in range(0, len(tweets)):
	for i in range(0, 1):
		#print(i)
		#print(tweets[i])
		try:
			id = tweets[i].find_all("div",{"class":"message-body"})[0].get('id')
			id = id.split('message_body_')[1]
			print(id)
		except Exception as e:
			print("Could not find id: ", e)
			continue

		try:
			userName = tweets[i].find_all("a", {"class": "username with-user-card"})[0].text
			userUrl = tweets[i].find_all("a", {"class": "username with-user-card"})[0].get("href")
			userUrl = urljoin(baseUrl, userUrl)
			print(userName, userUrl)
		except Exception as e:
			print("Could not find Name: ", e)
			continue

		try:
			tweetUrl = tweets[i].find_all("div", {"class":"message-date"})[0].find_all("a")[0].get("href")
			tweetUrl = urljoin(baseUrl, tweetUrl)
			print(tweetUrl)
		except Exception as e:
			print("Could not find tweetUrl: ", e)


		try:
			content = tweets[i].find_all("div",{"class":"message-body"})[0].text
			print(content)
		except Exception as e:
			print("Could not find content: ", e)

		try:
			sentiment = tweets[i].find_all("div",{"class":"message-body"})[0].find_all("span")[0].text
			print(sentiment)
		except Exception as e:
			print("Could not find sentiment: ", e)

		try:
			rawDateTime = tweets[i].find_all("div", {"class":"message-date"})[0].find_all("a")[0].text
			print(rawDateTime)
		except Exception as e:
			print("Could not find DateTime: ", e)

		try:
			# you need to sign in to get the number of retweets
			retweet = tweets[i].find_all("a", {"class":"retweet"})[0].find_all("span")[0].text
			print("retweet: ",retweet)
		except Exception as e:
			print("Could not find retweet: ", e)

		try:
			# you need to sign in to get the number of retweets
			like = tweets[i].find_all("a", {"class":"like"})[0].find_all("span")[0].text
			print("like: ",like)
		except Exception as e:
			print("Could not find like: ", e)

		try:
			# you need to sign in to get the number of retweets
			image = tweets[i].find_all("div", {"class":"message-content"})[0].find_all("a", {"class":"media-type"})
			#print(image)
			if(len(image)>0):
				numImg = 1
			else:
				numImg = 0
			print("numImg: ",numImg)
		except Exception as e:
			print("Could not find img: ", e)

		
		try:
			reshared = tweets[i].find_all("div", {"class":"reshared-message-content"})
			if(len(reshared)>0):
				reshared_dummy = 1
				reshared_message_id = reshared[0].find_all("div",{"class":"reshare-message clearfix default"})[0].get("data-message-id")
			else:
				reshared_dummy = 0
				reshared_message_id = None
			print("reshared: ",reshared_dummy, reshared_message_id)

		except Exception as e:
			print("Could not find reshared: ", e)

		print("#######################")
	
	"""
	try:
		title = soup.find_all("h1", {"itemprop":"headline"})[0].text
	except:
		print("Could not get title: ",url)
		return "Could not get title: "+url
	###print("title: ", title)
	dateTime = soup.find_all("time", {"itemprop":"datePublished"})[0]
	time1 = dateTime.get("content")
	time2 = dateTime.text
	date = dateTime.get("content").split('T')[0]
	time = dateTime.get("content").split('T')[1].split('Z')[0]
	"""

	"""
	tickersAbout = []
	companiesAbout = soup.find_all("a", {"sasource":"article_primary_about"})
	for companyAbout in companiesAbout:
		if "(" in companyAbout.text:
			tickersAbout.append(companyAbout.text.split("(")[1].split(")")[0])
		else:
			tickersAbout.append(companyAbout.text)
	#print("Tickers About are: {0}".format(', '.join(tickersAbout)))
	tickersAboutStr = ', '.join(tickersAbout)

	tickersIncludes = []
	companiesIncludes = soup.find_all("a", {"sasource":"article_about"})
	for companyIncludes in companiesIncludes:
	    tickersIncludes.append(companyIncludes.text)
	###print("Tickers Includes are: {0}".format(', '.join(tickersIncludes)))
	tickersIncludesStr = ', '.join(tickersIncludes)

	author = soup.find_all("a",{"class":"name-link", "sasource":"auth_header_name"})
	authorUrl = author[0].get("href")
	authorName = author[0].contents[0].text
	###print("Name is: {0}, {1}".format(authorUrl, authorName))

	bio = soup.find_all("div", {"class":"bio hidden-print"})[0].text
	###print("Bio is: {0} ".format(bio))

	summary = []
	try:
		summaryByParagraphes = soup.find_all("div", {"class":"a-sum", "itemprop":"description"})[0].find_all("p")
		#print(summaryByParagraphes)
		for p in summaryByParagraphes:
		    summary.append(p.text);
		###print("Summary: ",' '.join(summary))
	except Exception as e:
		print(', No Summary ', url)
	summaryStr = ' '.join(summary)

	image = soup.find_all("span", {"class":"image-overlay"})
	if len(image) > 0:
	    imageDummy = 1
	else:
	    imageDummy = 0
	###print("ImageDummy: ",imageDummy)
	
	bodyAll = soup.find_all("div", {"id":"a-body"})[0]
	body = bodyAll.find_all("p")
	bodyContent = ''
	for p in body:
	    bodyContent += (p.text+' ')
	bodyContent = bodyContent.split("Disclosure")[0]
	bodyAll = bodyAll.text
	#print(bodyAll)
	

	try:
		disclosure = soup.find_all("p", {"id":"a-disclosure"})[0].find_all("span")[0].text
		###print("Disclosure: ", disclosure)
	except:
		try:
			disclosure = bodyAll.split("Disclosure:")[1]
		except:
			print(', No Disclosure ', url )
			disclosure = ''
	#print(disclosure)
	# New way of collecting disclosure.
	try:
		articleNumber = int(url.split('article/')[1].split("-")[0])
	except:
		print("No article number.")
	#print(articleNumber)
	return {"title": title,
			"date": date,
			"time": time, 
			"tickersAbout": tickersAboutStr,
			"tickersIncludes": tickersIncludesStr,
			"name": authorName,
			"nameLink": authorUrl,
			"bio": bio,
			"summary": summaryStr,
			"bodyContent": bodyContent,
			"imageDummy": imageDummy,
			"disclosure": disclosure,
			"bodyAll": bodyAll,
			"articleNumber": articleNumber,
			'articleUrl2': url}
	"""
if __name__ == "__main__":
	with open('result.txt', 'r') as f:
		data = f.read()
	collectTweets(data)















