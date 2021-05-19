# api_test_options
Mimic local with app.py
Mimic staging with app_s.py

Run Tavern Test:
pytest custom_framework/feature_one/test_login.py -v -s

Run Tavern Test:
pytest snapshot_test/test_login_snap.py -v -s

Run Tavern Test:
pytest tavern_test/test_login.tavern.yaml -v -s

Run Staging Env:
pytest {testpath} -v -s --env staging
