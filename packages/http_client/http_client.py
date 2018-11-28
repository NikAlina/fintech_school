"""Module with class to work with HTTP client"""

import requests
import json


class HttpClient(object):
    """Class to work with HTTP requests."""

    def __init__(self):
        self.base_url = 'https://fintech-trading-qa.tinkoff.ru/v1/mb/'
        self.headers = {'Authorization':'Basic ZmludGVjaDoxcTJ3M2Uh'}

    def get_instruments(self, request_id, system_code):


        url_get_instruments = self.base_url + 'exchanges/moex/instruments?request_id=' + request_id + '&system_code=' + system_code

        response = requests.get(url_get_instruments, headers=self.headers)

        return response

    def get_subscriptions(self, request_id, system_code):

        url_get_subscriptions = self.base_url + 'contacts/525/subscriptions?request_id=' + request_id + '&system_code=' + system_code

        response = requests.get(url_get_subscriptions, headers=self.headers)

        return response

    def post_subscriptions(self, request_id, system_code):


        url_post_subscriptions = self.base_url + 'contacts/a.kitaeva/subscriptions?request_id=' + request_id + '&system_code=' + system_code

        response = requests.post(url_post_subscriptions, json.dumps({"instrument_id":"AAPL_SPBXM","sec_name":"AAPL","sec_type":"equity","price_alert":0}), headers=headers)

        return response

    def del_subscriptions(self, request_id, system_code):
        headers = {'Authorization': 'Basic ZmludGVjaDoxcTJ3M2Uh'}
        url_del_subscriptions = self.base_url + 'contacts/a.kitaeva/subscriptions/0x039D7730?request_id=' + request_id + '&system_code=' + system_code

        response = requests.delete(url_del_subscriptions, headers=self.headers)

        return response

    def get_instruments_details(self, request_id, system_code):


        url_del_subscriptions = self.base_url + 'contacts/a.kitaeva/subscriptions/0x039D7730?request_id=' + request_id + '&system_code=' + system_code

        response = requests.delete(url_del_subscriptions, headers=self.headers)

        return response