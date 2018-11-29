#-*-coding: utf8 -*
"""Test to check Investment API"""

def test_script_post(http_client):

    response = http_client.post_subscriptions(request_id='555', system_code='222')

def test_script_del(http_client):

    response = http_client.del_subscriptions (request_id='555', system_code='222')

    assert response.status_code == 200