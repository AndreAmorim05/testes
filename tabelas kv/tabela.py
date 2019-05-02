from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.metrics import dp



class Tabela(GridLayout):
    def __init__(self, DataFrame, **kwargs):
        super(Tabela, self).__init__(**kwargs)
        self.data = DataFrame
        self.cols = self.tamanho()
        self.spacing = dp(2)
        self.colunas = list(self.data.columns.values)
    
    def tamanho(self):
        Clock.schedule_once(self.adiciona, 0)
        return len(self.data.columns.values)+1

    def adiciona(self, *args):
        '''Para a variável header é importante verificar se é necessário 
        adicionar o espaço em branco,  caso seja fica da forma abaixo,
        criar condição if else da forma, 
        if len(list(columns.values)) == len(quantidade_de_elementos_numa_linha)'''
        header = [' '] + list(self.data.columns.values)
        for h in header:
            self.add_widget(Label(text=str(h)))

        for index, row in self.data.iterrows():
            # self.add_widget(Button(text=str(index), on_release=lambda a:self.pegar_dados(str(index-1))))
            self.add_widget(ButtonStyle(str(index), self))
            for col in list(self.data.columns.values):
                self.add_widget(Label(text=str(row[col])))
    
    def pegar_dados(self, index, *args):
        try:
            print(self.data.loc[index].tolist())
        except:
            print(self.data.loc[float(index)].tolist())
        # return self.data.loc[int(index)].tolist()

class ButtonStyle(ButtonBehavior, Label):
    def __init__(self, tex, ref, **kwargs):
        super(ButtonStyle, self).__init__(**kwargs)
        self.ref = ref
        self.text = tex
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()
    
    def on_state(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba = [0.4, 0.6, 0.7, 1] if self.state == 'normal' else [0.2, 0.3, 0.4, 1]) #if self.state=='normal' else [0.6, .5, .8, 1]
            Rectangle(pos=(self.pos[0], self.pos[1]), size=(self.size[0], self.size[1]))

    def on_release(self, *args):
        self.ref.pegar_dados(self.text)
 