import pytest
import requests
from vip_api import Vip

from unittest.mock import Mock, patch

from nose.tools import assert_true, assert_is_not_none


@patch('vip_api.requests.get')
def test_get_banner_v1_url_status_ok(get_mock):
    banner_url = [{
        'name': 'Mega promocja',
        'link': 'https://www.komputronik.pl',
        'priority': 1,
        'image-url': 'https://static.komputronik.pl/product-picture/6/MYSZGHPMS400-1.jpg'
    }]



@patch('vip_api.requests.get')
def test_get_banner_v1_url(get_mock):
    vip = Vip()

    get_mock.return_value.ok = True

    response = vip.get_banner_v1_url()

    assert response != None
