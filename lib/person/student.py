from person import Person

class Student(Person):
    """
    Class named Student, which inherits the properties and methods from the Person class
    """
    def __init__(self, person_id, name, surname, dob, lesson_id_l) -> None:
        super().__init__(person_id=person_id, name=name, surname=surname, dob=dob, email=None, phone_num=None, address=None)
        self._lesson_id_l = lesson_id_l

    @property
    def get_lesson_id_l(self):
        """ Return list of lesson assigned for the lesson"""
        return self._lesson_id_l
        