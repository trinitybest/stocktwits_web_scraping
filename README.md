#StockTwits
This program uses Python to collect data from [StockTwits](http://stocktwits.com/), which is a stock discussion in the US.
This website provide an API, but they limit the amount to the latest 30 Tweets and they don't provide the self-disclosed sentiment in the public API.
##The First Approach
Instead, I use a different approach, which let Python "scroll" down the webpage using Firefox, then scrape the data and parse it.
 - scraper.py is the file that scrolls down the page.
 - collectTweets.py collects Tweets from the collected data.
 - insertDB insert the parsed Tweets into a database.
 - CreateTable.sql is the T-SQL file to create the table.
 
I'm still updating this project. If you find any bugs, please kindly raise an issue:)
The solution is not optimal yet. I'm working a more sophisticated solution.
##The Second Approach
This approach gets data by using "GET" resquest from a customized URL.
- collectStream.py gets data from URLs.
- insertDB.py inserts the parse Tweets into a database. *Please be aware that this insertDB has a different table desgin in comparison with the insertDB from the first approach*

