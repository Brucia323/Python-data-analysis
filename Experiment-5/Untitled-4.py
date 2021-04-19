import matplotlib.pyplot as plt
from numpy import arange
plt.rcParams['font.sans-serif'] = ['simhei']
title1 = ['18岁以下', '18-24岁', '25-34岁', '35-44岁', '45-54岁', '55岁及以上']
title2 = ['男', '女']
red1 = [0.91, 16.79, 66.14, 13.68, 2.12, 0.36]
red2 = [10.32, 89.68]
black1 = [1.76, 29.58, 60.92, 5.28, 1.41, 1.05]
black2 = [24.42, 73.58]
bar_width = 0.3
plt.subplot(221)
index_red1 = arange(len(title1))
index_black1 = index_red1+bar_width
plt.bar(index_red1, height=red1, width=bar_width, color='red', label='红粉')
plt.bar(index_black1, height=black1,
        width=bar_width, color='black', label='黑粉')
plt.legend()
plt.xticks(index_red1+bar_width/2, title1)
plt.subplot(222)
index_red2 = arange(len(title2))
index_black2 = index_red2+bar_width
plt.bar(index_red2, height=red2, width=bar_width, color='red', label='红粉')
plt.bar(index_black2, height=black2,
        width=bar_width, color='black', label='黑粉')
plt.legend()
plt.xticks(index_red2+bar_width/2, title2)
plt.subplot(245)
plt.pie(red1, labels=title1)
plt.title('红粉')
plt.subplot(246)
plt.pie(black1, labels=title1)
plt.title('黑粉')
plt.subplot(247)
plt.pie(red2, labels=title2)
plt.title('红粉')
plt.subplot(248)
plt.pie(black2, labels=title2)
plt.title('黑粉')
plt.show()
