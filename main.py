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

    def book(self,pid,did):
        if pid not in self.patients or did not in self.doctors:
            print("Not found")
            return
        a=Appointment(self.patients[pid],self.doctors[did])
        self.appointments.append(a)
        print("Booked.")
    def view_apps(self):
        if not self.appointments:
            print("none")
            return
        for a in self.appointments:
            print(a)


##driver code
h=Hospital()

while 1:
    print("1.Add Patient 2.Add Doctor 3.Book 4.Show 5.Exit")
    c=input(">> ")
    if c=='1':
        pid=input("pid: ")
        name=input("name: ")
        age=input("age: ")
        ill=input("illness: ")
        h.add_patient(pid,name,age,ill)
    elif c=='2':
        did=input("did: ")
        name=input("name: ")
        spec=input("spec: ")
        h.add_doctor(did,name,spec)
    elif c=='3':
        pid=input("patient id: ")
        did=input("doctor id: ")
        h.book(pid,did)
    elif c=='4':
        h.view_apps()
    elif c=='5':
        break
    else:
        print("???")
