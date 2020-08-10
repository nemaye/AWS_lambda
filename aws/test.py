import requests

def call_requests(event,context):
	r = requests.get("https://quranreflect.com/posts.json?client_auth_token=tUqQpl4f87wIGnLRLzG61dGYe03nkBQj&q%5Bfilters_operation%5D=OR&q%5Btags_operation%5D=OR&page=1&tab=feed&lang=&verified=&student=&scholar=&approved=&feed=&approved_pages=false&exact_ayah=false&prioritize_ayah=false")
	if r.status_code == 200:
		return "OK"


print(call_requests())