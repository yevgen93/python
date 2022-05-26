import os
from venmo_api import Client, PaymentPrivacy

class Venmo:
    def __init__(self, access_token):
        self.client = Client(access_token=access_token)

    def get_user_id_by_username(self, username):
        user = self.client.user.get_user_by_username(username=username)
        if (user):
            return user.id
        else:
            print("ERROR: user did not comeback. Check username.")
            return None

    def request_money(self, id, amount, description, callback = None):
        # Returns a boolean: true if successfully requested
        return self.client.payment.request_money(amount, description, id, PaymentPrivacy.PUBLIC, None, callback)
