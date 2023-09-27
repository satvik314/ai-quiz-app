

class student:
    def __init__(self):
        self._board=None
        self._std=None
        self._subject=None
        self._lesson=None
        
    #setter methods:
    def set_board(self,board):
        self._board=board
    
    def set_std(self,std):
        self._std=std

    def set_subject(self,subject):
        self._subject=subject

    def set_lesson(self,lesson):
        self._lesson=lesson

    #getter methods
    def get_board(self):
        return self._board
    
    def get_std(self):
        return self._std

    def get_subject(self):
        return self._subject
    
    def get_lesson(self):
        return self._lesson
