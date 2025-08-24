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
