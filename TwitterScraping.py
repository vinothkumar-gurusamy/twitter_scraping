# Author - Vinothkumar Gurusamy

# This program helps us to scrap the data from twitter and store them into MongoDB
# and creating GUI using streamlit for operations made

# Modules import
import snscrape.modules.twitter as snmtwitter
import streamlit as st
import pandas as pd
import pymongo
from bson.json_util import dumps

# MongoDB connection
client = pymongo.MongoClient(
    "mongodb+srv://vinoth:122385@cluster0.tz2cqxj.mongodb.net/?retryWrites=true&w=majority")
db = client.demo
collections = db.twitterscrap


# Sidebar select box in GUI
def sidebar_select_box(label, ls):
    sideSelRes = st.sidebar.selectbox(label, ls)
    return sideSelRes


# Header text
def header_text(label):
    headerInput = st.header(label)
    return headerInput


# Sub Header text
def sub_header_text(label):
    subHeaderInput = st.header(label)
    return subHeaderInput


# Drop down select box
def select_box(label, ls):
    selRes = st.selectbox(label, ls)
    return selRes


# Passing text input
def txt_input(options):
    txtRes = st.text_input(options, "")
    return txtRes


# Writing the label in GUI
def write(label, val):
    st.write(label, val)


# Passing num input
def num_input(label):
    numRes = st.number_input(label)
    return numRes


# Date selection
def date_selection(label):
    selDate = st.date_input(label)
    return selDate


# Convert pandas dataframe to streamlit dataframe
def convert_pandasdf_to_stdf(df):
    stDataFrame = st.dataframe(df)
    return stDataFrame


# Convert list to pandas dataframe
def pandas_df(ls, columnnames):
    pdDataFrame = pd.DataFrame(ls, columns=columnnames)
    return pdDataFrame


# Scrap the data for the given keyword and hastag
def twitter_search_scraper(searchOptions, txtRes, count, startDate, endDate):
    tweetsList = []
    if searchOptions == "Keyword":
        for i, tweets in enumerate(snmtwitter.TwitterSearchScraper("from:" + txtRes).get_items()):
            if i > count:
                break
            tweetsList.append([tweets.date, tweets.id, tweets.content, tweets.user.username,
                               tweets.replyCount, tweets.retweetCount, tweets.lang,
                               tweets.source, tweets.likeCount])
    else:
        for i, tweets in enumerate(snmtwitter.TwitterSearchScraper(
                txtRes + " since:" + str(startDate) + " until:" + str(endDate)).get_items()):
            if i > count:
                break
            tweetsList.append([tweets.date, tweets.id, tweets.content, tweets.user.username,
                               tweets.replyCount, tweets.retweetCount, tweets.lang,
                               tweets.source, tweets.likeCount])
    return tweetsList


# Scrap the data and display in search page
def scrap_data(tweetList, columnnames):
    if st.button("Scrap the data for the given input"):
        pdData = pandas_df(tweetList, columnnames)
        convert_pandasdf_to_stdf(pdData)

# Upload the scrapped data into MongoDB
def upload_to_mongodb(pdDtF, textRes, startDate, endDate):
    if st.button("Upload the data"):
        docUpload = {}
        convertPdDfToDt = pdDtF.to_dict('records')
        docUpload["Scraped Word"] = textRes
        docUpload["Scrapped Start Date"] = startDate.isoformat()
        docUpload["Scrapped End Date"] = endDate.isoformat()
        docUpload["Scrapped Data"] = convertPdDfToDt
        collections.insert_one(docUpload)
        st.write("Successfully data uploaded into MongoDB")


# Display the available keyword and hashtag already stored
def check_avl_data():
    valuesList = []
    for i in collections.find({}, {"Scraped Word": 1, "_id": 0}):
        key, val = next(iter(i.items()))
        valuesList.append(val)
    dataList = list(set(valuesList))
    retrieveOption = select_box("List out available keyword and hashtag stored already", dataList)
    return retrieveOption


# Display the MongoDB document for selected keyword or hashtag in GUI
def display_data(retrieveValue):
    global displayDoc
    for i in collections.find({"Scraped Word": retrieveValue}):
        displayDoc = i
    if st.button("Display the data for given scraped word"):
        write("", displayDoc)


# Download MongoDB document as JSON and CSV format
def download_data(retrieveValue):
    global displayDoc
    for j in collections.find({"Scraped Word": retrieveValue}):
        displayDoc = j
    jsonData = dumps(displayDoc, indent=2)
    csvData = pd.DataFrame(displayDoc)
    csvData.pop("_id")
    csvData = csvData.to_csv(index=False).encode('utf-8')
    st.download_button(label="Download data as JSON", data=jsonData,
                       file_name="TwitterScrapData.json")
    st.download_button(label="Download data as CSV", data=csvData, file_name="TwitterScrapData.csv",
                       mime="csv")


def main():
    operationLists = ["Home", "Search", "Display", "Download"]
    searchOptionsLists = ["Keyword", "Hashtag"]
    columnnames = ["Datetime", "Tweet Id", "Text", "Username", "ReplyCount", "RetweetCount",
                   "Language", "Source", "LikeCount"]
    sidebarSelResult = sidebar_select_box("Which operation you want to perform", operationLists)
    # Home Page
    if sidebarSelResult == "Home":
        header_text("Twitter Scraping")
        write("This application helps us to scrap the data from twitter for the specific keyword or hashtag entered "
              "with given time period and number of tweets needs to be  scraped. After that, uploading the scraped data"
              "in MongoDB and downloading saved documents into Json and CSV formats", "")
    # Search Page
    elif sidebarSelResult == "Search":
        searchOptions = select_box("Choose either keyword or hashtag to be searched", searchOptionsLists)
        write("Going ahead with ", searchOptions)
        textRes = txt_input(searchOptions)
        count = num_input("How many tweets needs to be scraped")
        startDate = date_selection("Start date")
        endDate = date_selection("End date")
        tweetList = twitter_search_scraper(searchOptions, textRes, count, startDate, endDate)
        scrap_data(tweetList, columnnames)
        pandasDf = pandas_df(tweetList, columnnames)
        upload_to_mongodb(pandasDf, textRes, startDate, endDate)
    # Display Page
    elif sidebarSelResult == "Display":
        retrieveValue = check_avl_data()
        display_data(retrieveValue)
    # Download Page
    elif sidebarSelResult == "Download":
        retrieveValue = check_avl_data()
        download_data(retrieveValue)


pdData, stData = 0, 0
# Calling the main function
if __name__ == '__main__':
    main()
