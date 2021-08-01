# Reddit 
## Overview
This program allows for user input in the format "{subreddit}, {number of posts}, {timeframe}, {sort category}", and queries the reddit API for the specified data. It parses the returned JSON file and outputs the data as a .csv file. Requested parameters (column variables) can be changed within the code.

* subreddit: A specific sub-section of reddit, e.g. r/python (https://www.reddit.com/r/Python/).
* number of posts: The number of posts you want returned, e.g. 100.
* timeframe: The timeframe from which you want posts you returned (i.e. hour, day, week, month, year, all).
* sort category: The sorting method you want to pick posts from over the timeframe (i.e. controversial, best, hot, new, random, rising, top). More information about it here: https://www.reddit.com/r/help/comments/94q9hk/what_is_the_difference_between_the_6_types_of/. 

## Program Files
* reddit-api-first.py: Contains the code performing the above function.
* Reddit-all-100-year-top_02082021.csv: An example output for the query "all, 100, year, top". Output file name is saved in the format "Reddit-{subreddit}-{number of posts}-{timeframe}-{sort category}\_{current date}".

## Example: Requesting "all, 100, year, top"
This request is for the top 100 posts over the last year from the subreddit "all". Resultant output:

![image](https://user-images.githubusercontent.com/62014067/127779710-9302408d-70de-4e49-9e6e-7803a6dd1f1f.png)


