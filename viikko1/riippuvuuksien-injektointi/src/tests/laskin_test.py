import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):

    def setUp(self):
        io = StubIO(["5", "6", "5", "7"])
        self.laskin = Laskin(io)
    
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()
        self.assertEqual(io.outputs[0], "Summa: 4")
    
    def test_kaksi(self):
        ino = StubIO([2, 5, 6, 7, -9999])
        laskin = Laskin(ino)
        outputs = ("Summa: 7", "Summa: 13")
        laskin.suorita()
        self.assertEqual((ino.outputs[0], ino.outputs[1]), outputs)
   