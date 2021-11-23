from selenium import webdriver
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from main import main
from os import environ
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-ownr', default = False, action = 'store_const', const = True, help = "If present, only listings for sale by the owner will be grabbed. Defaults to False if not present")
args = parser.parse_args()

environ['WDM_LOG_LEVEL'] = '0'


with open('middleware.js') as f:
    middleware_code = f.read()

with open('get_region.js') as f:
    get_region_code = f.read()


def process_t_f(inp):
    return 't' in inp.lower()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
with webdriver.Chrome(ChromeDriverManager().install(), options = options) as driver:
    
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.maximize_window()
    driver.get('https://www.zillow.com/homes/')
    driver.execute_script(middleware_code)
    
    region_code = False
    while not region_code:
        region_code = driver.execute_script(get_region_code)
        print(region_code)
        sleep(0.5)
        

print('continuing...\n')
if not region_code:
    print('Unexpected error occured, retry')
    quit()
try:
    main('', args.ownr, region_code)
except Exception as e:
    print('Warning:', e)