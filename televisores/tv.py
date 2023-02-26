from televisores.control import Control


class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self.estado = estado
        self._marca = marca

        self._canal = 1
        self._volumen = 1
        self._precio = 500

        self.control = Control()
        TV._numTV += 1

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

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
        if 0 <= volumen <= 7:
            self._volumen = volumen

    def getVolumen(self):
        return self._volumen

    def setCanal(self, canal):
        if 1 <= canal <= 120:
            self._canal = canal

    def getCanal(self):
        return self._canal

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.estado:
            if self._canal < 120:
                self._canal += 1

    def canalDown(self):
        if self.estado:
            if self._canal > 2:
                self._canal -= 1

    def volumenUp(self):
        if self.estado:
            if self._volumen < 7:
                self._volumen += 1

    def volumenDown(self):
        if self.estado:
            if self._volumen > 1:
                self._volumen -= 1