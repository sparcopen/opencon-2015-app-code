"""
OpenCon auth models.
"""
import gdata.gauth
import gdata.client
import gdata.spreadsheets.client
import gspread

from django.db import models


class Token(models.Model):
    """
    Store google api token data.
    """
    name = models.TextField(blank=False)
    access_token = models.TextField(blank=False)
    refresh_token = models.TextField(blank=False)
    client_id = models.TextField(blank=False)
    client_secret = models.TextField(blank=False)
    scope = models.TextField(blank=False)

    def initialize(self):
        """
        Return OAuth2Token instance.
        """
        token = gdata.gauth.OAuth2Token(
            client_id=self.client_id,
            client_secret=self.client_secret,
            scope=self.scope,
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            user_agent="OpenCon",
        )

        return token


class Sheet(models.Model):
    """
    Store spreadsheet key.
    """
    name = models.TextField(blank=False)
    key = models.TextField(blank=False)
    token = models.ForeignKey(Token)

    def get_data(self):
        """
        First ensure we have fresh access token then call google api
        retrieve fresh data.
        """
        client = self.token.initialize().authorize(
            gdata.spreadsheets.client.SpreadsheetsClient()
        )
        client.GetSpreadsheets()
        self.token.access_token = client.auth_token.access_token
        self.token.save()

        client = gspread.authorize(self.token.initialize())
        return client.open_by_key(self.key).sheet1.get_all_records()
