import WindowWidget
import data.des
import tkinter as tk
import data.Data
import TeamPage


class AllTeamPage(WindowWidget.WindowWidget):
    def __init__(self, width, height, name, _data):
        super().__init__(width, height, name)
        self.data = _data

        self.label = []
        cnt = 0
        for i in range(10):
            for j in range(4):
                self.label.append(self.makeLabel((20 + j * 220, 20 + i * 60, 200, 40),
                                                 f"{self.data[cnt][1]['tname']}\n{self.data[cnt][1]['rank']}",
                                                 command=self.labelLeftClick))
                cnt += 1

    def labelLeftClick(self, event):
        team = event.widget['text'].split('\n')[0]
        for i in self.data:
            if i[1]['tname'] == team:
                self.selectValue = i[1]
                break
        teamPage = TeamPage.TeamPage(800, 900, '队伍信息', self.selectValue)
        teamPage.window.mainloop()
