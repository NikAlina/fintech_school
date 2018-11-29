#-*-coding: utf8 -*
"""Test to check Investment API"""


def test_script(http_client):

    response = http_client.post_subscriptions(request_id='555', system_code='222', instrument_id='AAPL_SPBXM', sec_name='AAPL', sec_type='equity', price_alert=0)

    assert response.status_code == 200