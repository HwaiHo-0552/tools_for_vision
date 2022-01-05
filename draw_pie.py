###### DiLusense 核心技术中心 ######
###### 算法工程师 2022.1.5 Hefei ######


#!/usr/bin/python
#-*- coding:UTF-8 -*- 

import os
import numpy as np
import matplotlib.pyplot as plt

over_time = 0.5123                                                         # Inference总时间
test_1 = ["backbone_time=0.4902s",                                         #计算得到的各个模块时间
          "FPN_time=0.0066s",
          "SSH_time=0.0103s",
          "head_time=0.0052s"
          ]
save_pth = 'E:\maxz\工作\试用期second_month工作(maxz)\inference_time'       #保存绘图的路径
img_name= 'test_2.jpg'                                                     #待存命名

class draw_pie:
    def __init__(self, sum_time, inputs, save_path):
        self.sum_time = sum_time 
        self.inputs = inputs
        self.save_path = save_path

    def to_pie_char(self):
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect="equal"))
        type = [str(x.split('=')[0]) for x in self.inputs]
        data = [float(x.split('=')[-1].split('s')[0])/float(self.sum_time) for x in self.inputs]

        ax.pie(data, labels=type, autopct='%.2f%%', startangle=20)
        ax.legend(self.inputs, loc='upper left')
        ax.set_title('Time Consumption of each block during Inference.')
        plt.savefig(self.save_path, dpi=500)
        
        plt.show()
        
def main():
    save_img = os.path.join(save_pth, img_name)
    drawing = draw_pie(over_time, test_1, save_img)
    drawing.to_pie_char()

if __name__=='__main__':
    main()