import matplotlib.pyplot as plt  # 对图片做一些改动
import pandas as pd  # 数据分析的库
import numpy as np;  # 大量数学函数库，大量维度数组和矩阵运算

a=pd.Series(np.random.randn(1000),index=pd.date_range('20100101',periods=1000))
b=a.cumsum()
b.plot()
plt.show()    #最后一定要加这个plt.show()，不然不会显示出图来。