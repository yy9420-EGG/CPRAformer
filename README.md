# CPRAformer: 基于Transformer的图像去雨模型
本仓库为 CPRAformer 图像去雨模型复现代码，课程实验复现项目。

## 项目信息
- 原论文官方仓库：https://github.com/zs1314/CPRAformer
- 复现数据集：Synthetic_Rain_Datasets
- 有效测试样本：2142张
- 实验指标：平均PSNR = 30.70 dB，平均SSIM = 0.9081

## 环境依赖
- Python >=3.8
- Pytorch
- opencv-python
- scikit-image
- numpy

## 文件说明
- `train.py`：模型训练脚本
- `test.py`：推理测试脚本
- `*.py`：网络结构、损失函数等模块
- `*.yml`：训练配置文件

## 模型权重与测试输出图片
权重文件、测试生成的去雨图片体积较大，不存放在GitHub。
百度网盘链接：
提取码：

## 复现备注
测试集总计2800张图像，推理过程中第2143张图像出现数据异常，因此选取2142张有效样本计算PSNR、SSIM。实验结果表明该模型能够有效去除图像雨纹，较好保留图像细节纹理。
