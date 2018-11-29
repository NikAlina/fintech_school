"""Module with class to work with HTTP client"""

import requests
import json


class HttpClient(object):
    """Class to work with HTTP requests."""

    def __init__(self):
        self.base_url = 'https://fintech-trading-qa.tinkoff.ru/v1/mb/'
        self.headers = {'Authorization':'Basic ZmludGVjaDoxcTJ3M2Uh'}
        self.siebel_id = 'A.Kitaeva'

    def get_instruments(self, request_id, system_code):

        url_get_instruments = self.base_url + 'exchanges/moex/instruments?request_id=' + request_id + '&system_code=' + system_code
        response = requests.get(url_get_instruments, headers=self.headers)

        return response

    def get_subscriptions(self, request_id, system_code):

        url_get_subscriptions = self.base_url + 'contacts/525/subscriptions?request_id=' + request_id + '&system_code=' + system_code
        response = requests.get(url_get_subscriptions, headers=self.headers)

        return response

    def post_subscriptions(self, request_id, system_code,  instrument_id, sec_name, sec_type, price_alert):

        url_post_subscriptions = self.base_url + 'contacts/' + self.siebel_id + '/subscriptions?request_id=' + request_id + '&system_code=' + system_code
        data = {'body': [{'instrument_id': instrument_id,'sec_name': sec_name,'sec_type': sec_type,'price_alert': price_alert}]}
        response = requests.post(url_post_subscriptions, json.dumps(data), headers=self.headers)

        return response

    def del_subscriptions(self, request_id, system_code):

        url_del_subscriptions = self.base_url + 'contacts/' + self.siebel_id + '/subscriptions/0x039D7730?request_id=' + request_id + '&system_code=' + system_code
        response = requests.delete(url_del_subscriptions, headers=self.headers)

        return response

    def get_instruments_details(self, request_id, system_code):

        url_del_subscriptions = self.base_url + 'contacts/' + self.siebel_id + '/subscriptions/0x039D7730?request_id=' + request_id + '&system_code=' + system_code
        response = requests.delete(url_del_subscriptions, headers=self.headers)

        return response