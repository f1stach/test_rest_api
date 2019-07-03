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

        # print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_premiere_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.PREMIERE_V1_URL, verify=False)

        # print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_userbyuuid_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.USER_GETBYUUID, verify=False)

        # print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_userbytoken_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.USER_GETBYTOKEN_V1, verify=False)

        # print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def get_userbytoken_v3_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.
        response = requests.get(constants.USER_GETBYTOKEN_V3, verify=False)

        # print(json.dumps(response.json(), indent=4))

        if response.ok:
            return response
        else:
            return None

    def user_profile(self):
        profile_data = """{
                      "uuid": "1234",
                      "login": "login",
                      "email": "example@example.com",
                      "sales_channel_code": "website",
                      "vip_code": "98765",
                      "mobile_phone": "987654321",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        return profile_data

    def post_register_user_v1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                      "email": "example@example.com",
                      "password": "password",
                      "mobile_phone": "123456789",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_register_user_v1_1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                      "email": "example@example.com",
                      "password": "password",
                      "mobile_phone": "123456789",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_register_user_v2_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                      "email": "example@example.com",
                      "password": "password",
                      "mobile_phone": "123456789",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_register_user_v2_1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                      "email": "example@example.com",
                      "password": "password",
                      "mobile_phone": "123456789",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_register_user_v3_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                      "email": "example@example.com",
                      "password": "password",
                      "mobile_phone": "123456789",
                      "vip_agreement": "yes",
                      "personal_data_agreement": "yes",
                      "komputronik_ecommerce_agreement": "yes"
                  }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_login_user_v1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                       "host": "https://api-komputronik-vippublic.test.netcorner.pl/",
                       "login": "user",
                       "password": "haslo"
                   }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # Print the response JSON:
        print(response.text)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_login_user_v3_url(self):
        # API url
        url = "http://httpbin.org/post"

        payload = """{
                    "host": "https://api-komputronik-vippublic.test.netcorner.pl",
                    "login": "wojtek",
                    "password": "wojtek"
                }"""

        response = requests.post(url, verify=False, data=payload)

        # Print the response JSON:
        print(response.text)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    # Return profile data and token after login and response if token has changed or not
    def post_change_login_token(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                       "host": "https://api-komputronik-vippublic.test.netcorner.pl/",
                       "login": "user",
                       "password": "haslo",
                       "token": "abcd"
                   }"""

        payload_dump = json.dumps(payload)
        payload_json = json.loads(payload_dump)

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        response_json = json.loads(response.text)
        j_path = jsonpath.jsonpath(response_json, 'data')

        # print(j_path[0])
        # print(payload_json)
        # print(response_json["data"])
        # print(response.text)

        if payload_json == j_path[0]:
            print("Token ok", response_json["data"])
            return self.user_profile()
        else:
            print("Error! Token has changed!", response_json["data"])
            return False

    def post_deactivate_user_v1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                       "uuid": "abc123"
                   }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_reset_password_v1_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                       "host": "https://api-komputronik-vippublic.test.netcorner.pl/",
                       "login": "user"
                   }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_personal_data_update_v3_url(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                       "token": "a044966d-837f-4d5d-ae87-91bafc4d5142",
                       "host": "https://api-komputronik-vippublic.test.netcorner.pl/",
                       "name": "Eryk",
                       "city": "Konin",
                       "birthday": "2000-12-12"
                   }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

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
        # print(response.text)

        data = response.json()

        print(response.status_code)
        print(data)

        # parse response to json format
        response_json = json.loads(response.text)
        print(response_json)

        # pick ID using json path (id selected from json on a website from url variable) - it will return a list
        form_api = jsonpath.jsonpath(response_json, 'json')
        # print(form_api[0])

        # print(response_json['data'][0][0])

        for i in response_json['data']:
            if 'items' in i:
                print(i['items'][0]['code'])
            else:
                print("Go away")

        if not 'code' in response_json or len(response_json['code']) == 0:
            print("wtf")
        else:
            print("fuck")

        # temp = json.load(response)
        # for lines in temp:
        #     text = lines['text']
        #     print(text)
        #
        x = "quantity" in payload
        #
        # for line in response_json:
        #     j = json.loads(line)
        #     try:
        #         if 'text' in j:
        #             print('TEXT: ', j['text'])
        #         elif 'delete' in j:
        #             print('DELETE: ', j['delete'])
        #         else:
        #             print('Everything: ', j)
        #     except:
        #         print("EXCEPTION: ", j)
        #
        return x



        #
        # if url == constants.TEST_URL:
        #     correct_url = response.status_code
        #     return correct_url and response.text
        # else:
        #     bad_url = response.status_code
        #     return bad_url

        # send = requests.post('http://httpbin.org/post', verify=False, data=payload)

    # sendkt = requests.post('https://api-komputronik-vippublic.test.netcorner.pl/vip/coupon/v1/private/coupon-apply',
        #                        verify=False, data=payload)
        # https://api-komputronik-vippublic.test.netcorner.pl/vip/coupon/v1/customer/coupons/active
        # print("BIN:", send.text, send.status_code)
        # print("KT:", sendkt.text, sendkt.status_code)


    def post_sales_doc_v1(self):
        # API url
        url = "http://httpbin.org/post"

        # Payload with JSON file to post
        payload = """{
                        "sales_document_number": "FV123456",
                        "sales_document_amount": "2999.00"
                    }"""

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        print(response.status_code)
        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

test = Vip()
print(test.post_coupon_v1_url())
