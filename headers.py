from fake_useragent import UserAgent

ua = UserAgent(fallback='Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]')


class Headers:


    def __init__(self):
        self._headers = {
    'authority': 'www.zillow.com',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zillow.com/',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'sec-gpc': '1',
}

    def update(self, key, val):
        self._headers[key] = val

    @property
    def headers(self):
        self.update('User-Agent', ua.random)
        return self._headers


    def update(self, key, val):
        self._headers[key] = val

