#!/usr/bin/env python3

import requests
import json


gitlab_api_secret = '5L5N4kpo212zVyXHdfbW'
gitlab_url = 'https://git.etick.ir'
projects_urls_list = []

try:
    for page in range(1, 8):
        response = requests.get(gitlab_url + '/api/v4/projects?per_page=100&page=' + str(page),
                                headers={'Private-Token': gitlab_api_secret})
        for item in json.loads(response.text):
            projects_urls_list.append(item.get('web_url'))
        if response.status_code != 200:
            raise ValueError('Request returned an error %s, the response is:\n%s' %
                             (response.status_code, response.text))
except Exception as e:
    print(e)
    exit(1)

print(len(projects_urls_list))
