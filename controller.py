from view import View
from voto import Libretto, Voto
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Libretto()
        self.startupLibretto()

    def handleAdd(self,e):
        pass

    def handlePrint(self,e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))
        self._view.update()



    def startupLibretto(self):
        self._model.append(Voto("Fisica I", 10, 25, False, '2022-07-12'))
        self._model.append(Voto("Analisi II", 8, 30, True, '2023-02-15'))
        self._model.append(Voto("Analisi 1", 10, 18,False, '2020-01-01'))
        self._model.append(Voto("Chimica", 8, 30,False, '2020-01-02'))
        self._model.append(Voto("Informatica", 8, 30,True, '2020-01-03'))
        self._model.append(Voto("Algebra Lineare", 10, 24,False, '2020-06-01'))
        self._model.append(Voto("Fisica 1", 10, 21,False, '2020-06-02'))