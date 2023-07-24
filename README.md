# SONY Music Labels Study
In this project, we will study the situation of the different record labels belonging to SONY Music and their artists using data from Spotify.

## Introduction
The idea behind this project is to periodically launch the data extraction script to have a historical record of data stored in a database, connected to PowerBI for real-time report querying at any time.

## Functionality
The study consists of three parts:

### Data Acquisition:
Obtaining data related to each of the record labels belonging to SONY Music. This data will come from Spotify, using their developer API, and the spotipy Python library, which facilitates the use of the API.
To obtain access tokens for the API, it is necessary to register on Spotify and create an app, and the complete process is described at https://developer.spotify.com/documentation/web-api/tutorials/getting-started
The data obtained will include information about artists, songs, and albums. For each item provided by the API, relevant fields will be selected and inserted into separate dataframes for artists, albums, or songs.

### Data Preprocessing:
The data obtained from Spotify, after selecting the relevant fields, will be inserted into pandas dataframes for cleaning and transformation, if necessary.

### PowerBI Reporting:
Once we have clean data, we load it into PowerBI Desktop and generate various reports: one with an overview of the company and one for each of SONY Music's record labels.
This report should be shared through PowerBI Service, but since I do not have a license, the only way to share it is by uploading the file to this repository.

The PowerBI report, Sony Music Report.pbix, is available in the repository. There is also a PDF version of the report for preliminary viewing, although it loses all the interactivity present in the .pbix format report.

## Conclusion
This project is born as a learning endeavor with the sole purpose of gaining knowledge and not for commercial purposes. It is worth clarifying that it is in a very early stage and can be enriched with additional functionality and improvements, which will be mentioned later, and it will be continuously updated as long as time permits.

Below, I mention certain issues I have encountered or that continue to occur during this development:

* The Spotify API organizes certain data in a slightly peculiar way. For example, when obtaining song data, it does not specify the main artist of the song but provides a list of participating artists.
* Some songs (singles) are categorized as belonging to a specific artist due to the reason mentioned above. Therefore, when processed, these songs are stored as their own when they are actually collaborations, as can be seen in the PowerBI report.
* Like any other API, the Spotify API has to limit the number of requests made within a time interval. Although there are ways to optimize batches of requests with API functions, many requests are still required to obtain all the data. This affects the script's execution time and it's essential not to overload the API with requests, so this should be taken into account. One possible solution is to schedule the script periodically (e.g., weekly) and store the data in a database for later use, avoiding making repeated requests to the API.
* The starting file (not present in the repository) is an Excel file with two columns: artists and their corresponding label. This file is manually created by consulting Sony Music's website (https://www.sonymusic.com/labels/) and their labels. This process may lead to errors in data collection, and the label names in the file may not match those in the Spotify API. Ideally, a well-constructed database with verified and up-to-date data directly from SONY Music would be preferred.
* Typically, artists do not produce all their albums under a single label throughout their careers. As a result, historical data for artists who no longer belong to a specific label may generate misleading or irrelevant data for this study.
* There is limited relevant data available to draw deep conclusions. Two possible future improvements include exploring other sources of information (e.g., additional APIs, web scraping) and creating a historical database to perform temporal analysis.

## Future of the Project
The idea is to update the project with enhancements and new functionalities. Some of the ideas planned for future implementation are:

* Storing the data in a database instead of a dataframe.
* Exploring more sources for data retrieval.
* Optimizing the number of requests made to the Spotify API.
* Improving the quality of the reports generated in PowerBI (both in terms of data quality and data analysis and presentation).


Thank you very much for taking the time to check out this project, and if you need to contact me, you can do so through GitHub or by sending an email to **ajsr922@gmail.com**.
