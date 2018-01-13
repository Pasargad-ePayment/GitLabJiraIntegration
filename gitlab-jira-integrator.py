#!/usr/bin/env python3

import json

import requests
from splinter import Browser

gitlab_api_secret = 'SECRET_TOKEN'
gitlab_url = 'https://git.yourdomain.TLD'
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

browser = Browser()
browser.visit('https://git.yourdomain.TLD/users/sign_in')
browser.fill('username', 'privilaged_user')
browser.fill('password', 'passwd')
browser.find_by_name('commit').click()

for url in projects_urls_list:
    browser.visit(url + '/services/jira/edit')
    #browser.find_by_id('service_active').click()
    browser.find_by_id('service_url').first.value = 'http://jira.yourdomain.TLD'
    browser.find_by_id('service_api_url').first.value = 'http://yourdomain.TLD'
    browser.find_by_id('service_username').first.value = 'jira_user'
    browser.find_by_id('service_password').first.value = 'jira_pwd'
    browser.find_by_id('service_jira_issue_transition_id').first.value = 'done'
    browser.find_by_text('Test settings and save changes').click()
    #browser.find_by_text('Cancel').click()
