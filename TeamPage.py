import WindowWidget
import Tools
import tkinter as tk


class TeamPage(WindowWidget.WindowWidget):
    def __init__(self, width, height, name, data):
        super().__init__(width, height, name, isTopLevel=True)
        self.data = data

        self.teamLabel = self.makeLabel((20, 20, 760, 40), data['tname'])
        self.logoLabel = self.makeLabel((300, 80, 200, 200))

        self.member1Label = self.makeLabel((20, 300, 200, 40), data['player1'])
        self.member2Label = self.makeLabel((300, 300, 200, 40), data['player2'])
        self.member3Label = self.makeLabel((560, 300, 200, 40), data['player3'])

        self.abstractText = self.makeText((20, 360, 760, 80), data['describe'])
        self.abstractText.configure(state=tk.DISABLED)

        self.memberLabel = self.makeLabel((100, 460, 600, 400))

        self.init()

    def init(self):
        self.logoFigure = Tools.pic2TKpic(f"./data/{self.data['logoFigure']}", (200, 200))
        self.logoLabel.configure(image=self.logoFigure)
        self.memberFigure = Tools.pic2TKpic(f"./data/{self.data['roster']}", (600, 400))
        self.memberLabel.configure(image=self.memberFigure)
