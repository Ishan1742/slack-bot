from wave import *

def test_load_env_variable():
    assert load_env_variable() is True

def test_get_slack_signing_secret():
    assert get_slack_signing_secret() is not None

def test_create_slack_events():
    assert create_slack_events() is not None

def test_get_slack_bot_token():
    assert get_slack_bot_token() is not None

def test_get_slack_client():
    assert get_slack_client() is not None

def test_get_user_id():
    assert get_user_id("ishanghosh1999") == "U012Q55UNAG"