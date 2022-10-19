class edificio:
    def __init__(self,p1,p2,p3,p4,p5):
        self.p1=p1
        self.p2=p2
        self.p3=p3
        self.p4=p4
        self.p5=p5

E=edificio("Sótano","Lavandería","Cocina","Dormitorios","Azotea")

print(E.p5)
print(E.p4)
print(E.p3)
print(E.p2)
print(E.p1)