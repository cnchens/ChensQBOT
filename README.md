# Chens_QBOT
基于Nonebot开发的QQ群机器人
<br>
学业繁忙，可能更新会慢点

# 某些链接
赞助：https://afdian.net/a/cnchens
<br>
网站：搭建中，暂无
<br>
QQ交流群：281814041，入群问题填github即可

# 硬件配置推荐
为了稳定，建议使用服务器平台，并加ECC/RECC内存
<br>
CPU：4核 2.2GHz 及以上
<br>
MEM：DDR3 8G 及以上
<br>
STORAGE：20G及以上（具体视数据库大小而定，建议使用PCIE SSD）
<br>
其他视个人喜好配置即可，后续可能需要GPU加速

# 安装
目前仅支持windows_x86_64系统
<br>
在安装前请确认已经配置好**Python3.7+**和**MongoDB**环境
<br>
在[Releases](https://github.com/cnchens/ChensBOT/releases)中下载最新的压缩包并解压
<br>
如果不需要额外配置的话，首先运行`modinstall.bat`等待安装完成
<br>
然后分别运行`pystart.bat`和`cqstart.bat`
<br>
首次运行会导入数据库，请确保你的MongoDB配置正确（连接时使用默认ip和端口，如果你修改过这两项内容请先往下看）
<br>
导入完成会有提示，请勿在导入时关闭程序（如果不小心关闭了，请删除整个数据库重新导入）
<br>
<br>
#### 以下是高级设置
修改go-cqhttp配置：`安装路径\cqhttp_win_x86_64\config.yml`
<br>
修改超级用户：`安装路径\bot\config.py`
<br>
修改MongoDB连接配置：`安装路径\bot\awesome\plugins\command_events.py`
<br>
打开文件后按照注释修改即可

# 运行
配置好一切之后，我们就可以开始使用机器人了
<br>
私聊界面，直接输入命令即可
<br>
群聊界面，需要先`@机器人名称`再输入命令
<br>
以下拿群聊界面做示范，私聊同理
<br>
输入`@机器人名称 allcmd`获取所有可用命令
<br>
![87eed233f7bc6b4b96f805cc9713b7d](https://user-images.githubusercontent.com/116929900/203548805-48ac768b-ac3f-4e1b-adbc-dec8324ca557.jpg)
<br>
回复结果可能跟图片中的不同，具体以实际为准
<br>

<br>
然后就慢慢摸索罢，这几个命令挺简单的，我都写了帮助文档

