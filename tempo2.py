# BPM:Beats Per Minute。1分間あたりの四分音符数
# 小節:bar
# 拍子:Metre
import math

class Tempo:
    def __init__(self):
        self.__BPM = 120
        self.__BPM_BASE = 4 # 4部音符

    @property
    def BPM(self): return self.__BPM
    @BPM.setter
    def BPM(self, value):
        if 0 < value and isinstance(value, int):
            self.__BPM = value
            self.sec_per_bar()
    
    # n小節/1分間
    def bar_per_minute(self, metre=(4, 4)):
        BarPerMinute = self.BPM / (metre[0] * (metre[1] / self.__BPM_BASE))
        print('BarPerMinute:', BarPerMinute)
        return BarPerMinute

    # 秒数/1小節
    def sec_per_bar(self, metre=(4, 4)):
        SecPerBar = 60 / self.bar_per_minute(metre)
        print('SecPerBar:', SecPerBar)
        return SecPerBar
    
    # 4部音符の長さ
    def sec_per_four(self, metre=(4, 4)): return self.sec_per_bar(metre) / 4
    
"""
class Metre:
    def __init__(self, numerator=4, denominator=4):
        self.__numerator = 4 #分子
        self.__denominator = 4 #分母
    @property
    def Numerator(self): return self.__numerator
    @property
    def Denominator(self): return self.__denominator
# 秒数/BPM_BASE(4部音符)
def sec_per_base(sec_per_bar): return sec_per_bar / BPM_BASE
"""

if __name__ == '__main__':
    tempo = Tempo()
    print(tempo.BPM)
    print(tempo.sec_per_bar((4,4)))
    print(tempo.sec_per_bar((3,4)))
    print(tempo.sec_per_bar((2,4)))
