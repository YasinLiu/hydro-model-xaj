# hydro-model-xaj

## 项目介绍

根据中国水利水电出版社出版的，由武汉大学叶守泽老师和河海大学詹道江老师等合编的《工程水文学》第三版教材中新安江模型的原理，结合河海大学芮孝芳老师《水文学原理》中的相关知识，并重点参考了河海大学包为民老师的《水文预报》第4版，编写的**三水源新安江模型**的 python 版本。因为此项目动机是复习新安江模型，所以代码不是重点，重点是思路，具体的思路在[wiki](https://github.com/OuyangWenyu/hydro-model-xaj/wiki)中都有说明。

项目目前有了第一个相对完整的可测试版本**v0.1.1**，仍在开发中。

详细说明请移至[wiki页面](https://github.com/OuyangWenyu/hydro-model-xaj/wiki)。

## 使用说明

运行test.py中的测试函数即可。
目前测试函数包括直接调用模型的测试函数，以及率定的测试函数，简单修改程序即可测试任意一个。测试使用的数据较少，并不符合实际预报规范，目前项目只是为了梳理新安江模型原理及其运算过程，实际应用还在本项目代码基础上进一步开发。

wiki文档使用markdown编写，浏览器上显示格式不完全，建议使用vscode编辑器+相应插件（在vscode的插件库中直接搜索markdown，选择markdown preview enhanced插件即可）浏览。

如果觉得项目中文字和代码对原理的理解有误，或者出现代码运行错误，请在[issues](https://github.com/OuyangWenyu/hydro-model-xaj/issues)中留言。

## 主要内容

本项目涉及内容主要包括以下各方面，详见[wiki页面](https://github.com/OuyangWenyu/hydro-model-xaj/wiki)。

- 数据处理

- 模型核心算法
  - 前期土壤含水量计算
  - 流域产流计算
  - 水源划分
  - 汇流计算

- 实测径流分析
  - 退水曲线分析
  - 流量过程分割

- 参数率定
  - 模型参数概念分析
  - 率定算法

## 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
