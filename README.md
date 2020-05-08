# 东南大学健康上报系统
* [环境配置](#%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)
  * [chrome驱动](#chrome%E9%A9%B1%E5%8A%A8)
    * [chrome版本查看](#chrome%E7%89%88%E6%9C%AC%E6%9F%A5%E7%9C%8B)
    * [chromedriver下载](#chromedriver%E4%B8%8B%E8%BD%BD)
    * [驱动放到指定文件夹](#%E9%A9%B1%E5%8A%A8%E6%94%BE%E5%88%B0%E6%8C%87%E5%AE%9A%E6%96%87%E4%BB%B6%E5%A4%B9)
  * [python环境配置](#python%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE)
* [测试脚本](#%E6%B5%8B%E8%AF%95%E8%84%9A%E6%9C%AC)
* [设置定时任务](#%E8%AE%BE%E7%BD%AE%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1)
## 环境配置
### chrome驱动
> 脚本需要chrome支持，所以想要使用此脚本，请安装chrome
#### chrome版本查看
![](https://pic.downk.cc/item/5eb4faedc2a9a83be556223f.png)
#### chromedriver下载
>根据chrome版本信息到[官网](https://npm.taobao.org/mirrors/chromedriver/)下载，注意下载的是windows32版本
#### 驱动放到指定文件夹
>根据你电脑默认使用的python解释器，找到python.exe文件夹，将刚才下载的文件解压到这个文件夹

具体而言，在windows下`win+R`，输入`cmd`，输入`python -V`，这样你就知道电脑默认使用的python版本（如果有多个版本），然后在开始中找到你这个python版本，右键打开exe所在的文件夹。
>tips
>如果没有安装python，建议直接使用anaconda进行安装，无论哪种安装方式，请记得安装时勾选上把python加入环境变量

### python环境配置
- python除了刚才的安装之外，还有就是安装依赖包。
- 打开cmd，输入`pip -V`，查看pip对应的版本是否正确，更新pip以及更换pip源（下载速度更快）等也是常规操作，不会的百度一下，很简单
- 然后安装依赖：

``` python
pip install selenium
pip install win32gui
pip install pypiwin32
```
## 测试脚本
>在脚本所在文件的文件导航栏输入`cmd`，回车打开cmd，输入`python sign_in.py`进行测试，如果出错请提出issue或者邮箱联系我：1779176477@qq.com

## 设置定时任务
- 打开`文件管理器`,右键`此电脑`,选择`管理->任务计划程序->任务计划程序库->Microsoft->Windows`,选中Windows文件夹之后再点击右边的`创建基本任务`
![](https://pic.downk.cc/item/5eb50058c2a9a83be55c8fba.png)
- 对`常规、触发器、操作`进行设置，如下图：
![](https://pic.downk.cc/item/5eb500bbc2a9a83be55cfa56.png)
![](https://pic.downk.cc/item/5eb50133c2a9a83be55d7d29.png)
![](https://pic.downk.cc/item/5eb501fbc2a9a83be55e4ca2.png)
>Tips
>注意，添加参数选项卡中，要填写文件地址，也就是包括.py，如：D:\mypython\learning\sign_in.py
>而起始于只需要填写到python.exe所在文件夹就行，也就是刚才放driver的地方
- 如下图，选中刚才创建的任务，点击运行测试一下，成功则说明设置好了，请享用吧，如果体温异常请一定记得手动上报哦
![](https://pic.downk.cc/item/5eb502fac2a9a83be55f5a06.png)