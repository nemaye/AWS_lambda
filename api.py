import json
import requests
from shutil import copy
import os
import io
import unicodedata

count = 0 
init_index = 0
final_index = 0
ns = ''

def add_lines(string):
	global count, init_index, final_index, ns
	for i in string:
		final_index = final_index+1
		if i == ' ':
			count = count + 1
		if count is 8:
			ns = ns + string[init_index:final_index]+'\n'
			init_index = final_index

			count = 0
	ns = ns + string[init_index:final_index]
	return ns

src = '/home/nemaye/.conky/template'
dest = '/home/nemaye/.conky/api_islamic'
copy(src,dest)

target = "https://quranreflect.com/posts.json?client_auth_token=tUqQpl4f87wIGnLRLzG61dGYe03nkBQj&q%5Bfilters_operation%5D=OR&q%5Btags_operation%5D=OR&page=1&tab=feed&lang=&verified=&student=&scholar=&approved=&feed=&approved_pages=false&exact_ayah=false&prioritize_ayah=false"
#target = "http://api.zippopotam.us/us/ma/belmont"

request = requests.get(target) #gets response like 200, 300 404 etc
request_txt = request.text

data = json.loads(request_txt)



text = data['posts'][0]['citation_texts']['0'][0]['text']
text = text + '\n\n\t\t\t\t\t\t\t\t-' + data['posts'][0]['filters'][0]['indicator_text']

string = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')

print(string[3])
print('____________________')
print(text[30:35])
print(type(string))

new_string = add_lines(string)
print(count)
print(new_string)
print(string)
file_name = '/home/nemaye/.conky/api_islamic'

f = open(file_name,'a')
f.write(new_string)
f.close()
