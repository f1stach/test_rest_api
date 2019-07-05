import json
from urllib.parse import urljoin
import jsonpath as jsonpath
import requests
import constants
import payloads
import urls


class Vip(object):

    def __init__(self):
        pass

    def get_banner_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.

        url = urls.get_banner_v1

        response = requests.get(url, verify=False)

        if response.ok:
            print(json.dumps(response.json(), indent=4))
            return response.status_code
        else:
            return None

    def get_premiere_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.

        url = urls.get_premiere_v1

        head = {'Authorization': 'Bearer ' + payloads.login_user['auth_token']}

        response = requests.get(url,  headers=head, verify=False)

        if response.ok:
            print(json.dumps(response.json(), indent=4))
            return response.status_code
        else:
            print("Error customer.002")
            return None

    def get_userbyuuid_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.

        url = urls.get_userbyuuid_v1

        head = {'Authorization': 'Key ' + 'thu0Eb8uiVoo7choobaepoh4thigh6Hae9aipie2du1NaeQueiz0fae6ieshopho'}

        response = requests.get(url, headers=head, verify=False)

        if response.ok:
            print(json.dumps(response.json(), indent=4))
            return response.status_code
        else:
            print("Error customer.001")
            return None

    def get_userbytoken_v1_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.

        url = urls.get_userbytoken_v1

        head = {'Authorization': 'Bearer ' + payloads.login_user['auth_token']}

        response = requests.get(url, headers=head, verify=False)

        if response.ok:
            print(json.dumps(response.json(), indent=4))
            return response.status_code
        else:
            return None

    def get_userbytoken_v3_url(self):
        # Make an HTTP request and return an HTTP response in the form of Response object which is JSON.
        # Get function communicates with the external server.

        url = urls.get_userbytoken_v3

        head = {'Authorization': 'Bearer ' + payloads.login_user['auth_token']}

        response = requests.get(url, headers=head, verify=False)

        if response.ok:
            print(json.dumps(response.json(), indent=4))
            return response.status_code
        else:
            return None

    def user_profile(self):
        profile_data = payloads.data_profile

        return profile_data

    def post_register_user_v1_url(self):
        # API url
        url = urls.register_user_v1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, data=payload, verify=False)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            print(json.dumps(response.json(), indent=4))
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            print("API error.")
            return bad_url, "api.001"

    def post_register_user_v1_check_error(self):
        # API url
        url = urls.register_user_v1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, data=payload, verify=False)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        print(response_json)

        if len(response_json['form']['email']) == 0:
            print("Fill in your email address.")
            return "customer.003"
        elif len(response_json['form']['password']) == 0:
            print("Fill in your password.")
            return "customer.004"
        elif len(response_json['form']['mobile_phone']) == 0:
            print("Fill in your mobile phone number.")
            return "customer.005"
        elif len(response_json['form']['vip_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.006"
        elif len(response_json['form']['personal_data_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.007"
        elif len(response_json['form']['komputronik_ecommerce_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        else:
            token_number = payloads.token_number['token']
            print("Authorised. Token number:")
            return token_number

    def post_register_user_v1_1_url(self):
        # API url
        url = urls.register_user_v1_1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            print(json.dumps(response.json(), indent=4))
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            print("API error.")
            return bad_url, "api.001"

    def post_register_user_v1_1_check_error(self):
        # API url
        url = urls.register_user_v1_1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if len(response_json['form']['email']) == 0:
            print("Fill in your email address.")
            return "customer.003"
        elif len(response_json['form']['password']) == 0:
            print("Fill in your password.")
            return "customer.004"
        elif len(response_json['form']['mobile_phone']) == 0:
            print("Fill in your mobile phone number.")
            return "customer.005"
        elif len(response_json['form']['vip_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.006"
        elif len(response_json['form']['personal_data_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.007"
        elif len(response_json['form']['komputronik_ecommerce_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        else:
            token_number = payloads.token_number['token']
            print("Authorised. Token number:")
            return token_number

    def post_register_user_v2_url(self):
        # API url
        url = urls.register_user_v2

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            print("API error.")
            return bad_url, "api.001"

    def post_register_user_v2_check_error(self):
        # API url
        url = urls.register_user_v2

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if len(response_json['form']['email']) == 0:
            print("Fill in your email address.")
            return "customer.003"
        elif len(response_json['form']['password']) == 0:
            print("Fill in your password.")
            return "customer.004"
        elif len(response_json['form']['mobile_phone']) == 0:
            print("Fill in your mobile phone number.")
            return "customer.005"
        elif len(response_json['form']['vip_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.006"
        elif len(response_json['form']['personal_data_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.007"
        elif len(response_json['form']['komputronik_ecommerce_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        else:
            token_number = payloads.token_number['token']
            print("Authorised. Token number:")
            return token_number

    def post_register_user_v2_1_url(self):
        # API url
        url = urls.register_user_v2_1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            print("API error.")
            return bad_url, "api.001"

    def post_register_user_v2_1_check_error(self):
        # API url
        url = urls.register_user_v2_1

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if len(response_json['form']['email']) == 0:
            print("Fill in your email address.")
            return "customer.003"
        elif len(response_json['form']['password']) == 0:
            print("Fill in your password.")
            return "customer.004"
        elif len(response_json['form']['mobile_phone']) == 0:
            print("Fill in your mobile phone number.")
            return "customer.005"
        elif len(response_json['form']['vip_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.006"
        elif len(response_json['form']['personal_data_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.007"
        elif len(response_json['form']['komputronik_ecommerce_agreement']) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        else:
            token_number = payloads.token_number['token']
            print("Authorised. Token number:")
            return token_number

    def post_register_user_v3_url(self):
        # API url
        url = urls.register_user_v3

        # Payload with JSON file to post
        payload = payloads.register_user

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            print("API error.")
            return bad_url, "api.001"

    def post_register_user_v3_check_error(self):
        # API url
        url = urls.register_user_v3

        # Payload with JSON file to post
        payload = payloads.register_user_v3

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if len(response_json['form']['name']) == 0 or len(payload['mail']) == 0:
            print("Fill in your name and email address.")
            return "customer.003"
        elif len(response_json['form']['password']) == 0:
            print("Fill in your password.")
            return "customer.004"
        elif len(response_json['form']['phone']) == 0:
            print("Fill in your mobile phone number.")
            return "customer.005"
        elif len(response_json['form']['city']) == 0 or len(payload['birthday']) == 0:
            print("Fill in city and date of birth.")
            return "customer.009"
        elif len(response_json['form']['agreements'][0]) == 0:
            print("Choose if you agree or not.")
            return "customer.006"
        elif len(response_json['form']['agreements'][1]) == 0:
            print("Choose if you agree or not.")
            return "customer.007"
        elif len(response_json['form']['agreements'][2]) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        elif len(response_json['form']['agreements'][3]) == 0:
            print("Choose if you agree or not.")
            return "customer.008"
        else:
            token_number = payloads.token_number['token']
            print("Authorised. Token number:")
            return token_number

    # Return profile data and token after login and response if token has changed or not
    def post_change_login_token(self):
        # API url
        url = urls.url_change_login_token

        # Payload with JSON file to post
        payload = payloads.change_login_token

        payload_dump = json.dumps(payload)
        payload_json = json.loads(payload_dump)

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        response_json = json.loads(response.text)
        j_path = jsonpath.jsonpath(response_json, 'form')

        print(j_path[0])
        print(payload_json)
        # print(response_json["data"])
        # print(response.text)

        if payload_json['token'] == j_path[0]['token']:
            print("Token ok")
            return self.user_profile()
        else:
            print("Error! Token has changed!", response_json["data"])
            return False

    def post_login_user_v1_url(self):
        # API url
        url = urls.url_login_user_v1

        # Payload with JSON file to post
        payload = payloads.login_user

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

    def post_login_user_v1_check_error(self):
        # API url
        url = urls.url_login_user_v1

        # Payload with JSON file to post
        payload = payloads.login_user

        srv_response = requests.get(url)

        passsw = {
                   "login": "wojtek",
                   "password": "wojtek"
                }

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if response_json['form']['profile'][1] != passsw['login'] or response_json['form']['auth_token'] != passsw['password']:
            print("Wrong login or password.")
            return "coupon.002"
        else:
            print("User logged in. Token:", payloads.token_number['token'])
            return self.user_profile()

    def post_login_user_v3_url(self):
        # API url
        url = urls.url_login_user_v3

        payload = payloads.login_user

        response = requests.post(url, verify=False, data=payload)

        # Print the response JSON:
        # print(response.text)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_login_user_v3_check_error(self):
        # API url
        url = urls.url_login_user_v3

        # Payload with JSON file to post
        payload = payloads.login_user

        srv_response = requests.get(url)

        passsw = {
            "login": "wojtek",
            "password": "wojtek"
        }

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        if response_json['form']['profile'][1] != passsw['login'] or response_json['form']['auth_token'] != passsw['password']:
            print("Wrong login or password.")
            return "coupon.002"
        else:
            print("User logged in. Token:", payloads.token_number['token'])
            return self.user_profile()

    def post_deactivate_user_v1_url(self):
        # API url
        url = urls.url_deactivate_user_v1

        # Payload with JSON file to post
        payload = payloads.deactivate_user_v1

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_reset_password_v1_url(self):
        # API url
        url = urls.url_reset_password_v1

        # Payload with JSON file to post
        payload = payloads.reset_password_v1

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_personal_data_update_v3_url(self):
        # API url
        url = urls.url_personal_data_update_v3

        # Payload with JSON file to post
        payload = payloads.personal_data_update_v3

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.text)
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_coupon_v1_url(self):
        # API url
        url = urls.url_coupon_v1

        head = {'Authorization': 'Key ' + 'thu0Eb8uiVoo7choobaepoh4thigh6Hae9aipie2du1NaeQueiz0fae6ieshopho'}

        # Payload with JSON file to post
        payload = payloads.payload_coupon_v1

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly
        # print(response.status_code)

        if url == constants.TEST_URL:
            correct_url = response.status_code
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_coupon_v1_check_error(self):
        # API url
        url = urls.url_coupon_v1

        # Payload with JSON file to post
        payload = json.dumps(payloads.payload_coupon_v1)
        # payload = payloads.payload_coupon_v1

        # Make a post request with json input body
        response = requests.post(url, payload)  # data sent successfuly

        # parse response to json format
        response_json = json.loads(response.text)

        # print(response_json['json']['items']['code'])

        if len(response_json['json']['coupon_code']) == 0:
            print("Fill in the coupon code number.")
            return "coupon.019"
        elif response_json['json']['items']['code'] == 0:
            print("Fill in the netto price.")
            return "coupon.008"
        elif response_json['json']['items']['code_erp'] == 0:
            print("Fill in the erp code.")
            return "coupon.012"
        elif response_json['json']['items']['price_net'] == 0:
            print("Fill in the netto price.")
            return "coupon.015"
        elif response_json['json']['items']['price_gross'] == 0:
            print("Fill in the gross price.")
            return "coupon.016"
        elif response_json['json']['items']['quantity'] == 0:
            print("Fill in the quantity.")
            return "coupon.017"
        elif response_json['json']['items'] == 0:
            print("Fill in the tax rate.")
            return "coupon.018"
        else:
            print("Coupon added.")
            return response_json

    # if len(response_json['form']['items']['code']) == 0:
        #     print("jest")
        #     return

        # https://api-komputronik-vippublic.test.netcorner.pl/vip/coupon/v1/customer/coupons/active

    def post_sales_doc_v1(self):
        # API url
        url = urls.url_sales_doc_v1

        # Payload with JSON file to post
        payload = payloads.payload_sales_doc_v1

        # Payload with JSON file to post
        head = {'Authorization': 'Bearer ' + payloads.login_user['auth_token']}

        response = requests.post(url, payload, headers=head, verify=False)

        # print(response.text)
        # print(response.status_code)

        if response.ok and url == constants.TEST_URL:
            correct_url = response.status_code
            print(json.dumps(response.json(), indent=4))
            return correct_url
        else:
            bad_url = response.status_code
            return bad_url

    def post_sales_doc_v1_check_error(self):
        url = urls.url_sales_doc_v1

        # Payload with JSON file to post
        payload = payloads.payload_sales_doc_v1

        # Payload with JSON file to post
        head = {'Authorization': 'Bearer ' + payloads.login_user['auth_token']}

        response = requests.post(url, payload, headers=head, verify=False)

        # parse response to json format
        response_json = json.loads(response.text)

        if len(response_json['form']['sales_document_amount']) == 0:
            print("Fill in the document's amount.")
            return "sales-document.001"
        elif len(response_json['form']['sales_document_number']) == 0:
            print("Fill in the document's number.")
            return "sales-document.002"
        else:
            print("Document added successfully.")
            return response.status_code

test = Vip()
print(test.post_sales_doc_v1_check_error())



# print(payloads.login_user['profile']['uuid'])