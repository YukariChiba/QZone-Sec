# QZone-Sec
一个神秘的抓取QQ空间秘密作者的脚本，针对Python基础并不好的小白们。  
A mysterious tool for Python XiaoBais to see the senders of secrets in QZone.

[![platform](https://img.shields.io/badge/python-3.6-green.svg)]()  

## 注意！！！
本工具已无法继续使用，可能的原因是更改了api地址或者使用qq自身的验证措施，有兴趣的朋友可以试着对QQ流量进行抓包（请使用xposed模块just trust me或相同工具绕过证书绑定，否则无法实现抓包），不过本人猜测本工具的运作原理大概率已经无法满足，这些代码就留作后人研究了。

### 谨记
这个项目源于当年学Python时做的练手项目，本人只是拿这个来做研究和学习。我不关心你们有多少故事，也不关心你把这个拿来做什么，但是容我告诫一句，**不要用它来伤害你所在乎的人**，如果你真想看，有些东西，知道就好。

### 简介

[qwqmeow](https://github.com/qwqmeow) 针对之前的分析，写了[一个脚本](https://github.com/qwqmeow/qqzone)，但是并不完整，这个脚本是不能直接给小白们使用的，所以亲自动手进行了改进，主要基于本人的个人查询站和先前的代码。

1. 使用SQLite存储数据，有兴趣的自己修改db.py可以兼容MySQL。
2. 使用tqdm作为进度条，更加美观。
3. 将时间戳转换成日期输出，也是更加美观。
4. 在settings.py里可以设置输出，还是更加美观。
5. 优化了我之前的恶心代码，减少了一堆bug的出现。
6. 不仅会将某QQ号的秘密存储，还将存储该用户的所有好友的所有秘密，并设置发送者为null。
7. 秘密全部以id和时间戳的格式存储，有效避免重复。
8. 有兴趣的可以试试前缀树剪枝的方式对未发现发送者的秘密条目进行分类。

### 食用方法

- 请参照[qwqmeow的脚本](https://github.com/qwqmeow/qqzone)获取cookie和g_tk，填到settings.py和qzone_req.py处。
- qzone_req.py只需替换[...]处的对应信息

### 你可能需要安装...
- tqdm
- urllib
- sqlite3
- json  
(好吧我也不知道哪些是Python自带的)

### 初始化设置
有下列地方需要修改：
- settings.py 修改g_tk和数据库文件，并设置显示规则
- qzone_req.py 修改cookie
- db.sql 创建SQLite数据库

#### db.sql : 数据库初始化
```sql
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'SEC', 'SEC', 2, 'CREATE TABLE "SEC"
(
    ID int PRIMARY KEY,
    QQ CHAR(20),
    CONTENT CHAR(300),
    T_STAMP CHAR(30),
    M_ID CHAR(70)
)');

```

#### settings.py : 设置
```python
g_tk = '[Your g_tk]' #填写你的g_tk，非常重要
api_url = "https://h5.qzone.qq.com/webapp/json/secretList/getSecretActFeeds" #API地址，不需要改
default_end_time = 1484841600 # 默认开始搜索时间戳，这里是2017年1月，是秘密刚刚上线的时间
db_data = 'data.db' # 数据库文件
insert_sql = True # 是否将找到的结果插入数据库
show_unknown = False # 显示搜索的QQ的好友发的秘密(作者为Unknown)
show_detail = False # 显示详细信息(没卵用，就关掉吧)
db_name = 'SEC' # 数据库表名
```

### 两个功能

#### find.py : 单号查找
即查找一个QQ号在某段时间发过的所有秘密。
```bash
python3 find.py -h
usage: find.py [-h] -q QQ_NUM [-s START_DATE] [-F]

optional arguments:
  -h, --help     show this help message and exit
  -q QQ_NUM      the qq number you want to lookup
  -s START_DATE  the start timestamp you want to spider
  -F             whether the data is forced updated
```

##### Example
```bash
python3 find.py -q 123123123 -s 1514736000
Start searching QQ 123123123                                                         
 [2018-06-01 00:30:50 (123123123) test                                       
T-stamp 2018-01-01: : 14752569it [00:08, 1569483.60it/s] 
```

#### list_scan.py : 列表查找
即查找一个QQ号列表里每个QQ在某段时间发过的所有秘密。
```bash
python3 list_scan.py -h 
usage: list_scan.py [-h] -l QQ_LIST [-s START_DATE] [-F]

optional arguments:
  -h, --help     show this help message and exit
  -l QQ_LIST     the qq numbers list you want to lookup
  -s START_DATE  the start timestamp you want to spider
  -F             whether the data is forced updated
```

##### Example
```bash
python3 list_scan.py -l test.list -s 1514736000
Start searching QQ 123123123                                                         
 [2018-06-01 00:30:50 (123123123) test                                       
T-stamp 2018-01-01: : 14752569it [00:08, 1569483.60it/s] 
Start searching QQ 1231231234                                                         
 [2018-06-02 02:30:51 (1231231234) test2                                       
T-stamp 2018-01-01: : 18742933it [00:10, 1265756.10it/s] 
```
