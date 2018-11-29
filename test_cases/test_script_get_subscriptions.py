#-*-coding: utf8 -*
"""Test to check Investment API"""


def test_script(http_client):

    response = http_client.get_subscriptions(request_id='555', system_code='222')

    assert response.status_code == 200