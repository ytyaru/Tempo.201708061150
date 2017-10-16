# BPM:Beats Per Minute。1分間あたりの四分音符数
# 小節:bar
# 拍子:Metre
import math

BPM = 120
BPM_BASE = 4 # 4部音符
metre = (4, 4) # 4/4拍子

BarPerMinute = BPM / (metre[0] * (metre[1] / BPM_BASE))
print('BarPerMinute:', BarPerMinute)

SecPerBar = 60 / BarPerMinute
print('SecPerBar:', SecPerBar)
