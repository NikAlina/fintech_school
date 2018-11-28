#-*-coding: utf8 -*
"""Test to check Investment API"""


def test_script(http_client):
    """
        1.Send request to receive the list of instruments.
        2.Check response status code is 200.
    """

    response = http_client.get_instruments_details(request_id='555', system_code='222')

    assert response.status_code == 200