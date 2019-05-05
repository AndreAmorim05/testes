from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from tabela import Tabela

import pandas as pd
import numpy as np



valores = np.array([1.58,-0.085,4.51,-0.265,57.7,-0.0718,272,-0.995]).reshape(4,2)
df = pd.DataFrame(valores, columns='a b'.split(),
                    index='Retificado Usinado/Laminado_a_frio Laminado_a_quente Forjado'.split())


class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Inicio(Screen):
    pass
class Tela1(Screen):
    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.pop = None #inicialização importante para usar o dismiss() no TextInput

    def req_tabela(self, *args):
        ids = [self.ids.tex1, self.ids.tex2]
        self.pop = Popup(title='Tabela', content=Tabela(DataFrame=df, ids_list=ids), size_hint=(0.5, 0.5))
        self.pop.open()

class PD_Grid(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    PD_Grid().run()
