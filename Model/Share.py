__author__ = 'thiagocastroferreira'

import datetime

class Share(object):
    _id = str
    _name = str
    _price = float
    _variation = float
    _volume = int
    _date = datetime.datetime

    def __init__(self, id, name, price, variation, volume, date):
        super(Share, self).__init__()
        self.id = id
        self.name = name
        self.price = price
        self.variation = variation
        self.volume = volume
        self.date = date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @id.deleter
    def id(self):
        del self._id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

    @property
    def variation(self):
        return self._variation

    @variation.setter
    def variation(self, value):
        self._variation = value

    @variation.deleter
    def variation(self):
        del self._variation

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value

    @volume.deleter
    def volume(self):
        del self._volume

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @date.deleter
    def date(self):
        del self._date