#!/usr/bin/env python
#parent class/base class :main class 
#sub_clas:Always contains a parenthesis
from user import User

class Student(User):#inheritance
    knowledge=[]
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        
    def learn(self,a_string):
        self.knowledge.append(a_string)
        

        