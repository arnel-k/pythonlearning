from src import Address
class Contact(Address):
    def __init__(self, fname, lname, street, zipcode, city):
        self._fname = fname
        self._lname = lname
        super().__init__(street, zipcode, city)
        
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, value):
        self._fname = value

    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, value):
        self._lname = value