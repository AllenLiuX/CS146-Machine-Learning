import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import time
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块

if __name__ == '__main__':
    start_time = time.time()
    fig = plt.figure(figsize=(5, 5))
    df = pd.read_csv('points.csv')
    print(df)
    # ar = np.random.randn(20, 4)
    # df2 = pd.DataFrame(ar, columns=['a', 'b', 'c', 'd'])
    # df2['e'] = pd.Series(
    #     ['one', 'one', 'one', 'one', 'one', 'one', 'two', 'two', 'two', 'two', 'two', 'two', 'two', 'two',
    #      'three', 'three', 'three', 'three', 'three', 'three'])
    # sns.scatterplot(df2['a'], df2['b'], hue=df2['e'])
    # print(df2)
    ax = axisartist.Subplot(fig, 111)  # 使用axisartist.Subplot方法创建一个绘图区对象ax
    ax.axis["x"] = ax.new_floating_axis(0, 0, axis_direction="bottom")  # 添加x轴
    ax.axis["y"] = ax.new_floating_axis(1, 0, axis_direction="bottom")  # 添加y轴
    sns.scatterplot(df['feature1'], df['feature2'], hue=df['y'])
    plt.xlim(-11, 11)
    plt.ylim(-11, 11)
    plt.axis()
    plt.grid()
    plt.savefig('plot.png')
    plt.show()
    print('======= Time taken: %f =======' %(time.time() - start_time))
