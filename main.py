"""
Il main viene utilizzato per far comunicare view e controller
"""
import flet as ft

from UI.controller import Controller
from UI.view import View
from modello.voto import Libretto

def main(page: ft.Page):
    v = View(page)
    lb = Libretto()
    c = Controller(v, lb)   # gli metto view come argomento così potranno comunicare e lo metto come variabile di classe
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
