# from dataclasses import dataclass

import dataclasses

@dataclasses.dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)



def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, '2024-03-11')
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

if __name__ == "__main__":
    _test_voto()
