import json
from headers import Headers
from fields import fields, field_names
from get_query_state import get_query_data
from csv import DictWriter
from argparse import ArgumentParser
from selenium import webdriver
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import environ


environ['WDM_LOG_LEVEL'] = '0'

class Sesh:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.zillow.com/')
        sleep(1)

    def get(self, url, json = False):
        method = 'json' if json else 'text'
        script = f'fetch("{url}").then(e => e.{method}()).then(e => window._custom_property = e)'
        self.driver.execute_script(script)
        sleep(2)
        return self.driver.execute_script('return window._custom_property')



default_map_bounds = {"west":-151.08538844001984,"east":-48.25335719001985,"south":1.2662658270896698,"north":58.09685401428484}

headers = Headers()

def get_phone(sesh, url):
    try:
        html = sesh.get(url)
        start = html.index('areacode')
        end = html.index('}', start)
        dict_text = html[start - 2:end]
        dict_text = dict_text.replace('\\', '')
        json_dict = json.loads('{' + dict_text + '}')
        return f"{json_dict['areacode']}-{json_dict['prefix']}-{json_dict['number']}"

    except:
        return "N/A"

def main(url, by_owner, region_code = {}):
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--headless')
    with webdriver.Chrome(ChromeDriverManager().install(), options = options) as driver:
    
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        sesh = Sesh(driver)

        regional_map_bounds, region = get_query_data(sesh, url) if url else (default_map_bounds, None)


        page_num = 1
        first_listing = None
        with open('output.csv', 'w', newline = '') as f:  
            writer = DictWriter(f, field_names)
            writer.writeheader() 

            with open('args.json') as f:
                args = json.load(f)

                args['searchQueryState']['mapBounds'] = regional_map_bounds

                if region_code:
                    k, v = list(region_code.items())[0]
                    args['searchQueryState'][k] = v

                else:
                    args['searchQueryState']['regionSelection'] = [region]

         
                false_val = {'value': False}
                if by_owner:
                    turn_false = ["isAuction", "isNewConstruction", "isComingSoon", "isForSaleByAgent", "isForSaleForeclosure"]

                    for v in turn_false:
                        args['searchQueryState']['filterState'][v] = false_val

                    args['wants'] = { "cat2": ["listResults"], "cat1": ["total"] }
            

            while True:

                args['requestId'] = str(page_num)
                args['searchQueryState']['pagination'] = {'currentPage': page_num}


                url = 'https://www.zillow.com/search/GetSearchPageState.htm?'

                #serialize in their format
                for k, v in args.items():
                    s_args = str(v)
                    s_args = s_args.replace(' ', '')
                    v = f'{k}={s_args}&'
                    url += v


                res = sesh.get(url, json = True)

                # with open('out.html', 'w', encoding = 'utf-8') as f:
                #     f.write(res)
                #     print(json.dumps(args))
                #     print(url)
                #     quit()
                
                main_dict = res.get('cat1') or res.get('cat2')
                listings = main_dict['searchResults']['listResults']
                if not listings:
                    break

                print(f'Page: {page_num}: {len(listings)} listings')

                first = fields[0]['get'](listings[0])

                if page_num == 1:
                    first_listing = first
                elif first_listing == first:
                    break

                for ls in listings:
                    row_dict = {}
                    for field in fields:
                        row_dict[field['name']] = field['get'](ls)

                    row_url = ls['detailUrl']
                    if not row_url.startswith('https'):
                        row_url = 'https://www.zillow.com/' + row_url

                    if by_owner:
                        row_dict['phone'] = get_phone(sesh, row_url)
                    writer.writerow(row_dict)

                page_num += 1

        print('\n\nFINISHED')

    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('URL', help = "The URL of the city to scrape")
    parser.add_argument('-ownr', default = False, action = 'store_const', const = True, help = "If present, only listings for sale by the owner will be grabbed. Defaults to False if not present")
    args = parser.parse_args()
 
    main(args.URL, args.ownr)

