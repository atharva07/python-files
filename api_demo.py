import requests

'''
result = requests.get('http://api.citybik.es/v2/networks')

print(result)

if result:
    print('response ok')
else:
    print('error')

print(result.headers)
print(result.text)

output = open('index.html', 'w')
output.write(result.text)
output.close()
'''

API_KEY = '423937e5d0204179b54bfe790e72bcea'

url = 'https://api.football-data.org/v2/competitions/CL/matches'

res = requests.get(url)
print(res)
