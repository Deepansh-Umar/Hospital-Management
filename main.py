from collections import deque

class Patient:
    def __init__(self,pid,name,age,illness):
        self.pid=pid
        self.name=name
        self.age=age
        self.illness=illness
    def __str__(self):
        return f"{self.pid} - {self.name} ({self.age}) : {self.illness}"


class Doctor:
    def __init__(self,did,name,spec):
        self.did= did
        self.name =name
        self.spec=spec
    def __str__(self):
        return f"{self.did} - Dr. {self.name} ({self.spec})"
class Appointment:
    def __init__(self,pat,doc):
        self.pat=pat
        self.doc=doc
    def __str__(self):
        return f"{self.pat.name} : Dr. {self.doc.name}"

class Hospital:
    def __init__(self):
        self.patients={}
        self.doctors={}
        self.appointments=deque()
    def add_patient(self,pid,name,age,ill):
        if pid in self.patients:
            print("ID exists")
            return
        self.patients[pid]=Patient(pid,name,age,ill)
        print("Added the pateint.")
