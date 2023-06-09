**About The Project**
---------------------
      
This application helps us to scrap the data from twitter for the specific keyword or hashtag entered with given time period and number of tweets needs to scraped. After that, uploading the scraped data in MongoDB and downloading saved documents into JSON and CSV formats based on user choice

**Built With**
--------------

•	**Language** – Python, **Libraries used** – snscrape, pandas, pymongo

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
User needs to choose either Keyword or Hashtag for the scraping the data and needs to provide other input also such as - start date, end date, number of tweets to be scraped

If we click Scrap the data button and it will show scraped data into table view and we will one more button to upload the data into MongoDB

Once data upload is successful, we will get a success message as Successfully data uploaded into MongoDB
   
**Display**
-----------

This page is designed to list out all the scraped keyword or hashtag in dropdown button. 

So user can choose any one of scraped word from dropdown and saved document will be displayed for choosed scraped word

**Download**
------------

This page is designed to list out all the scraped keyword or hashtag in dropdown button. So user can choose any one of input from dropdown.

If user want to download the document into JSON, they can click Download data as Json 

else go ahead with click Download data as CSV if they want data into CSV format


**Sample Document Saved in MongoDB**
------------------------------------

<img width="532" alt="image" src="https://user-images.githubusercontent.com/129018424/230647740-686d31ed-8ceb-4241-91cd-472ec38a2fc5.png">

**Sample Downloaded Json **
---------------------------
<img width="854" alt="image" src="https://user-images.githubusercontent.com/129018424/230648111-3946392b-edb3-4328-8d44-c04e357d4ec6.png">


**Sample Downloaded CSV**
-------------------------
<img width="960" alt="image" src="https://user-images.githubusercontent.com/129018424/230648176-b13000d9-254e-4427-a154-dafa523018ae.png">





