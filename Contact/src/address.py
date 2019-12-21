class Address:
    def __init__(self, street, zipcode, city):
        self._street = street
        self._zipcode = zipcode
        self._city = city
    
    @property
    def street(self):
        return self._street
    @street.setter
    def street(self, value):
        self._street = value

    @property
    def zipcode(self):
        return self._zipcode
    @zipcode.setter
    def zipcode(self, value):
        self._zipcode = value
    
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value