def add(*args):
    x = 0
    for n in args:
        x+=n
    print(x)
# add(1,2,3,4,5,67,8,9,0)

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=22,multiply=22,divide=1)

class Car:
    def __init__(self,**kwargs):
        self.weight = kwargs.get("weight")
        self.speed = kwargs.get("speed")
        self.brand = kwargs.get("brand")
        self.mileage = kwargs.get("mileage")
car = Car(weight=220,speed=220,mileage=220)
print(car.weight)

def yolo(a,*args,**kwargs):
    print(a,args,kwargs)
yolo(4,1,2,3,x=10,y=10)
