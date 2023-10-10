# chatgpt-python-django

## 介绍

简易版 高仿`ChatGPT` 官网网站，拿来即用

ChatGPT 5刀账户KEY 自提网 [点击购买](https://chat.orglen.com)  https://kekey.top

体验地址：[点击体验](https://kekey.top) 

登录账户：`admin`密码 `admin`

该项目基于Python Django version 4.2.1下开发

前端vue已经打包好 并未使用前后端分离技术

考虑到小白 

后期也不会对代码进行更新和迭代了基本功能已经完善了 要好好工作了！！！！


## 使用说明

1. 本项目后端用 `django` 快速搭建，可使用宝塔面板中的python项目管理器快速部署（自己研究）

2. 本项目支持流式响应，`markdown` 实时转换为 `html`！

## 部署教程

部署教程我就不讲那么详细了 希望大家自己用就好 我就直接教大家本地运行吧！

我的站点已经被警告了 "该网站/网页因存在不符合中国当地法律的行为，被上级主管部门阻断，域名被暂停解析了"！

直接拉代码进入项目跟目录  ！




##本地运行

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


