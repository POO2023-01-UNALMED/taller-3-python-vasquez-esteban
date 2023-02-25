class TV:
    _numTV = 0
    _numTV += 1

    def __init__(self, marca, estado):
        self._estado = estado
        self._marca = marca

        self._canal = 1
        self._volumen = 1
        self._precio = 500

        self.control = Control(self)

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio

    def setVolumen(self, volumen):
        self._volumen = volumen

    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):
        self._canal = canal

    def getCanal(self):
        return self._canal

    def getNumTV(cls):
        return cls._numTV

    def turnOn(self):
        self._estado = "encendido"

    def turnOff(self):
        self._estado = "apagado"

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._estado == "encendido":
            if self._canal < 120:
                self._canal += 1

    def canalDown(self):
        if self._estado == "apagado":
            if self._canal > 2:
                self._canal -= 1

    def volumenUp(self):
        if self._estado == "encendido":
            if self._volumen < 7:
                self._volumen += 1

    def volumenDown(self):
        if self._estado == "encendido":
            if self._volumen > 1:
                self._volumen -= 1