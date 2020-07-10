# 2020春商务数据分析大作业

2020年春季学期毛波老师的商务数据分析大作业，我选用的是德铁（Deutsche Bahn）的列车晚点数据进行分析，最终课程成绩是 A+。

## 题目简介

期末数据分析报告要求：

1. 从网络学堂上给出的数据集中选择一个作为分析对象

2. 或自己提供一个不少于十万条原始数据的数据集（提交报告时请同时提交原始数据集作为参考）

3. 数据分析中应包括对数据的处理、数据的统计分析、数据分析结果及应用前景等内容，详见[数据分析报告内容要求](data/report_requirement.pdf)。

我是选择自选数据集，从 Kaggle 上找到一个[德铁列车时间的数据集](https://www.kaggle.com/chemamengibar/dbahn-travels-captures/data)，详见我的[数据分析报告](report_text/)。

## Repo 内容结构

- DB_data 文件夹
    - 十个德国主要城市某天列车进出站信息原始数据

- data 文件夹
    - 其他分析所需的文件
    - [数据分析报告内容要求](data/report_requirement.pdf)

- [report_tex 文件夹](report_tex/)
    - 只放了数据分析报告的 .tex、.bib、所需的图片及最终 pdf 文件，模板为 [ElegantPaper](https://github.com/ElegantLaTeX/ElegantPaper) ![GitHub stars](https://img.shields.io/github/stars/ElegantLaTeX/ElegantPaper?style=social) 

- results 文件夹
    - 代码输出结果，其中几个比较好看的 html 文件：
        - [列车总行驶轨迹](results/total_track_graph.html)
        - [晚点列车行驶轨迹](results/delayed_track_graph.html)
        - [不同时间段列车行驶轨迹的交互图](results/timeline_map.html)

- 代码：
    - utils，对数据进行预处理，提取之后分析需要用到的信息。
    - text，对列车晚点信息进行文本分析。
    - network，对列车行驶轨迹进行网络分析。
    - 使用 pyecharts 画图：
        - save_city_coor，存储城市经纬度信息。
        - total_graph，列车总行驶轨迹。
        - delayed_graph，晚点列车行驶轨迹。
        - timeline，不同时间段列车行驶轨迹的交互图。
