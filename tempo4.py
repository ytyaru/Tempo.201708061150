# BPM:Beats Per Minute。1分間あたりの四分音符数
# 小節:bar
# 拍子:Metre

#http://sumishiro.blogspot.jp/2010/08/blog-post_26.html
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
#    def sec_per_four(self): return 60 / self.BPM
    def sec_per_base(self): return 60 / self.BPM
    
    
#音価から時間長を取得する
#https://en.wikipedia.org/wiki/Note_value
class NoteValue:
    def __init__(self, timebase:TimeBase):
        self.__timebase = timebase
    """
    音符における時間の長さを取得する。
    base: 音価(分数の分母)。1,2,4,8,16,32,64,128,256,...2のn乗値。
    dotted: 符点.。baseの1.5倍
    let: 連符。baseの等分。2,3,4,5,6,7,8,9 
    """
    def Get(self, base, dotted=False, let=0):
        dotted_rate = 1.5 if dotted else 1.0
#        if dotted: dotted_rate = 1.5
#        else: dotted_rate = 1.0
        length = self.__timebase.SecPerBar * (1 / base) * dotted_rate
        if 1 < let: length /= let
        return length


if __name__ == '__main__':
    tempo = TimeBase()
    print(tempo.BPM)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_base())
    tempo.Metre=(3,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_base())
    tempo.Metre=(2,4)
    print(tempo.Metre)
    print(tempo.SecPerBar)
    print(tempo.sec_per_base())
    
    tempo.Metre=(4,4)
    print(f'{tempo.Metre}拍子 {tempo.SecPerBar}秒/1小節')
    nv = NoteValue(tempo)
    for b in [pow(2, n) for n in range(8)]:
        print(f'{b}部音符:{nv.Get(b)}秒')

    for b in [pow(2, n) for n in range(8)]:
        print(f'{b}部符点音符:{nv.Get(b, dotted=True)}秒')

    let = 3
    for b in [pow(2, n) for n in range(8)]:
        print(f'{b}部{let}連符の一つ:{nv.Get(b, let=let)}秒')

    let = 3
    for b in [pow(2, n) for n in range(8)]:
        print(f'{b}部符点{let}連符の一つ:{nv.Get(b, dotted=True, let=let)}秒')

