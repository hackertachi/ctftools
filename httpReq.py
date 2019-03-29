import requests

def main():
	myurl = "http://docker.hackthebox.eu:45857/index.php"
	req = {'user1' : 'admin','user2' : 'admin'}
	r = requests.post(myurl,req, allow_redirects=False)
	print(r.status_code)
	print(str(r.text))

if __name__ == "__main__":
	main()
