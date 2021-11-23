from datetime import datetime


DEBUG = False
ERROR_VAL = "N/A"
def error_decorator(func, err = ERROR_VAL):
    def new_func(*args, **kwargs):
        try:
            return func(*args, **kwargs) or err
        except Exception as e:
            if DEBUG: print(e)
            return err
    
    return new_func


fields = [
    {
        'name': 'address',
        'get': lambda ls: f"{ls['hdpData']['homeInfo']['streetAddress']}, {ls['hdpData']['homeInfo']['city']}, {ls['hdpData']['homeInfo']['state']} {ls['hdpData']['homeInfo']['zipcode']}"
    },
    {
        'name': 'price',
        'get': lambda ls: ls['price']
    },
    {
        'name': 'beds',
        'get': lambda ls: ls['beds']
    },
    {
        'name': 'baths',
        'get': lambda ls: ls['baths']
    },
    {
        'name': 'sqft',
        'get': lambda ls: ls['area']
    },
    #TODO
    {
        'name': 'zestimate',
        'get': lambda ls: ls['hdpData']['homeInfo']['zestimate']
    },
    {
        'name': 'time_on_market',
        'get': lambda ls: (datetime.now() - datetime.utcfromtimestamp(ls['hdpData']['homeInfo']['timeOnZillow']/1000)).days
    },
    {
        'name': 'lot',
        'get': lambda ls: f"{round(ls['hdpData']['homeInfo']['lotAreaValue'], 2)} {ls['hdpData']['homeInfo']['lotAreaUnit']}"
    },
    {
        'name': 'type',
        'get': lambda ls: ls['hdpData']['homeInfo']['homeType']
    },
    {
        'name': 'URL',
        'get': lambda ls: ls['detailUrl']
    },
]


#apply decorator for error checking, decorator for adding base URL
for element in fields:
    element['get'] = error_decorator(element['get'], element.get('errorVal', ERROR_VAL))

field_names = [field['name'] for field in fields] + ['phone']
