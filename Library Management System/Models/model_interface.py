from abc import abstractclassmethod, ABC
from datetime import datetime
from constants.constant import UserState, BookState
import uuid


class IModel(ABC):
    
    def __init__(self):
        # Contatins a list of all entries, objects
        self.all = []

    @abstractclassmethod
    def insert_and_create(self, entry):
        if entry in self.all:
            return
        self.all.append(entry)

    @abstractclassmethod
    def get(self, **kwargs):
        result_list = []
        try:
            for model in self.all:
                flag = True
                for key in kwargs:
                    if getattr(model,key) != kwargs.get(key):
                        flag = False                                              
                        break
                if flag:
                    return model
        except:
            print("Something went wrong while geting a model")
            return

    @abstractclassmethod
    def filter(self, **kwargs):
        result_list = []
        try:
            for model in self.all:
                flag = True
                for key in kwargs:
                    if getattr(model,key) != kwargs.get(key):
                        flag = False                                              
                        break
                if flag:
                    result_list.append(model)
            return result_list
        except:
            print("Something went wrong while filterting")
    
    @abstractclassmethod
    def remove(self, **kwargs):
        try:
            for model in self.all:
                flag = True
                for key in kwargs:
                    if getattr(model,key) != kwargs.get(key):
                        flag = False
                        break
                if flag:
                    self.all.remove(model)
        except:
            print("Something went wrong while removing")

    @abstractclassmethod
    def update(self, query_dict, update_dict):
        try:
            for model in self.all:
                flag = True
                for key in query_dict:
                    if getattr(model,key) != query_dict.get(key):
                        flag = False
                        break
                if flag:
                    for key in update_dict:
                        setattr(model, key,update_dict.get(key))
        except:
            print("something went wrong while updating")
