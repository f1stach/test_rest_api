import pytest
import requests
from vip_api import Vip
from unittest.mock import Mock, patch, MagicMock
from nose.tools import assert_true, assert_is_not_none, assert_list_equal


@patch('vip_api.requests.get')
def test_get_banner_v1_url_status_ok(get_mock):
    vip = Vip()

    banner_url = [{
        'name': 'Promocja',
        'link': 'https://www.komputronik.pl',
        'priority': 1,
        'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
    }]

    # Creating a function to mock and mocking JSON response with a dictionary from above.
    get_mock.return_value = Mock(ok=True)
    get_mock.return_value.json.return_value = banner_url

    # Call the service, which will send a request to the server.
    response = vip.get_banner_v1_url()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response.json() == banner_url


@patch('vip_api.requests.get')
def test_get_banner_v1_url_status_nok(get_mock):
    vip = Vip()

    # Configure the mock to not return a response with an OK status code.
    get_mock.return_value.ok = False

    # Call the service, which will send a request to the server.
    response = vip.get_banner_v1_url()

    # If the response contains an error, I should get None.
    assert response == None


@patch('vip_api.requests.get')
def test_get_banner_v1_url(get_mock):
    # Create an instance of a class
    vip = Vip()

    # Configure the mock to return a response with an OK status code.
    get_mock.return_value.ok = True

    # Call the service, which will send a request to the server.
    response = vip.get_banner_v1_url()

    # If the request is sent successfully, then I expect a response to be returned.
    assert response != None
