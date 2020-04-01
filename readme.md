# KGview-python

项目地址：https://github.com/mr-program/KGview_python

项目中文地址：https://gitee.com/mrprogram/KGview_python

知识图谱的可视化方案，参考https://github.com/molamolaxxx/KGView，加入Flask后台数据处理。

使用说明：

1.修改./KG_data/node.json添加图谱节点

2.修改./KG_data/relation.json添加图谱节点关系

3.运行index.py

4.访问127.0.0.1:5000/KG

加载页面时，会先读取两个json文件，然后再渲染页面。

特别感谢：

https://github.com/molamolaxxx/KGView