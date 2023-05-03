class Drank:
    def __init__(self, naam, temp = '20'):
        self.naam = naam
        self.temp = temp

class LogFile:
    def __init__(self, bestandsnaam):
        self.bestand = open(bestandsnaam, 'w')
    def log(self, tektst):
        self.bestand.write(tektst + '/n')
    def close(self):
        self.bestand.close




water = Drank("water", '6')
cola = Drank("cola", '6')
koffie = Drank("koffie", '70')

print(f"{water.naam} is {water.temp} graden celcius")
print(f"{cola.naam} is {cola.temp} graden celcius")
print(f"{koffie.naam} is {koffie.temp} graden celcius")