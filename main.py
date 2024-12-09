import requests.cookies
import pytest
import requests
import requests.utils
import json


@pytest.fixture
def cred():
    kpi_domain = 'https://demo.kpi-check.online'
    login = 'demo'
    password = 'demo'
    return {"kpi_domain": kpi_domain, "login": login, "password": password}


@pytest.fixture
def login():
    def _login(kpi_domain, login, password):
        url = f'{kpi_domain}/_api/auth/login'
        payload = {
            'login': login, 'password': password
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        session = requests.Session()
        resp = session.post(url, data=payload, headers=headers)
        assert resp.status_code == 200
        # jsonData = resp.json()
        # assert jsonData['status'] == 0
        cookies = session.cookies
        return cookies

    return _login


def test_login(cred, login):
    print('\n Вход в программу: ')
    kpi_domain = cred["kpi_domain"]
    logins = cred["login"]
    password = cred["password"]
    cookies = login(kpi_domain, logins, password)


def test_getmo(cred, login):
    print('\n Получено более 1 ОУ: ')
    kpi_domain = cred["kpi_domain"]
    logins = cred["login"]
    password = cred["password"]
    cookies = login(kpi_domain, logins, password)
    url = f'{kpi_domain}/_api/mo/get_mo'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    session = requests.Session()
    resp = session.post(url, headers=headers, cookies=cookies)
    jsonData = resp.json()
    assert jsonData['DATA']['rows_count'] > 1 and resp.status_code == 200
    print(' Количество ОУ: ' + str(jsonData['DATA']['rows_count']))
    print(' статус: ' + str(jsonData['DATA']['rows_count']))

def test_get_layout(cred, login):
    print('\n Проверяем возвращается ли layout: ')
    kpi_domain = cred["kpi_domain"]
    logins = cred["login"]
    password = cred["password"]
    cookies = login(kpi_domain, logins, password)
    url = f'{kpi_domain}/_api/layout'
    payload = {
        'id': 1
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    session = requests.Session()
    resp = session.post(url, headers=headers, cookies=cookies)
    jsonData = resp.json()
    assert resp.status_code == 200
    print(' статус: ' + str(resp.status_code))
