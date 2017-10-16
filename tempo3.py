# BPM:Beats Per Minute。1分間あたりの四分音符数
# 小節:bar
# 拍子:Metre
class TimeBase:
    def __init__(self):
        self.__BPM = 120
        self.__BPM_BASE = 4 # 4部音符
        self.__metre = (4, 4) # 4/4拍子
        self.__spb = None
        self.__sec_per_bar()
    
    @property
    def BPM(self): return self.__BPM
    @BPM.setter
    def BPM(self, value):
        if 0 < value and isinstance(value, int):
            self.__BPM = value
            self.__sec_per_bar()

    @property
    def Metre(self): return self.__metre
    @Metre.setter
    def Metre(self, value):
        if isinstance(value, (tuple, list)) and 2 == len(value):
            if isinstance(value[0], int) and isinstance(value[1], int):
                self.__metre = value
                self.__sec_per_bar()
    
    @property
    def SecPerBar(self): return self.__spb
    
    # n小節/1分間
    def __bar_per_minute(self):
        BarPerMinute = self.BPM / (self.Metre[0] * (self.Metre[1] / self.__BPM_BASE))
#        print('BarPerMinute:', BarPerMinute)
        return BarPerMinute

    # 秒数/1小節
    def __sec_per_bar(self):
        self.__spb = 60 / self.__bar_per_minute()
#        print('SecPerBar:', self.__spb)

    # 4部音符の長さ 60秒/120個 1秒/2個 0.5秒/1個
    def sec_per_four(self): return 60 / self.BPM

if __name__ == '__main__':
    tempo = TimeBase()
    print(tempo.BPM)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())
    tempo.Metre=(3,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())
    tempo.Metre=(2,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())
    
    tempo.BPM = 140
    tempo.Metre=(4,4)
    print(tempo.BPM)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())
    tempo.Metre=(3,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())
    tempo.Metre=(2,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_four())

