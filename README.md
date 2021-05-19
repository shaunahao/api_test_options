# api_test_options
Mimic local with app.py

Mimic staging with app_s.py

## pytest
https://docs.pytest.org/en/6.2.x/index.html

Run Custom Pytest Test:

pytest custom_framework/feature_one/test_login.py -v -s

Run against Staging Env:

pytest custom_framework/feature_one/test_login.py -v -s --env staging

## snapshot
https://pypi.org/project/snapshottest/

Run snapshot Test:

pytest snapshot_test/test_login_snap.py -v -s

Run against Staging Env:

pytest snapshot_test/test_login_snap.py -v -s --env staging
## tavern
https://tavern.readthedocs.io/en/latest/basics.html

Run Tavern Test:

pytest tavern_test/test_login.tavern.yaml -v -s

Run against Staging Env:

pytest tavern_test/test_login.tavern.yaml -v -s --env staging
