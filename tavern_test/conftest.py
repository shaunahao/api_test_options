from pytest import fixture
from config import Config
import time

def pytest_addoption(parser):
    parser.addoption(
        '--env', 
        action='store',
        default='local',
        help='Environment to run tests against'
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')

@fixture(scope='session', autouse=True)
def url(env):
    url = Config(env).base_url
    return url

@fixture(scope='function', autouse=True)
def logging(url):
    print('\n', url)
    print('Test starts', time.time())
    yield
    print('\nTest ends', time.time())
