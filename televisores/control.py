class Control:
    def __init__(self):
        self.tv = None

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, canal):
        if self.tv.estado:
            self.tv.setCanal(canal)

    def enlazar(self, tv):
        self.tv = tv
        tv.control = self

    def setTV(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv
