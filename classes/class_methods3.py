class CarModel:
    def __new__(cls, model):
        if model == 1998:
            return Model1998()
        else:
            return NotModel1998()


class Model1998:
    def __init__(self):
        print("1998 model")


class NotModel1998:
    def __init__(self):
        print("not 1998 model")


car1 = CarModel(model=1992)
car2 = CarModel(model=1993)
