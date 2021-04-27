import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
type(res)
#<class 'requests.models.Respons'>
res.status_code==requests.codes.ok
#true
#ok status code is 200, NOT FOUND status code is 404
len(res.text)
#178981
print(res.text[:250])

