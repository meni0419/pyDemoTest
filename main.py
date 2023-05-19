import requests.cookies
import pytest
import requests
<<<<<<< HEAD
=======
import json
>>>>>>> parent of adb90d1 (comment json (for test commit mac and win10))
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
    print('Тест вход в программу:')
    kpi_domain = cred["kpi_domain"]
    logins = cred["login"]
    password = cred["password"]
    cookies = login(kpi_domain, logins, password)
    print(cookies)
