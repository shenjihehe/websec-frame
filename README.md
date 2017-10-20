# websec-frame
### 开源的安全扫描器框架，支持漏洞模块开发载入

### 目录结构
#### /exp   漏洞利用模块（暂不公开提供，原因你也懂的）
#### /lib/data 各种字典储存位置
#### /lib/core 核心文件库（cdn检测，端口扫描，网站爬虫，网址处理等模块）
#### /lib/websec.py 主调度程序
#### /script 存放漏洞检测模块（sql，xss，email，webshell_check等） 当然你也可以开发其他漏洞检测模块加入

## 更新说明：较上一版本，基于python3重新架构，优化线程效率和一些模块特殊情况下可能出现的小blog（近期可能会解锁一些其他热门漏洞检测模块）
