import pytest
# pip install snapshottest

testdata = [
    {"username":"admin", "password":"abc123", "age":18, "sex":"F"},
    {"password":"abc123", "age":18, "sex":"F"},
    {"username":"admin", "password":"abc123", "age":18, "sex":"X"}
]

@pytest.mark.parametrize('data', testdata)
def test_login_post(re, url, data, snapshot):
    my_api_response = re.post(url, json=data).json()
    snapshot.assert_match(my_api_response)


# def test_login_post(re, url, snapshot):
#     data = {"username":"admin", "password":"abc123", "age":18, "sex":"F"}
#     my_api_response = re.post(url, json=data).json()
#     snapshot.assert_match(my_api_response)

# def test_login_post_no_username(re, url, snapshot):
#     data = {"password":"abc123", "age":18, "sex":"F"}
#     my_api_response = re.post(url, json=data).json()
#     snapshot.assert_match(my_api_response)

# def test_login_post_wrong_sex(re, url, snapshot):
#     data = {"username":"admin", "password":"abc123", "age":18, "sex":"X"}
#     my_api_response = re.post(url, json=data).json()
#     snapshot.assert_match(my_api_response)
