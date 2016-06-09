#StockTwits
This program uses Python to collect data from StockTwits [http://stocktwits.com/], which is a stock discussion in the US.
This website provide an API, but they limit the amount to the latest 30 Tweets and they don't provide the self-disclosed sentiment in the public API.
Instead, I use a different approach, which let Python "scroll" down the webpage using Firefox and then scrape the data and parse it.
 - scraper.py is the file that scrolls down the page.
 - collectTweets.py collects Tweets from the collected data.
 - insertDB insert the parsed Tweets into a database.
 - CreateTable.sql is the T-SQL file to create the table.
I'm still updating this project. If you find any bugs, please kindly raise an issue:)

