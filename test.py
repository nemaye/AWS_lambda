import praw

r = praw.Reddit(client_id='DygS03uWuXsBOQ',
	client_secret='6pwn5yPHCe6QcFnJiS6mxmeqqTs',
	username='mayum13',
	password='mayum13khan',
	user_agent='theDeenBot by u/nemaye')

subred = r.subreddit("islam")

print(dir(subred.submit))