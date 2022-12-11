import uuid
from abc import abstractclassmethod, ABC
from datetime import datetime

from constants.constant import UserState, BookState
from Models.model_interface import IModel



class UserModel(IModel):

    def __init__(self):
        super().__init__()


class LibrarianModel(IModel):

    def __init__(self):
        super().__init__()


class RackModel(IModel):

    def __init__(self):
        super().__init__()


class BookModel(IModel):

    def __init__(self):
        super().__init__()


class LibraryCardModel(IModel):

    def __init__(self):
        super().__init__()
