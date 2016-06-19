"""
Author:TH
Date:14/06/2016
"""

import requests
import json
from datetime import datetime
from urllib.parse import urljoin
from insertDB import insertTweet, insertUser
BASE_URL = 'http://stocktwits.com'

def get_json(max, stream_id):
	resp = None
	headers = {'Cookie':'__cfduid=d1e431e23a5217624072aa1c9cf1e76001465112923; signup_id=63334172; quotes_port=0; em_cdn_uid=t%3D1465112924602%26u%3D3350a27304944692af074640c1b09014; timezone=-720; __qca=P0-1645324571-1465112925487; bm_monthly_unique=true; stream_crumb_id=de369480-0d1f-0134-dfdf-525400ae6770; 767264active-platform=1; user_segment=Prospect; has_logged_in=true; session_visits_count=16; bm_daily_unique=true; bm_sample_frequency=1; __utmt=1; mp_mixpanel__c=6; mp_mixpanel__c3=6659; mp_mixpanel__c4=6051; mp_mixpanel__c5=39; session_visit_counted=true; amplitude_idstocktwits.com=eyJkZXZpY2VJZCI6IjM2YjY2OWVkLTJjZTktNDQ0MC04MjUwLWQwYmRmOTBkY2E2YyIsInVzZXJJZCI6Ijc2NzI2NCIsIm9wdE91dCI6ZmFsc2V9; mp_108975b2f0dfaa5464d158413babf48a_mixpanel=%7B%22distinct_id%22%3A%20%221551f89164864f-0d14597cb34fda-36667f02-13c680-1551f891649479%22%2C%22First%20Landing%20Page%22%3A%20%22%2F%22%2C%22First%20Source%22%3A%20%22https%3A%2F%2Fwww.google.co.nz%2F%22%2C%22First%20Visit%20Date%22%3A%20%222016-06-05T07%3A48%3A43%2B00%3A00%22%2C%22User%20Type%22%3A%20%22unauthenticated%22%2C%22Number%20of%20Visits%22%3A%2016%2C%22Landing%20Page%22%3A%20%22%2Fsignedout%22%2C%22Source%22%3A%20%22http%3A%2F%2Fstocktwits.com%2Fhome%22%2C%22Platform%22%3A%20%22web%22%2C%22Last%20Visit%20Date%22%3A%20%222016-06-13T19%3A55%3A43-07%3A00%22%2C%22Search%20Bucket%22%3A%20%22null%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.co.nz%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.co.nz%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpap%22%3A%20%5B%5D%2C%22__alias%22%3A%20%22767264%22%2C%22mp_name_tag%22%3A%20%22DeanHu%22%2C%22User%20Follows%22%3A%2062%2C%22Stock%20Follows%22%3A%200%2C%22Messages%20Sent%22%3A%201%2C%22Full%20Name%22%3A%20%22Dean%20Hu%22%2C%22Signup%20Date%22%3A%20%222016-06-06T05%3A18%3A38%2B00%3A00%22%2C%22Email%20Address%22%3A%20%22hutianyou6%40gmail.com%22%2C%22visitorID%22%3A%20%22767264%22%2C%22Username%22%3A%20%22DeanHu%22%2C%22signupFlowTest1%22%3A%20%22interests%22%7D; bm_last_load_status=BLOCKING; _stwts=BAh7C0kiD3Nlc3Npb25faWQGOgZFVEkiJTNhZTY4NTlkZjU5ZTM4YzAyOWNjYTEwYWU0YmI4ZjViBjsAVEkiFGFuYWx5dGljc19xdWV1ZQY7AEZbAEkiEF9jc3JmX3Rva2VuBjsARkkiMTFWdmlXb3ZkeDRhbGF1MXdyQmxaVjU2WnRLeXovUExOYm9yajgxcGpGTzA9BjsARkkiH2luY29taW5nX3NvY2lhbF9jb25uZWN0aW9uBjsARkkiDFR3aXR0ZXIGOwBUSSIOcmV0dXJuX3RvBjsARiIYL3N5bWJvbC9BQVBMP3E9YWFwbEkiCmZsYXNoBjsAVG86JUFjdGlvbkRpc3BhdGNoOjpGbGFzaDo6Rmxhc2hIYXNoCToKQHVzZWRvOghTZXQGOgpAaGFzaH0GOgx3YXJuaW5nVEY6DEBjbG9zZWRGOg1AZmxhc2hlc3sGOwpJIi5Zb3UgbXVzdCBiZSBzaWduZWQgaW4gdG8gYWNjZXNzIHRoaXMgcGFnZQY7AFQ6CUBub3cw--ce06e1c14b77a270fc42b7faca524cf09b6e876e; __utma=62941037.1127145370.1465112926.1465635259.1465871967.16; __utmb=62941037.15.9.1465872955257; __utmc=62941037; __utmz=62941037.1465112926.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=62941037.|2=Start%20Date=20160605=1',
	'X-NewRelic-ID':'VwEPUV5ACQEHXFBS',
	'Accept-Encoding':'gzip, deflate, sdch',
	'X-CSRF-Token':'1VviWovdx4alau1wrBlZV56ZtKyz/PLNborj81pjFO0=',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
	'Accept':'application/json, text/javascript, */*; q=0.01',
	'Referer':'http://stocktwits.com/symbol/AAPL?q=aapl',
	'X-Requested-With':'XMLHttpRequest',
	'Connection':'keep-alive'}
	#r = requests.get('http://stocktwits.com/streams/poll?stream=symbol&max=56591341&stream_id=686&substream=top&item_id=686', headers = headers)
	#print(r.text)

	resp = None
	for i in range(4):
		try:
			resp = requests.get('http://stocktwits.com/streams/poll?stream=symbol&max='+max+'&stream_id='+stream_id+'&substream=top&item_id='+stream_id, headers = headers, timeout=5)
		except Exception as e:
			print("Time Out: ", e)
			with open("TimeOut.txt", "a") as f1:
				f1.write('http://stocktwits.com/streams/poll?stream=symbol&max='+max+'&stream_id='+stream_id+'&substream=top&item_id='+stream_id+'\n')
			#log.error('GET Timeout to {} w/ {}'.format(url[len(ST_BASE_URL):], trimmed_params))
		if resp is not None:
			break
	if resp is None:
		#log.error('GET loop Timeout')
		return None
	else:
		return json.loads(resp.content.decode()) # Decode binary str to normal str.

def get_features(json_param, ticker):
	if json_param == None:
		print('No JSON loaded.')
	else:
		reshared = 0
		reshare_id = None
		image = 0
		video = 0
		in_reply_to_message_id = None
		link_embed = 0
		embedUrl = None
		sentiment = None
		tweetUrl = None
		replies = 0
		for k, v in json_param.items():
			if k == 'messages': # Find the messages with 'messages' as the key
				print('number of messages: ', len(v)) # v is a list
				#print(v[1])
				for message_count in range(0,len(v)): # We will have 30 messages here by default. More details available at http://stocktwits.com/developers/docs/api#streams-symbol-docs
				#for message_count in range(0,1):
					#print(message_count)
					try:
						for key, value in v[message_count].items():
							if key == 'id':
								id = value
								#print(id)
							elif  key == 'created_at':
								dateTime = value
								date = datetime.strptime(dateTime, '%a, %d %b %Y %H:%M:%S %z').date().strftime("%Y-%m-%d")
								time = datetime.strptime(dateTime, '%a, %d %b %Y %H:%M:%S %z').time().strftime("%H:%M:%S")
								body = value.strip()
								tickersInclude = {tag.strip('$') for tag in body.split() if tag.startswith('$')}
								tickersInclude = ', '.join(tickersInclude)
								#print(body)
								#print(tickersInclude)
							elif key == 'user':
								for user_key, user_value in value.items():
									if user_key == 'id':
										userID = user_value
										#print(userID)
									elif user_key == 'username':
										userName = user_value
										#print(userName)
							elif key == 'total_likes':
								totalLikes = value 
								#print(totalLikes)
							elif key == 'total_reshares':
								totalReshares = value
								#print(totalReshares)
							elif key == 'reshare_message':
								reshared = 1
								#print(value)
								for reshare_key, reshare_value in value.items():
									if reshare_key == 'message':
										for reshare_msg_key, reshare_msg_value in reshare_value.items():
											if reshare_msg_key == 'id':
												reshare_id = reshare_msg_value
												#print('reshare_id: ',reshare_id)
							elif key == 'conversation':
								for con_key, con_value in value.items():
									if con_key == 'path':
										tweetUrl = urljoin(BASE_URL, con_value)
										#print('tweetUrl: ',tweetUrl)
									elif con_key == 'replies':
										replies = con_value
										#print('replies: ', replies)
							elif key == 'sentiment':
								#print(value)
								#print(type(value))
								if type(value) is dict:
									for sentiment_key, sentiment_value in value.items():
										if sentiment_key == 'name':
											sentiment = sentiment_value
								else:
									sentiment = value

								#print("Sentiment: ",sentiment)
							elif key == 'view_chart':
								image = 1
							elif key == 'in_reply_to_message_id':
								in_reply_to_message_id = value
							elif key == 'user_path':
								userPath = urljoin(BASE_URL, value)
								#print(userPath)
							elif key == 'link_embed':
								link_embed = 1
								for embed_key, embed_value in value.items():
									if embed_key == 'video_url':
										if embed_value == 'None':
											video = 0
										else:
											video = 1
								#print('video: ',video)
						Tweet = {"tweet_ID": id,
								"date_time": dateTime,
								"date": date, 
								"time": time,
								"body": body,
								"sentiment": sentiment,
								"ticker": ticker,
								"tickers_include": tickersInclude,
								"user_id": int(userID),
								"image_dummy": image,
								"video_dummy": video,
								"total_likes": int(totalLikes),
								"total_reshares": int(totalReshares),
								'reshared': reshared,
								'reshared_tweet_id':reshare_id,
								'tweet_url': tweetUrl,
								'replies': int(replies),
								'link_embed': link_embed}
						User = {"user_ID":int(userID),
								"user_name": userName,
								"user_path": userPath}
						#print(Tweet, User)
						#print(message_count)
						#print(Tweet)
						if insertTweet(Tweet)!= 'success':
							with open("insertTweetError.txt", "a") as f2:
								f2.write(id + '\n')
						if insertUser(User)!='success':
							with open("insertUserError.txt", "a") as f3:
								f3.write(userID + '\n')
					except Exception as e:
						print(e)
			elif k == 'max':
				max = v
		return max
					#f.write("\n ############################### \n")
		
		print(max)
if __name__ == "__main__":
	#with open("features.txt", "a") as f:
		#f.write(str(get_json()))
	#json = get_json('56670305', '686')
	#max = get_features(json, 'AAPL')
	tickerGroup = [('AAPL', '686'), ('GOOG', '2044'), ('GOOGL', '11938'),('MSFT', '2735'), ('BRK.A', '4586'), ('BRK.B', '8132'), ('XOM', '7825'), ('FB', '7871'), 
	('JNJ', '6011'), ('GE','5481'), ('AMZN', '864'), ('WFC', '7718')]
	#print(tickerGroup[0][1])
	#56670305
	for i in range(0, len(tickerGroup)):
		#max = 56670305
		max = 55098250
		for j in range(0, 1000):
			#print(i)
			print(j,tickerGroup[i][0], max)
			jsonFile = get_json(str(max), tickerGroup[i][1])
			max = get_features(jsonFile, tickerGroup[i][0])
	








