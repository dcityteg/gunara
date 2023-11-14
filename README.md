# chatgpt-python-django

## 介绍

简易版 高仿`ChatGPT` 官网网站，拿来即用

ChatGPT 5刀账户KEY 自提网 [点击购买](https://kekey.top)  https://kekey.top

体验地址：[点击体验](https://chat.orglen.com) 

登录账户：`admin`密码 `admin`

该项目基于Python Django version 4.2.1下开发

前端vue已经打包好 并未使用前后端分离技术

考虑到小白 

后期也不会对代码进行更新和迭代了基本功能已经完善了 要好好工作了！！！！


## 使用说明

1. 本项目后端用 `django` 快速搭建，uwsgi + nginx 部署

2. 本项目支持流式响应，`markdown` 实时转换为 `html`！

## 部署教程

本地部署和宝塔部署，如果仅作个人简单使用直接部署到本地即可，若放到公网上直接用宝塔部署即可。

## 宝塔部署

下载源码上传到网站目录解压或git到网站目录

> #### 进入项目根目录安装依赖

    pip install -r requirements.txt

若出现以下报错

![输入图片说明](img/image.png)

请删除 `requirements.txt` 内对应的版本号即可 或者直接删除 新建一个 `requirements.txt` 并填入以下内容：
```
﻿django-cors-headers
djangorestframework
python-dotenv
django
requests
```
再执行安装依赖

    pip install -r requirements.txt



在 `.env` 文件中 添加 OpenAI API key 和 代理IP:

```
# 填入 OPENAI_API_KEY

OPENAI_API_KEY = "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"

#模型

MODEL = "gpt-3.5-turbo-16k-0613"

# 代理url  可替换

ENDPOINT = "https://api.openai.com/v1/chat/completions" 
```
#### 如何获取：OPENAI_API_KEY
两种方法 ：

一种是有openai账户的直接登录官网拿到 OPENAI_API_KEY

还有一种直接购买 [点击购买](https://kekey.top/) https://kekey.top 价格良心！
  




> #### 安装 uwsgi


    pip install uwsgi

进入到项目根目录创建一个 uwsgi.ini 文件 并填入以下信息 

请将项目目录换成自己实际目录切勿直接复制粘贴

```
[uwsgi]   
http=127.0.0.1:8000  #联调阶段优先使用http模式，方便定点测试

#项目目录  
chdir=/www/wwwroot/chat.orglen.com/ 

#项目中wsgi.py文件的目录，相对于项目目录  
wsgi-file=/www/wwwroot/chat.orglen.com/ChatGPT_python/wsgi.py 

# 指定启动的工作进程数  
processes=4  

# 指定工作进程中的线程数  
threads=2  
master=True  

# 保存启动之后主进程的pid  
pidfile=uwsgi.pid  

# 设置uwsgi后台运行，用uwsgi.log保存日志信息  
daemonize=uwsgi.log  

#项目静态地址
static-map = /static=/www/wwwroot/chat.orglen.com/collectstatic/static

buffer-size     = 65535
post-buffering  = 32768


# 设置虚拟环境的路径  
#virtualenv=/home/shuan/.virtualenvs/bj18_py3# conda 环境路径  
```

若是腾讯云、阿里云、华为云、请到控制台放行端口 8000

> #### 启动 uwsgi

在项目根目录打开终端执行启动命令 

    uwsgi --ini uwsgi.ini


uwsgi 相关命令

    uwsgi --ini uwsgi.ini    #启动命令
    uwsgi --stop uwsgi.pid    #停止命令 
    uwsgi --reload uwsgi.pid    #重启命令



> #### 配置 nginx

将以下代码添加到 `nginx` 中

```
    location / {
        proxy_pass http://127.0.0.1:8000/;
        # 不缓存，支持流式输出
        proxy_cache off;  # 关闭缓存
        proxy_buffering off;  # 关闭代理缓冲
        chunked_transfer_encoding on;  # 开启分块传输编码
        tcp_nopush on;  # 开启TCP NOPUSH选项，禁止Nagle算法
        tcp_nodelay on;  # 开启TCP NODELAY选项，禁止延迟ACK算法
        keepalive_timeout 300;  # 设定keep-alive超时时间为65秒


    }
   location /static {	#这里就是静态文件的配置
        expires 30d;
        autoindex on;
        add_header Cache-Control private;
        alias /www/wwwroot/chat.orglen.com/collectstatic/static/;	
    }
```

请将静态文件的配置换成自己实际目录切勿直接复制粘贴

![输入图片说明](img/nginx.jpg.png)

保存后直接用你绑定的域名访问即可！

> #### 数据库

项目数据库默认使用的 sqlite3

若启动项目报错  请换成 mysql 数据库

安装mysql依赖

    pip install pymysql

在项目中 找到 `ChatGPT_python/__init__.py` 并填入

```
import pymysql
pymysql.version_info = (1,4,13,"final",0)
pymysql.install_as_MySQLdb()
```

在项目中  `ChatGPT_python/settings.py` 中注释以下代码

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

并添加以下代码 请修改为自己的数据库地址

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': '',        #mysql数据库名称

        'USER': '',        #mysql数据库用户

        'PASSWORD': '',    #mysql数据库密码

        'HOST': '',        #mysql数据库连接地址

        'PORT': '3306',    #mysql数据库连接端口
    }
}
```

修改好后回到项目根目录

打开终端执行数据库迁移命令

    python manage.py makemigrations
    python manage.py migrate



在项目根目录打开终端执行启动命令 

    uwsgi --ini uwsgi.ini










## 本地部署

在 `.env` 文件中 添加 OpenAI API key 和 代理IP:

```
# 填入 OPENAI_API_KEY

OPENAI_API_KEY = "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"

#模型

MODEL = "gpt-3.5-turbo-16k-0613"

# 代理url  可替换

ENDPOINT = "https://api.openai.com/v1/chat/completions" 
```
### 如何获取：OPENAI_API_KEY
两种方法 ：

一种是有openai账户的直接登录官网拿到 OPENAI_API_KEY

还有一种直接购买 [点击购买](https://kekey.top/) https://kekey.top 价格良心！
  


### 安装依赖

`pip install -r requirements.txt`

### 启动django 项目

`python manage.py runserver` 

## 项目截图

#### PC端截图

![输入图片说明](https://foruda.gitee.com/images/1695451760221108701/8a345f2d_2098213.png "20230923144856.png")

![输入图片说明](https://foruda.gitee.com/images/1695451839951074237/7861c63e_2098213.png "20230923144951.png")

![输入图片说明](https://foruda.gitee.com/images/1695451923521246282/e389b44b_2098213.png "20230923145140.png")



## 注意

1. 开发不易，拒绝白嫖，如果此小项目帮助到了您，希望能得到您的 `star` ！
2. 页面可任各位修改，希望留下项目地址，为此项目吸引更多的 `star` !
3. 项目使用的开源代理：[https://gitee.com/Flyintro/chatgpt-python-django) ，点个 `star` 支持作者
4. 此项目适合小白，主打简洁，可不断完善！
5. 对于项目如有疑问，可加 `QQ` 群823830031交流！


