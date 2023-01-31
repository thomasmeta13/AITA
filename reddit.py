CLIENT_ID = "2A3Rb8B3SPFvMvBMyMAaGA"
SECRET_KEY = "iqcdhEAGaox6hH0y3MWuJ3n1714bDg"

import requests
import pandas as pd

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
data = {'grant_type': 'password',
        'username': 'tmeta', 
        'password': 'Thomas.meta13'}
    
headers = {'User-Agent': 'MyAPI/0.0.1'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

TOKEN = res.json()['access_token']
headers['Authorization'] = f'bearer {TOKEN}'

res = requests.get('https://oauth.reddit.com/r/AmItheAsshole/top', headers=headers, params={'limit': '100', 'after': 't3_10pe3qk'})

df = pd.DataFrame()

# Store the posts
for post in res.json()['data']['children']:
    if post['data']['link_flair_text'] == 'Asshole':
        df = df.append({
            'title': post['data']['title'],
            'score': post['data']['score'],
            'id': post['data']['id'],
            'url': post['data']['url'],
            'comms_num': post['data']['num_comments'],
            'created': post['data']['created'],
            'body': post['data']['selftext'],
        }, ignore_index=True)


# Save the dataframe to a CSV file
df.to_csv("output.csv", index=False)


# Print the dataframe
print(df)
print(post['kind'] + '_' + post['data']['id'])
