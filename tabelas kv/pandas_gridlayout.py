from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from tabela import Tabela

import pandas as pd
import numpy as np


# dados_Ke = np.array([50,1.0, 90,0.897, 95,0.868, 99,0.814,
#                     99.9,0.753, 99.99,0.702, 99.999,0.659,
#                     99.9999,0.620]).reshape(8,2)
# df = pd.DataFrame(dados_Ke, columns='Confiabilidade (%),Fator de confiabilidade Ke'.split(','))

# print(df.shape)
df = pd.read_csv('chavetas_paralelas.csv')

# valores = np.array([1.58,-0.085,4.51,-0.265,57.7,-0.0718,272,-0.995]).reshape(4,2)
# df = pd.DataFrame(valores, columns='a b'.split(),
#                     index='Retificado Usinado/Laminado_a_frio Laminado_a_quente Forjado'.split())
# display(df)

class Manager(ScreenManager):
    pass

class Inicio(Screen):
    pass
class Tela1(Screen):
    def __init__(self, **kwargs):
        super(Tela1, self).__init__(**kwargs)
        self.add_widget(Tabela(df))

class PD_Grid(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    PD_Grid().run()

# tab.clear_widgets()
