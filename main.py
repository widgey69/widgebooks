# import kivy
# from kivy.app import App
from kivymd.app import MDApp
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.widget import Widget
# from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from datetime import date, time
from kivy.core.window import Window
# from kivymd.uix.datatables import MDDataTable
# from kivy.metrics import dp
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
# from kivy.factory import Factory
# from kivy.effects.opacityscroll import OpacityScrollEffect
from kivy.uix.camera import Camera
import csv
import pandas


def load_data():
    df = pandas.read_csv('report.csv')
    df = df.set_index('date')
    df.sort_index(axis=0, inplace=True)
    return df


Window.softinput_mode = "below_target"
today = date.today()
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']


class WindowManager(ScreenManager):
    pass


class Income(Screen):
    income = ObjectProperty(None)
    reference = ObjectProperty(None)

    def submit(self):
        try:
            value = float(self.income.text)
            value = format(value, '.2f')
            self.income.text = str(value)
        except ValueError:
            self.income.text = 'please enter a number'
            return
        else:
            for num in self.income.text:
                if num not in numbers:
                    self.income.text = 'please enter a number'
                    break
            else:
                with open('report.csv', mode='a') as f:
                    update = csv.writer(f, delimiter=',')
                    update.writerow([today, self.income.text, 0, 0, self.reference.text])
                    self.income.text = ''
                    self.reference.text = ''


class Expense(Screen):
    expense = ObjectProperty(None)
    referenceex = ObjectProperty(None)

    def submit(self):
        try:
            value = float(self.expense.text)
            value = format(value, '.2f')
            self.expense.text = str(value)
        except ValueError:
            self.expense.text = 'please enter a number'
            return
        else:
            for num in value:
                if num not in numbers:
                    self.expense.text = 'please enter a number'
                    break
            else:
                with open('report.csv', mode='a') as f:
                    update = csv.writer(f, delimiter=',')
                    update.writerow([today, 0, self.expense.text, 0, self.referenceex.text])
                self.expense.text = ''
                self.referenceex.text = ''


class Total(Screen):
    gross_total = StringProperty()
    net_total = StringProperty()

    def __init__(self, **kwargs):
        super(Total, self).__init__(**kwargs)

    def calculate(self):
        with open('report.csv', 'r') as f:
            f.readline()
            total = 0
            net_total = 0
            try:
                for row in f:
                    vals = row.strip('\n')
                    vals = vals.split(',')
                    total += float(vals[1])
                    net_total += float(vals[1]) - float(vals[2])
                self.gross_total = '£ ' + str(round(total, 2))
                self.net_total = '£ ' + str(round(net_total, 2))
            except IndexError:
                self.gross_total = ''
                self.net_total = 'something went wrong'


class History(Screen):

    @staticmethod
    def january():

        pops = JanPop()
        pops.open()

    @staticmethod
    def february():

        pops = FebPop()
        pops.open()

    @staticmethod
    def march():
        pops = MarchPop()
        pops.open()

    @staticmethod
    def april():
        pops = AprilPop()
        pops.open()

    @staticmethod
    def may():
        pops = MayPop()
        pops.open()

    @staticmethod
    def june():
        pops = JunePop()
        pops.open()

    @staticmethod
    def july():
        pops = JulyPop()
        pops.open()

    @staticmethod
    def august():
        pops = AugustPop()
        pops.open()

    @staticmethod
    def september():
        pops = SeptemberPop()
        pops.open()

    @staticmethod
    def october():
        pops = OctoberPop()
        pops.open()

    @staticmethod
    def november():
        pops = NovemberPop()
        pops.open()

    @staticmethod
    def december():
        pops = DecemberPop()
        pops.open()


class JanPop(Popup):
    data = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        jan = load_data()
        jan = jan.loc["2021-01-01":"2021-01-31"]
        if jan.empty:
            self.data = 'Nothing to display'
        else:
            jan = jan.to_string(col_space=20, justify='end')
            self.data = jan


class FebPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        feb = load_data()
        feb = feb.loc["2021-02-01":"2021-02-31"]
        if feb.empty:
            self.data = 'Nothing to display'
        else:
            feb = feb.to_string(col_space=20, justify='end')
            self.data = feb


class MarchPop(Popup):
    data = StringProperty()

    def __init__(self,):
        super().__init__()
        mdf = load_data()
        march = mdf.loc["2021-03-01":"2021-03-31"]
        if march.empty:
            self.data = 'Nothing to display'
        else:
            march = march.to_string(col_space=20, justify='end')
            self.data = march


class AprilPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        april = load_data()
        april = april.loc["2021-04-01":"2021-04-31"]
        if april.empty:
            self.data = 'Nothing to display'
        else:
            april = april.to_string(col_space=20, justify='end')
            self.data = april


class MayPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        may = load_data()
        may = may.loc["2021-05-01":"2021-05-31"]
        if may.empty:
            self.data = 'Nothing to display'
        else:

            may = may.to_string(col_space=20, justify='end')
            self.data = may


class JunePop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        june = load_data()
        june = june.loc["2021-06-01":"2021-06-31"]
        if june.empty:
            self.data = 'Nothing to display'
        else:
            june = june.to_string(col_space=20, justify='end')
            self.data = june


class JulyPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        july = load_data()
        july = july.loc["2021-07-01":"2021-07-31"]
        if july.empty:
            self.data = 'Nothing to display'
        else:
            july = july.to_string(col_space=20, justify='end')
            self.data = july


class AugustPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        august = load_data()
        august = august.loc["2021-08-01":"2021-08-31"]
        if august.empty:
            self.data = 'Nothing to display'
        else:
            august = august.to_string(col_space=20, justify='end')
            self.data = august


class SeptemberPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        september = load_data()
        september = september.loc["2021-09-01":"2021-09-31"]
        if september.empty:
            self.data = 'Nothing to display'
        else:
            september = september.to_string(col_space=20, justify='end')
            self.data = september


class OctoberPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        october = load_data()
        october = october.loc["2021-10-01":"2021-10-31"]
        if october.empty:
            self.data = 'Nothing to display'
        else:
            october = october.to_string(col_space=20, justify='end')
            self.data = october


class NovemberPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        november = load_data()
        november = november.loc["2021-11-01":"2021-11-31"]
        if november.empty:
            self.data = 'Nothing to display'
        else:
            november = november.to_string(col_space=20, justify='end')
            self.data = november


class DecemberPop(Popup):
    data = StringProperty()

    def __init__(self):
        super().__init__()
        december = load_data()
        december = december.loc["2021-12-01":"2021-12-31"]
        if december.empty:
            self.data = 'Nothing to display'
        else:
            december = december.to_string(col_space=20, justify='end')
            self.data = december


class Records(Screen):
    def capture(self):

        timestr = today
        self.export_to_png('IMG_{}.png'.format(timestr))

class MyMainApp(MDApp):
    def build(self):
        return


if __name__ == '__main__':
    MyMainApp().run()
