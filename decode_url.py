from furl import furl
import json

url = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-73.980532%2C%22east%22%3A-73.482708%2C%22south%22%3A40.876591%2C%22north%22%3A41.366375%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A3148%2C%22regionType%22%3A4%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22],%22cat2%22:[%22total%22]}&requestId=2'

url = furl(url)

args = dict(url.args)


for key, value in args.items():
    if value.startswith('{'):
        args[key] = json.loads(value)

with open('url-args.json', 'w') as f:
    f.write(json.dumps(args))

