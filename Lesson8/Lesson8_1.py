class Auto(object):
    def __init__(self,brand,age,mark):
        self.brand=brand
        self.age=age
        self.mark=mark
        self.color="black"
        self.weight="до 2 тонн"
        """Constructor"""
    def move(self):
        return "move"
    def stop(self):
        return "stop"
    def birthday(self):
        return self.age+1
    def opisanie(self):
        print(self.move(),'\n'+"модель авто"'\t'+self.brand,'\n'+"сколько лет в эксплуатации",'\t'+
              str(self.birthday()),'\n'+"марка авто"'\t'+self.mark,'\n'+'цвет авто''\t'+self.color,'\n'+
              "вес авто"'\t'+self.weight,'\n'+self.stop())




car2=Auto("polo",5,"WV")
car1=Auto('camry',8,'toyta')
print(car1.opisanie())
print(car2.opisanie())
