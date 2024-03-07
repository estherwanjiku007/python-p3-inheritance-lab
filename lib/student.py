#!/usr/bin/env python

from user import User
knowledge=[]
class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
    def learn(self,a_string):
        knowledge.append(a_string)
        self.knowledge=knowledge

        