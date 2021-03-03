import json 
from urllib.request import urlopen

with urlopen("http://api.currencylayer.com/live?access_key=f50ffac22c2df1f274331305ee235cdf") as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=2))


