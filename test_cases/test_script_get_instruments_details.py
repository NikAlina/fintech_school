#-*-coding: utf8 -*
"""Test to check Investment API"""


def test_script_post(http_client):

    response = http_client.post_subscriptions(request_id='555', system_code='222', siebel_id='A.Kitaeva')

def test_script(http_client):

    response = http_client.get_instruments_details(request_id='555', system_code='222', siebel_id='A.Kitaeva')

    assert response.status_code == 200