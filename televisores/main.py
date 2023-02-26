from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    marca = Marca("Semsung")
    tv2 = TV(marca, False)

    control = Control()
    control.enlazar(tv2)
    control.setCanal(50)

    print(tv2.getCanal())

    control.turnOn()
    control.canalUp()

    print(tv2.getCanal())

    tv2.setCanal(121)

    print(tv2.getCanal())
