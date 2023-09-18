class Lesson():
    """
    Class presenting an information about current lesson.
    """
    def __init__(self, lesson_id, subject, teacher, assistant, time, room, stud_id_l) -> None:
        self._lesson_id = lesson_id
        self._subject = subject
        self._teacher = teacher
        self._assistant = assistant
        self._time = time
        self._room = room
        self._stud_id_l = stud_id_l

    @property
    def lesson_id(self):
        """ Return id """
        return self._lesson_id

    @property
    def get_sunject(self):
        """ Return subject """
        return self._subject

    @property
    def get_teacher(self):
        """ Return teacher """
        return self._teacher

    @property
    def get_assistant(self):
        """ Return assistant """
        return self._assistant

    @property
    def get_time(self):
        """ Return time """
        return self._time

    @property
    def get_room(self):
        """ Return room """
        return self._room

    @property
    def get_stud_id_l(self):
        """ Return list of students assigned for the lesson"""
        return self._stud_id_l