"""
Il main viene utilizzato per far comunicare view e controller
"""
import flet as ft

from controller import Controller
from view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)   # gli metto view come argomento così potranno comunicare e lo metto come variabile di classe
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)
