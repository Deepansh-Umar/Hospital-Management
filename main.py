class Patient:
    def __init__(self,pid,name,age,illness):
        self.pid=pid
        self.name=name
        self.age=age
        self.illness=illness
    def __str__(self):
        return f"{self.pid} - {self.name} ({self.age}) : {self.illness}"
