# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""barcode.isxn

This module provides some special codes, which are no standalone barcodes.
All codes where transformed to EAN-13 barcodes. In every case, the checksum
is new calculated.

Example::

    >>> from barcode import get_barcode
    >>> ISBN = get_barcode('isbn10')
    >>> isbn = ISBN('0132354187')
    >>> unicode(isbn)
    u'0132354187'
    >>> isbn.get_fullcode()
    u'9780132354189'
    >>> # Test with wrong checksum
    >>> isbn = ISBN('0132354180')
    >>> unicode(isbn)
    u'0132354187'

"""
__docformat__ = 'restructuredtext en'

from barcode.ean import EuropeanArticleNumber13
from barcode.errors import *


class InternationalStandardBookNumber13(EuropeanArticleNumber13):

    name = 'ISBN-13'

    def __init__(self, isbn, writer=None):
        isbn = isbn.replace('-', '')
        self.isbn13 = isbn
        if isbn[:3] not in ('978', '979'):
            raise WrongCountryCodeError('ISBN must start with 978 or 979.')
        EuropeanArticleNumber13.__init__(self, isbn, writer)


class InternationalStandardBookNumber10(InternationalStandardBookNumber13):

    name = 'ISBN-10'

    digits = 9

    def __init__(self, isbn, writer=None):
        isbn = isbn.replace('-', '')
        isbn = isbn[:self.digits]
        self.isbn10 = isbn
        self.isbn10 = '{0}{1}'.format(isbn, self._calculate_checksum())
        InternationalStandardBookNumber13.__init__(self, '978'+isbn, writer)

    def _calculate_checksum(self):
        tmp = sum([x*int(y) for x, y in enumerate(self.isbn10[:9],
                                                  start=1)]) % 11
        if tmp == 10:
            return 'X'
        else:
            return tmp

    def __unicode__(self):
        return self.isbn10


class InternationalStandardSerialNumber(EuropeanArticleNumber13):

    name = 'ISSN'

    digits = 7

    def __init__(self, issn, writer=None):
        issn = issn.replace('-', '')
        issn = issn[:self.digits]
        self.issn = issn
        self.issn = '{0}{1}'.format(issn, self._calculate_checksum())
        EuropeanArticleNumber13.__init__(self, self.make_ean(), writer)

    def _calculate_checksum(self):
        tmp = 11 - sum([x*int(y) for x, y in enumerate(reversed(self.issn[:7]),
                                                       start=2)]) % 11
        if tmp == 10:
            return 'X'
        else:
            return tmp

    def make_ean(self):
        return '977{0}00{1}'.format(self.issn[:7], self._calculate_checksum())

    def __unicode__(self):
        return self.issn


# Shortcuts
ISBN13 = InternationalStandardBookNumber13
ISBN10 = InternationalStandardBookNumber10
ISSN = InternationalStandardSerialNumber
