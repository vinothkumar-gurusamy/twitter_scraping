**About The Project**
---------------------
      
This application helps us to scrap the data from twitter for the specific keyword or hashtag entered with given time period and number of tweets needs to scraped. After that, uploading the scraped data in MongoDB and downloading saved documents into Json and CSV formats

**Built With**
--------------

•	**Language** – Python, Libraries used – snscrape, pandas, pymongo

•	**NoSQL DB** - MongoDB

•	**GUI** – Streamlit

**Getting Started**
-------------------

This application contains 4 pages in UI and those are all - Home page, Search, Display, Download

**Homepage**
----------
This page tell us what application does and its flow

**Search**
----------
User needs to choose either Keyword or hashtag for the scraping the data and need to provide other input such as - start date, end date, number of tweets to be scraped

If we click Scrap the data button and it will show the scraped data into table format and we will one more button to upload the data into Mongo

Once upload is successful, we will get success message as Successfully data uploaded into MongoDB
   
**Display**
-----------

This page is designed to list out all the scraped keyword or hashtag in dropdown button. So user can choose any one of input from dropdown and saved document will be displayed for choosed one

**Download**
------------

This page is designed to list out all the scraped keyword or hashtag in dropdown button. So user can choose any one of input from dropdown and if user want to download the document into JSON, they can click Download data as Json or else go ahead with click Download data as CSV if they want CSV format




