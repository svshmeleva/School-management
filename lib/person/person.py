
class Person():
    
    def __init__(self, person_id, name, surname, dob, email, phone_num, address) -> None:
        """
        Class presenting a personal information.
        This class is a parent class for child classes: Parent, Student and Teacher
        """
        self._person_id = person_id
        self._name = name
        self._surname = surname
        self._dob = dob
        self._email = email
        self._phone_num = phone_num
        self._address = address

    @property
    def person_id(self):
        """ Return ID """
        return self._person_id

    @person_id.setter
    def person_id(self, val):
        # Don't check here!
        self._person_id = val

    @property
    def get_name(self):
        """ Return name """
        return self._name

    @property
    def get_surname(self):
        """ Return surname """
        return self._surname

    @property
    def get_dob(self):
        """ Return Date of Birth """
        return self._dob

    @property
    def email(self):
        """ Return email """
        return self._email

    @email.setter
    def email(self, val):
        # Check here!
        self._email = val

    @property
    def get_phone_num(self):
        """ Return phone number """
        return self._phone_num

    @property
    def get_address(self):
        """ Return address """
        return self._address