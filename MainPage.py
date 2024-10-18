import Tools
import WindowWidget
import data.des
import tkinter as tk
import data.Data
import TeamPage
import AllTeamPage


class MainPage(WindowWidget.WindowWidget):
    def __init__(self, width, height, name):
        super().__init__(width, height, name)

        self.regionValue = ['北美', '欧洲', '东南亚', '东亚日韩', '南美']
        self.regionIndex = ['southAmerican', 'europe', 'southeastAsia', 'southAsia', 'northAmerican']
        self.titleLabel = self.makeLabel((200, 20, 400, 40), "ALGS冠军赛队伍信息查询")
        self.logoLabel = self.makeLabel((260, 80, 300, 300), 'logoFigure')
        self.abstractLabel = self.makeLabel((20, 400, 760, 80), data.des.general_des)
        self.regionLabel = self.makeLabel((20, 500, 100, 40), '地区')
        self.regionCombobox = self.makeCombobox((140, 500, 100, 40), self.regionValue)
        self.teamLabel = self.makeLabel((260, 500, 100, 40), '队伍')
        self.teamCombobox = self.makeCombobox((380, 500, 160, 40))
        self.selectTeamButton = self.makeButton((560, 500, 100, 40), '选择队伍', self.selectTeamButtonLeftClick)
        self.allTeamButton = self.makeButton((680, 500, 100, 40), '所有队伍', self.allTeamButtonLeftClick)

        self.regionCombobox.bind('<<ComboboxSelected>>', self.regionComboboxSelected)

        self.init()

    def init(self):
        self.dataSheet = data.Data.DataSheet()
        self.data = {'southAmerican': [self.dataSheet.Furia, self.dataSheet.A_Hundred_Thieves, self.dataSheet.SSG,
                                       self.dataSheet.TSM, self.dataSheet.NRG, self.dataSheet.TL, self.dataSheet.C9,
                                       self.dataSheet.OG, self.dataSheet.LG, self.dataSheet.E8],
                     'northAmerican': [self.dataSheet.GODFIRE, self.dataSheet.SNG, self.dataSheet.ODK,
                                       self.dataSheet.INF,
                                       self.dataSheet.Fenix, self.dataSheet.IQ],
                     'europe': [self.dataSheet.GMT, self.dataSheet.Alliance, self.dataSheet.SCARZ, self.dataSheet.AYM,
                                self.dataSheet.ZETA, self.dataSheet.IG, self.dataSheet.ACEND, self.dataSheet.FAK,
                                self.dataSheet.element_6],
                     'southeastAsia': [self.dataSheet.DZ, self.dataSheet.EXO, self.dataSheet.Burger, self.dataSheet.STK,
                                       self.dataSheet.DF, self.dataSheet.BRU],
                     'southAsia': [self.dataSheet.FNC, self.dataSheet.aD, self.dataSheet.PULVEREX, self.dataSheet.RC,
                                   self.dataSheet.ORF, self.dataSheet.FOR7, self.dataSheet.CR, self.dataSheet.DNG,
                                   self.dataSheet.FENNEL]}

        self.teamValue = []
        for i in self.data['southAmerican']:
            self.teamValue.append(i['tname'])
        self.teamCombobox.configure(values=self.teamValue)
        self.teamCombobox.current(0)

        self.logoFigure = Tools.pic2TKpic("logo.jpg", (300, 300))
        self.logoLabel.configure(image=self.logoFigure)

    def regionComboboxSelected(self, *args):
        region = self.regionIndex[self.regionCombobox.current()]
        self.teamValue = []

        for i in range(100):
            self.teamCombobox.delete(0, tk.END)

        for i in self.data[region]:
            self.teamValue.append(i['tname'])

        self.teamCombobox.configure(values=self.teamValue)
        self.teamCombobox.current(0)

    def selectTeamButtonLeftClick(self, *args):
        regionIndex = self.regionCombobox.current()
        teamIndex = self.teamCombobox.current()
        for i in self.data[self.regionIndex[regionIndex]]:
            if i['tname'] == self.teamValue[teamIndex]:
                self.selectValue = i
                break
        teamPage = TeamPage.TeamPage(800, 900, '队伍信息', self.selectValue)
        teamPage.window.mainloop()
        pass

    def allTeamButtonLeftClick(self, *args):
        val = []
        idx = []
        for i in self.data.keys():
            for j in self.data[i]:
                val.append(j)
        for i in val:
            txt = int(i['rank'].replace("st", "").replace("rd", "").replace("nd", "").replace("th", "").split(' ')[0])
            idx.append([txt,i])
        idx.sort()
        allTeamPage = AllTeamPage.AllTeamPage(900, 620, '所有队伍', idx)
        allTeamPage.window.mainloop()
        pass


mainPage = MainPage(800, 600, 'APEX信息查询')
mainPage.window.mainloop()
