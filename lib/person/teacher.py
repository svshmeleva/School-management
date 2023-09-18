from person import Person

class Teacher(Person):
    """
    Class named Teacher, which inherits the properties and methods from the Person class
    """
    def __init__(self, person_id, name, surname, dob, email, phone_num, address, lesson_id_l) -> None:
        super().__init__(person_id, name, surname, dob, email, phone_num, address)
        self._lesson_id_l = lesson_id_l

    @property
    def get_lesson_id_l(self):
        """ Return list of lesson assigned for the lesson"""
        return self._lesson_id_l