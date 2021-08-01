import requests
import sys
import pandas as pd
from datetime import date

# data columns we're interested
reddit_data_col = ["subreddit", "title", "score", "num_comments", "upvote_ratio", "gilded", "author"]

# Error handling for input
try:
    subreddit, limit, timeframe, sort_cat = input('Enter the subreddit\'s posts you want to view in the following format:\n'
                                                  '"{subreddit}, {number of posts}, {timeframe}, {sort category}"\n'
                                                  'without the {} or "" (e.g. all, 100, year, top):\n'
                                         ).split(",")
    input_list = [subreddit, limit, timeframe, sort_cat]
    for i in range(0,len(input_list)):
        input_list[i] = input_list[i].strip()
    if any(input_list) is None:
        raise ValueError
    if input_list[0].isalpha() == False or input_list[1].isnumeric == False \
            or input_list[2].lower() not in ["hour", "day", "week", "month", "year", "all"]\
            or input_list[3].lower() not in ["controversial", "best", "hot", "new", "random", "rising", "top"]:
        raise ValueError

    input_list[1] = int(input_list[1])

except ValueError:
    print('Error: Invalid input.')
    sys.exit()


# Query reddit to return a JSON file for requested data
def get_reddit(input_list_curr):
    subreddit = input_list_curr[0]
    limit = input_list_curr[1]
    timeframe = input_list_curr[2]
    sort_cat = input_list_curr[3]
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{sort_cat}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers={'User-agent': 'yourbot'})
    except:
        print('Error retrieving data.')
    return request.json()


# parse requested data and create a list of all the retrieved posts
def get_posts(input_list_curr):
    r_data = get_reddit(input_list)
    all_posts = []
    for post in r_data['data']['children']:
        all_posts.append(post)
    return all_posts


# return output to df
def output_results(input_list_curr):
    all_posts = get_posts(input_list_curr)
    output_df = pd.DataFrame(columns = reddit_data_col)
    for i in range(len(all_posts)):
        row_i = []
        for j in range(len(reddit_data_col)):
            row_i.append(all_posts[i]['data'][reddit_data_col[j]])
        output_df.loc[i] = row_i
    return output_df


# output results to .csv
reddit_results = output_results(input_list)
date_today = date.today().strftime("%d%m%Y")
reddit_results.to_csv(f"Reddit-{input_list[0]}-{input_list[1]}-{input_list[2]}-"
                      f"{input_list[3]}_{date_today}.csv", index=False)