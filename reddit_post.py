#while creating app in prefs/app use script
import praw
import json
import requests


source_api = "https://quranreflect.com/posts.json?client_auth_token=tUqQpl4f87wIGnLRLzG61dGYe03nkBQj&q%5Bfilters_operation%5D=OR&q%5Btags_operation%5D=OR&page=1&tab=feed&lang=&verified=&student=&scholar=&approved=&feed=&approved_pages=false&exact_ayah=false&prioritize_ayah=false"
#link to the source api from where i get the data

request = requests.get(source_api) #gets response like 200, 300 404 etc
request_txt = request.text
data = json.loads(request_txt)

##################
text = ''
text = data['posts'][0]['body']
text = text + '\n\n' + data['posts'][0]['citation_texts']['0'][0]['text']
text = text + '\n\n\t\t\t\t\t\t\t\t-' + data['posts'][0]['filters'][0]['indicator_text']
#this block extracts the required text to be posted to reddit


subreddit_name = 'islam'

yourUsername = 'yourUsername'
yourPassword= 'yourPassword'

#get your client_id,client_secret from the reddit api
r = praw.Reddit(client_id='DygS03uWuXsBOQ',
	client_secret='6pwn5yPHCe6QcFnJiS6mxmeqqTs',
	username=yourUsername,
	password=yourPassword,
	user_agent='theDeenBot by u/nemaye')


subred = r.subreddit(subreddit_name)
subred.submit(subreddit_name,selftext=text)
print(request.status_code)