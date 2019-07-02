import requests
import json
import jsonpath

# API url
url = 'https://reqres.in/api/users'

# the point of this test is to check the response status code. Should be 201 - then test is passed.

def test_create_new_user():
    # Read input JSON file in read-only mode
    file = open('E:\\Dane\\Praca\\Komputronik\\PyCharm projekt\\untitled\\json_test.json', 'r')
    # the content is a string:
    json_input = file.read()
    # put into json format
    request_json = json.loads(json_input)
    # make a post request with json input body - arguments are: url with api and data in json format
    response = requests.post(url, request_json)  # data sent successfuly
    # validating response code - success is under code 201
    assert response.status_code == 201


def test_create_other_user():
    # Read input JSON file in read-only mode
    file = open('E:\\Dane\\Praca\\Komputronik\\PyCharm projekt\\untitled\\json_test.json', 'r')
    # the content is a string:
    json_input = file.read()
    # put into json format
    request_json = json.loads(json_input)
    # make a post request with json input body - arguments are: url with api and data in json format
    response = requests.post(url, request_json)  # data sent successfuly
    response_json = json.loads(response.text)
    # pick ID using json path (id selected from json on a website from url variable) - it will return a list
    id_api = jsonpath.jsonpath(response_json, 'id')
    print(id_api[0])
    # the output is 834 and it will change after every new program run. It means that every time
    # we are running a new resource is created on a server