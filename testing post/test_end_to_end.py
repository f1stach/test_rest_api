import requests
import json
import jsonpath


def test_add_new_data():
    app_url = 'http://thetestingworldapi.com/api/studentsDetails'
    file = open('E:\\Dane\\Praca\\Komputronik\\PyCharm projekt\\untitled\\requestjson.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(app_url, request_json)
    id_url = jsonpath.jsonpath(response.json(), 'id')

    print("\nid:", id_url[0])

    print(response.text)
    print(response.status_code)

    tech_api_url = '/http://thetestingworldapi.com/api/technicalskills'
    file = open('E:\\Dane\\Praca\\Komputronik\\PyCharm projekt\\untitled\\requestjson_tech.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    # get response
    # final_details = '/http://thetestingworldapi.com/api/FinalStudentDetails/{id}'
    final_details = '/http://thetestingworldapi.com/api/FinalStudentDetails/3044'
    response = requests.get(final_details)
    print(response.text)