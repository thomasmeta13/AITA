import warnings
warnings.filterwarnings(action="ignore", category=FutureWarning)
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import praw

# Create a Reddit instance
useragent = "Scraper 1.0 by /u/tmeta"
reddit = praw.Reddit(client_id="2A3Rb8B3SPFvMvBMyMAaGA",
                    client_secret="iqcdhEAGaox6hH0y3MWuJ3n1714bDg",
                    user_agent=useragent
)

# Create an empty list to store the filtered headlines
filtered_headlines = []
 # define filtered_df as dtaframe with 3 columns
filtered_df = pd.DataFrame(columns=['title', 'selftext', 'flair'])
# Iterate through the submissions
for submission in reddit.subreddit('AmItheAsshole').rising(limit=None):
    # Check if the link flair text is 'Asshole' or 'Not the A-hole'
    if submission.link_flair_text in ['Asshole', 'Not the A-hole']:
        # Add the title and selftext to the list of filtered headlines
        # combine the title, selftext and flair text to make a row
        row = pd.DataFrame(data = {'title':submission.title, 'selftext': submission.selftext, 'flair':submission.link_flair_text}, index=[0])
        # append the row to the dataframe
        filtered_df = filtered_df.append(row, ignore_index=True)

        # filtered_headlines.append(submission.title)
        # filtered_headlines.append(submission.selftext)
        # filtered_headlines.append(submission.link_flair_text)

# Create a filtered dataframe from the filtered headlines
# filtered_df = pd.DataFrame(filtered_headlines, columns=['headline'])
filtered_df.to_csv("output_rising.csv", index=False)

print(filtered_df)