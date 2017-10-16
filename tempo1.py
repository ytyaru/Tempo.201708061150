# BPM:Beats Per Minute。1分間あたりの四分音符数
# 小節:bar
# 拍子:Metre
import math

BPM = 120
BPM_BASE = 4 # 4部音符

metre = (4, 4) # 4/4拍子
BPM_BASE_sec = 0 #BMP_BASE音符における絶対時間（4部音符の長さ(秒)）
metre_base_sec = 0 #拍子の分母音符における絶対時間

# 小節/1分間
def bar_per_minute(metre=(4, 4)):
    BarPerMinute = BPM / (metre[0] * (metre[1] / BPM_BASE))
    print('BarPerMinute:', BarPerMinute)
    return BarPerMinute

# 秒数/1小節
def sec_per_bar(metre=(4, 4)):
    SecPerBar = 60 / bar_per_minute(metre)
    print('SecPerBar:', SecPerBar)
    return SecPerBar
    
# 秒数/BPM_BASE(4部音符)
def sec_per_base(sec_per_bar): return sec_per_bar / BPM_BASE

# 秒数/拍子の分母
#def sec_per_base(sec_per_bar): return sec_per_bar / (metre[1] / BPM_BASE)
#def sec_per_base(sec_per_bar): return sec_per_bar / (metre[0] * (metre[1] / BPM_BASE))


if __name__ == '__main__':
    print(sec_per_bar(metre=(4,4)))# 4/4拍子
    print(sec_per_bar(metre=(3,4)))# 3/4拍子
    print(sec_per_bar(metre=(2,4)))# 2/4拍子
    
    metre=(4,4)
    spbar = sec_per_bar(metre)
    spbase = sec_per_base(spbar)
    print('拍子={} 1小節={}sec 𝅘𝅥={}sec'.format(metre, spbar, spbase))
