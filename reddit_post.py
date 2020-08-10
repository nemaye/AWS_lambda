#while creating app in prefs/app use script

import praw
import json
import requests

source_api = "https://quranreflect.com/posts.json?client_auth_token=tUqQpl4f87wIGnLRLzG61dGYe03nkBQj&q%5Bfilters_operation%5D=OR&q%5Btags_operation%5D=OR&page=1&tab=feed&lang=&verified=&student=&scholar=&approved=&feed=&approved_pages=false&exact_ayah=false&prioritize_ayah=false"
request = requests.get(source_api) #gets response like 200, 300 404 etc
request_txt = request.text

data = json.loads(request_txt)
text = data['posts'][0]['citation_texts']['0'][0]['text']
#text = text + '\n\n\t\t\t\t\t\t\t\t-' + data['posts'][0]['filters'][0]['indicator_text']

r = praw.Reddit(client_id='DygS03uWuXsBOQ',
	client_secret='6pwn5yPHCe6QcFnJiS6mxmeqqTs',
	username='mayum13',
	password='mayum13khan',
	user_agent='theDeenBot by u/nemaye')


subred = r.subreddit("islam")

for sub in new_post:
	print(sub.title)


