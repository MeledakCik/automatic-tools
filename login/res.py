import requests
# title : Disclosure page
def blocking():
    url = "https://www.instagram.com/fxcal/disclosure/?next=%2F"
    headers = {
        "authority": "www.instagram.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "dpr": "2",
        "priority": "u=0, i",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-full-version-list":' "Google Chrome";v="131.0.6778.266", "Chromium";v="131.0.6778.266", "Not_A Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "",
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-platform-version": '"14.6.1"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "viewport-width": "661",
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)


def cekprofile():
    url = "https://www.instagram.com/api/v1/web/accounts/fb_profile/"
    headers = {
        "authority": "www.instagram.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "dpr": "2",
        "priority": "u=0, i",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-full-version-list":' "Google Chrome";v="131.0.6778.266", "Chromium";v="131.0.6778.266", "Not_A Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "",
        "sec-ch-ua-platform": '"macOS"',
        "sec-ch-ua-platform-version": '"14.6.1"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "viewport-width": "661",
    }
    params = {
        "accessToken": 'eyJhbGciOiJkaXIiLCJraWQiOjIsImN0eSI6IkpXVCJ9...AZUDyCAdNnSykYunll_osldtg1PtF0b-7V8Cat__POI1dZArw9RJ5IDPCTwsHNtxV9T6SaHqWScEDLH1ccNU40S2076l4Pm4kS0ig4fiUKEquJ39W1VcKrDO6WJAOB5IFqauzQ53JjOOpPqdZQi7sFqWJiPALlxufA6Cak-_gxegvpCq3SdKG6BATyS29WdLHgPHq0MrGlUpxWGfaIHQNk7vH6FRe7zPpGwN2y-Yyc1j0TSu5ERmi2B-HEvb5HpylBtgOjX94VRs4pzkayC8EgyBSUMpbFdXtze2V6ii7RNd9-zikNog5PiXE9KXdOP8S1RW9w3YGaHvcJ7YZjIByNsUCCcLEf6ukr04yKDQb5h4lkINhvRi2-v307CkFJmiUU22Zee4o7AQoHPABvMSXBFI8RI9XobrS_iHdXYAbDE15JibSvsZpY1kYHmrkF3F-IJ4C-NM_Sr5h9VQS5Bw8LV68WexOHhYoTOynaooHtgIaMQMcfCZfLKbrvseVWefbnfNABIQiAUnEtNNpMu_pfkYdc-p_Aq10bcC4mIneSFpIl4FLbeylLu8jEK1FqznE0wtJjjHMX6ki8poK5bnzJWFyT3MwRqCet0BuGJhyQvTwOgeWR06bnjvzoIg3_EEhYfKR1P6BMBhhfaBSzg80Cs88FYfsTZ6mq0t3hG-MPclGJh7T4ieZMdLxdLEc-Ie4FiBDZmdouIjRz8RWWYeCYt4_6jGHatAQBqd3_TIhA6yx0sTCyhdDKsBmhMUzUhyr12aa17tSDbCBhazKtqLtka6RJori209yYGwSd3wciedYpZA4wn1hFOjQfd6eSBTEpecq1rtArfIy0LHl3RL3q9bs8NVvhnGGQp_hN2GeoYDJuuhTA.',
        "profilePicSize": '88',
        "useOIDCFlow": 'true',
    }
    response = requests.get(url, headers=headers,data=params)
    print(response.status_code)
    print(response.text)


def login():
    url_post = "https://www.facebook.com/oidc/complete/facebook/?redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignupviafb%2F&code=AaiMzlRI3VnSXKF_HRe816XernyLOjBS5sfZl-fFUkjf_9qo5ttTw_ywW-19ZPNWcYVD3lhSRvCfCnU2ComWRpKqA66iZmuXTZZcPgaMk2OEPBEXYgybVeLbgLvPgrr0sYe5vESi6OhiSAeJ3HFM1bqwnQW3LNZxJ5sHcwdc0uYBizK_0R1dgABT0jHcJuUbI5jj52bR&state=ATC-Qk21HDRsrdYhXMImdCIfj2P5_e3TBCAHze1AVuNPSSjqYXZUuRPIvel4HkolkmkjOeKhgNjuJEHj24bLHtu2ImLShViQzNQ3fiqCul3lJGS80kzC8yS1tY_4tHPZUah-eNbsJIKCCYms1Dm5328YmhGfAZYWhedDxi2HfIC-fY8_SHIxi85Ho2JkZhbhSjNQdEkx72Zj_sDazCbM9l5H7zP0EDhayvsn2Qbcxv9b5ZMIoXs6Hv360prG-IO74t2t&app_id=124024574287414"
    url_get = "https://www.facebook.com/oidc/?app_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignupviafb%2F&response_type=code&scope=openid%20email%20profile%20linking&state=ATC-Qk21HDRsrdYhXMImdCIfj2P5_e3TBCAHze1AVuNPSSjqYXZUuRPIvel4HkolkmkjOeKhgNjuJEHj24bLHtu2ImLShViQzNQ3fiqCul3lJGS80kzC8yS1tY_4tHPZUah-eNbsJIKCCYms1Dm5328YmhGfAZYWhedDxi2HfIC-fY8_SHIxi85Ho2JkZhbhSjNQdEkx72Zj_sDazCbM9l5H7zP0EDhayvsn2Qbcxv9b5ZMIoXs6Hv360prG-IO74t2t"
    url_post_2 = "https://www.instagram.com/api/v1/web/accounts/login/ajax/facebook/"
    header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'pragma': 'no-cache',
    'upgrade-insecure-requests': '1',
    'cookie': '',
    'x-csrftoken': '',
    'x-instagram-ajax': '1',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.266", "Chromium";v="131.0.6778.266", "Not_A Brand";v="24.0.0.0"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': 'macOS',
    'sec-ch-ua-platform-version': '14.6.1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate'
    }
    response = requests.get(url_get, headers=header)
    print(response.status_code)
    print(response.text)
    




blocking()
cekprofile()
login()