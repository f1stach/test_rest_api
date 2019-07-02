import json
from urllib.parse import urljoin

import jsonpath as jsonpath
import requests
import constants


class Vip(object):

    def __init__(self):
        pass

    def get_banner_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.BANNER_V1_URL, verify=False)

        print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_premiere_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.PREMIERE_V1_URL, verify=False)

        print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_userbyuuid_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.USER_GETBYUUID, verify=False)

        print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None


    def post_user_login_v3_url(self):
        payload = """{
            "host": "https://api-komputronik-vippublic.test.netcorner.pl",
            "login": "wojtek",
            "password": "wojtek"
        }"""

        sendkt = requests.post(constants.USER_V3_LOGIN, verify=False, data=payload)

        # print("BIN:", send.text, send.status_code)
        print("KT:", sendkt.text, sendkt.status_code)


    def post_coupon_v1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
            "items": [
                {
                    "code": "SPORT178064",
                    "code_erp": "",
                    "price_net": 26.748,
                    "price_gross": 32.9,
                    "quantity": 1,
                    "tax_rate": 0.23
                }
            ],
            "coupon_code": "VIPRABAT20LO0D"
        }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        print(response.text)
        print(response.status_code)

        # parse response to json format
        response_json = json.loads(response.text)

        # pick ID using json path (id selected from json on a website from url variable) - it will return a list
        form_api = jsonpath.jsonpath(response_json, 'json')
        print(form_api)

        # send = requests.post('http://httpbin.org/post', verify=False, data=payload)

    # sendkt = requests.post('https://api-komputronik-vippublic.test.netcorner.pl/vip/coupon/v1/private/coupon-apply',
        #                        verify=False, data=payload)
        # https://api-komputronik-vippublic.test.netcorner.pl/vip/coupon/v1/customer/coupons/active
        # print("BIN:", send.text, send.status_code)
        # print("KT:", sendkt.text, sendkt.status_code)




test = Vip()
print(test.post_coupon_v1_url())