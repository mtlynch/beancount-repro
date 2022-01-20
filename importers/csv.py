import datetime

from beancount.core import amount
from beancount.core import data
from beancount.core import number
from beancount.ingest import importer


class CsvImporter(importer.ImporterProtocol):
    def __init__(self, account, lastfour=None, currency='USD'):
        self._account = account
        self._last_four_account_digits = lastfour
        self._currency = currency

    def identify(self, f):
        return f.name.endswith('.csv')

    def file_date(self, _):
        return datetime.date(2021, 12, 1)

    def file_account(self, _):
        return self._account

    def extract(self, f):
        d = data.Transaction(meta=data.new_metadata("dummy", 1),
                             date=datetime.date(2021, 12, 2),
                             flag=self.FLAG,
                             payee='Dummy Payee',
                             narration=None,
                             tags=data.EMPTY_SET,
                             links=data.EMPTY_SET,
                             postings=[
                                 data.Posting(account=self._account,
                                              units=amount.Amount(
                                                  number.D('1868.26'), 'USD'),
                                              cost=None,
                                              price=None,
                                              flag=None,
                                              meta=None),
                                 data.Posting(account='Income:Dummy',
                                              units=None,
                                              cost=None,
                                              price=None,
                                              flag=None,
                                              meta=None)
                             ])
        return [d]
