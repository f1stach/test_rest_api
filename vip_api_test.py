import os
from unittest import skipIf

import pytest
import requests
from vip_api import Vip
from unittest.mock import Mock, patch, MagicMock
from nose.tools import assert_true, assert_is_not_none, assert_list_equal


# Create a fixture for creating class instance
@pytest.fixture()
def vip():
    # Create an instance of a class
    vip = Vip()
    return vip

#
# @patch('vip_api.requests.get')
# def test_get_banner_v1_url(get_mock, vip):
#     # Configure the mock to return a response with an OK status code.
#     get_mock.return_value.ok = True
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_banner_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response != None
#
#
# @patch('vip_api.requests.get')
# def test_get_banner_v1_url_status_ok(get_mock, vip):
#     object_url = {
#         'name': 'Promocja',
#         'link': 'https://www.komputronik.pl',
#         'priority': 1,
#         'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
#     }
#
#     # Creating a function to mock and mocking JSON response with a dictionary from above.
#     get_mock.return_value = Mock(ok=True)
#     get_mock.return_value.json.return_value = object_url
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_banner_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response.json() == object_url
#
#
# @patch('vip_api.requests.get')
# def test_get_banner_v1_url_status_nok(get_mock, vip):
#     # Configure the mock to not return a response with an OK status code.
#     get_mock.return_value.ok = False
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_banner_v1_url()
#
#     # If the response contains an error, I should get None.
#     assert response == None
#
#
# def test_get_banner_v1_url_real_contract():
#     vip_real = Vip()
#
#     # Call the service, which will send a request to the server.
#     response = vip_real.get_banner_v1_url()
#     response_keys = response.json().pop().keys()
#
#     with patch('vip_api.requests.get') as get_mock:
#         get_mock.return_value.ok = True
#         get_mock.return_value.json.return_value = [{
#             'name': 'Promocja',
#             'link': 'https://www.komputronik.pl',
#             'priority': 1,
#             'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
#         }]
#
#         after_mock = vip_real.get_banner_v1_url()
#         after_mock_keys = after_mock.json().pop().keys()
#
#     # An object from mocked and actual API should have the same structure
#     assert list(response_keys) == list(after_mock_keys)
#
#
# @patch('vip_api.requests.get')
# def test_get_premiere_v1_url(get_mock, vip):
#     # Configure the mock to return a response with an OK status code.
#     get_mock.return_value.ok = True
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_premiere_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response != None
#
#
# @patch('vip_api.requests.get')
# def test_get_premiere_v1_url_status_ok(get_mock, vip):
#     object_url = {
#         'title': 'Premiera',
#         'description': 'Mega premiera nowego produktu',
#         'link': 'https://www.komputronik.pl',
#         'type': 'now',
#         'priority': 1,
#         'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
#     }
#
#     # Creating a function to mock and mocking JSON response with a dictionary from above.
#     get_mock.return_value = Mock(ok=True)
#     get_mock.return_value.json.return_value = object_url
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_premiere_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response.json() == object_url
#
#
# @patch('vip_api.requests.get')
# def test_get_premiere_v1_url_status_nok(get_mock, vip):
#     # Configure the mock to not return a response with an OK status code.
#     get_mock.return_value.ok = False
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_premiere_v1_url()
#
#     # If the response contains an error, I should get None.
#     assert response == None
#
#
# @skipIf(os.getenv('SKIP_REAL', False), 'Real API server not responding. Skipping.')
# def test_get_premiere_v1_url_real_contract():
#     vip_real = Vip()
#
#     # Call the service, which will send a request to the server.
#     response = vip_real.get_premiere_v1_url()
#     # response_keys = response.json().pop().keys()
#
#     with patch('vip_api.requests.get') as get_mock:
#         get_mock.return_value.ok = True
#         get_mock.return_value.json.return_value = [{
#             'title': 'Premiera',
#             'description': 'Mega premiera nowego produktu',
#             'link': 'https://www.komputronik.pl',
#             'type': 'now',
#             'priority': 1,
#             'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
#         }]
#
#         after_mock = vip_real.get_premiere_v1_url()
#         after_mock_keys = after_mock.json().pop().keys()
#
#     # An object from mocked and actual API should have the same structure
#     # assert list(response_keys) == list(after_mock_keys)
#
#
# @patch('vip_api.requests.get')
# def test_get_userbyuuid_v1_url(get_mock, vip):
#     # Configure the mock to return a response with an OK status code.
#     get_mock.return_value.ok = True
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_userbyuuid_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response != None
#
#
# @patch('vip_api.requests.get')
# def test_get_userbyuuid_v1_url_status_ok(get_mock, vip):
#     object_url = {
#         'uuid': 1,
#         'login': 'user',
#         'email': 'user',
#         'sales_channel_code': 1,
#         'vip_code': 5,
#         'mobile_phone': 123456789,
#         'vip_agreement': 'yes',
#         'personal_data_agreement': 'yes',
#         'komputronik_ecommerce_agreement': 'yes'
#     }
#
#     # Creating a function to mock and mocking JSON response with a dictionary from above.
#     get_mock.return_value = Mock(ok=True)
#     get_mock.return_value.json.return_value = object_url
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_userbyuuid_v1_url()
#
#     # If the request is sent successfully, then I expect a response to be returned.
#     assert response.json() == object_url
#
#
# @patch('vip_api.requests.get')
# def test_get_userbyuuid_v1_url_status_nok(get_mock, vip):
#
#     # Configure the mock to not return a response with an OK status code.
#     get_mock.return_value.ok = False
#
#     # Call the service, which will send a request to the server.
#     response = vip.get_userbyuuid_v1_url()
#
#     # If the response contains an error, I should get None.
#     assert response == None
#
#
# def test_get_userbyuuid_v1_url_real_contract():
#     vip_real = Vip()
#
#     # Call the service, which will send a request to the server.
#     response = vip_real.get_userbyuuid_v1_url()
#     # response_keys = response.json().pop().keys()
#
#     with patch('vip_api.requests.get') as get_mock:
#         get_mock.return_value.ok = True
#         get_mock.return_value.json.return_value = [{
#             'uuid': 1,
#             'login': 'user',
#             'email': 'user',
#             'sales_channel_code': 1,
#             'vip_code': 5,
#             'mobile_phone': 123456789,
#             'vip_agreement': 'yes',
#             'personal_data_agreement': 'yes',
#             'komputronik_ecommerce_agreement': 'yes'
#         }]
#
#         after_mock = vip_real.get_userbyuuid_v1_url()
#         after_mock_keys = after_mock.json().pop().keys()
#
#     # An object from mocked and actual API should have the same structure
#     # assert list(response_keys) == list(after_mock_keys)
#

# @patch('vip_api.requests.get')
def test_post_coupon_v1_url(vip):
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
    assert response.status_code == 200


def test_post_sales_doc_v1_url():
    # API url
    url = "http://httpbin.org/post"

    # Payload with JSON file to post
    payload = """{
                "sales_document_number": "FV123456",
                "sales_document_amount": "2999.00"
            }"""

    # Make a post request with json input body
    response = requests.post(url, payload)  # data sent successfuly
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200


def test_post_register_user_v1_url():
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
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200