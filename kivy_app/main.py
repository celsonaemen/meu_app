from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ApresentacaoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        texto = (
            "Bem-vindo ao ExitPoint!\n\n"
            "Já dormiu no ônibus e perdeu o ponto? Nunca mais!\n\n"
            "Com o ExitPoint, você:\n"
            "- Escolhe o ponto de desembarque no mapa\n"
            "- Configura um alarme para tocar antes de chegar\n"
            "- Dorme tranquilo durante a viagem\n\n"
            "Seu despertador de viagem chegou. Bora usar?"
        )

        label = Label(text=texto, halign="center", valign="middle", font_size='18sp')
        label.bind(size=label.setter('text_size'))

        botao = Button(text="Começar", size_hint=(1, 0.2), font_size='20sp')
        botao.bind(on_press=self.ir_para_proxima)

        layout.add_widget(label)
        layout.add_widget(botao)

        self.add_widget(layout)

    def ir_para_proxima(self, instance):
        # Aqui vai pra próxima tela (por enquanto só printa no console)
        print("Botão pressionado! Aqui vai pra tela do mapa ou configurações.")

class ExitPointApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ApresentacaoScreen(name='apresentacao'))
        return sm

if __name__ == '__main__':
    ExitPointApp().run()
