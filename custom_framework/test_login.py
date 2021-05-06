import pytest

def test_success_login(re, url):
    r = re.post(
        url = url,
        json = {"username":"admin", "password":"abc123", "age":18, "sex":"F"}
    )
    assert r.status_code == 200
    assert r.json() == {"username":"admin", "password":"abc123", "age":18, "sex":"F"}

@pytest.mark.smoke
def test_login_wrong_sex(re, url):
    r = re.post(
        url = url,
        json = {"username":"admin", "password":"abc123", "age":18, "sex":"X"}
    )
    assert r.status_code == 400
    assert r.json() == {'message': {'sex': 'sex is wrong'}}

def test_login_wrong_name(re, url):
    r = re.post(
        url = url,
        json = {"password":"abc123", "age":18, "sex":"F"}
    )
    assert r.status_code == 400
    assert r.json() == {'message': {'username': 'username is wrong'}}
