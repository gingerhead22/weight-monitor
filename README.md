Weight Monitor
------

**1. 安装git**

打开terminal， 将下面的内容拷贝至Terminal 中， 并回车。

```
brew install git
```

**2. 下载程序**

```
git clone https://github.com/gingerhead22/weight-monitor
```

**3. 将路径移动到weight_monitor文件夹**

```
cd ./weight_monitor
```


**4. 安装相关libraries**

```
pip install requirements.txt
```


**5. 运行程序**

```
python weight_monitor.py
```

初次运行时，会被额外要求输入目标时间， 体重和体脂率。 之后每次需要更新数据时， 再次按照步骤五启动程序并按要求输入当前体重和体脂率即可。