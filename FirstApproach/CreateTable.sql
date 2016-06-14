CREATE TABLE [dbo].[StockTwits_Tweets](
	[ID] [bigint] IDENTITY(1,1) NOT NULL,		--Automatic generated ID
	[TweetID] [bigint] NOT NULL PRIMARY KEY,				--Tweet ID assigned by StockTwits (ST)
	[DateTime] [nvarchar](max) NOT NULL,		--This is the original string collected
	[Date] [date] NOT NULL,
	[Time] [time](7) NOT NULL,
	[Content] [nvarchar](max) NULL,
	[Sentiment] [nvarchar](max) NULL,			--Self disclosed sentiment by users of ST
	[Ticker] [nvarchar](max) NULL,			--Ticker that we used to collect this Tweet 
	[TickersInclude] [nvarchar](max) NULL,		--All tickers inclueded in this Tweet
	[Name] [nvarchar](max) NULL,				--Name for the author
	[NameLink] [nvarchar](max) NULL,			--Link for the author
	[ImageDummy] [int] NULL,					--Dummy variable, 1 for having img, 0 for none.
	[VideoDummy] [int] NULL,					--Dummy variable, 1 for having video, 0 for none.
	[NumLike] [int] NULL,							--Number of likes
	[Retweet] [int] NULL,						--Number of ReTweets, need to login to get this
	[Reshared] [int] NULL,						--Dummy variable, 1 for having reshared Tweets, 0 for none.
	[ResharedTweetID] [bigint] NULL,			--The Tweet ID for the Tweeted being reshared.
	[TweetUrl] [varchar](max) NULL,				--Url for this Tweet
	[CreatedAt] [datetime] NULL,
	[UpdatedAt] [datetime] NULL
	)