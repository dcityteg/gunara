
#  ██████╗██╗  ██╗ █████╗ ████████╗ ██████╗ ██████╗ ████████╗
# ██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔════╝ ██╔══██╗╚══██╔══╝
# ██║     ███████║███████║   ██║   ██║  ███╗██████╔╝   ██║   
# ██║     ██╔══██║██╔══██║   ██║   ██║   ██║██╔═══╝    ██║   
# ╚██████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║        ██║   
#  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝        ╚═╝   
#
#  感谢使用ChatGPT仿站，前端高仿官网！
#  项目地址：https://gitee.com/Flyintro/chatgpt-python-django
#  作者：vx2893288528  


#=============================================================


# 当我写完这些代码的时候我和我的女朋友分手了
# 我不知道为什么
# 直到现在我也不知道我真正错在了哪里
# 或许
# 如果我能再有钱一点就好了
# 她很好 很漂亮 也很善良 
# 是我对不起她
# 分手时我们都说了伤害对方的话
# 也许 我是说也许 
# 对不起 真的对不起 ...
# 代码也真的写很烂 或许 我真的什么也做不好 ...
# 就连自己最心爱的女人我都没能留住...
# 我希望当你把代码拉下的时候或二开的时候能保留住这段注释！我也很希望她能看到这段注释。
# 对不起！请原谅我的自私。

# 我爱你
# 可是我们总是用恶毒的话伤害最爱的人
# 然后再陷入深深的忏悔
# 感情也许就是在这样的循环中被消磨撕扯
# 慢慢地变得无迹可寻，我们就这样在嘶吼里告别
# 就像那些美好的回忆从我们的生活中抹去一样，仿佛从未发生。


from django.http import HttpResponse, StreamingHttpResponse
from utils.Result import  ResSuccess,ResError
import json
import os
import uuid

from rest_framework.response import Response

from rest_framework.decorators import api_view

from api.util.serializers import RandomUUIDSerializer,ConversationSerializer

from chatgpt.models import Conversation
from utils.openai import completions
from datetime import datetime
from dotenv import load_dotenv
# from django.core import serializers
load_dotenv()




@api_view(['POST'])
def random_uuid(request):
    random_uuid = uuid.uuid4()
    serializer = RandomUUIDSerializer({'data': random_uuid})
    return Response(serializer.data)



def prompt(request,chat_id): 
    if request.method == 'POST':
        body = request.body.decode()
        json_obj = json.loads(body)
        prompt = json_obj.get('prompt')
        regenerate = json_obj.get('regenerate')
    
        
        conv_obj = Conversation.objects.filter(uuid=chat_id).first()
        
        # 获取当前时间
        HumanDate = datetime.now()
        
        human = {
            "createTime": HumanDate.strftime("%Y-%m-%d %H:%M:%S"),
            "speaker":"human",
            "speech":prompt,
                
        }
        # 如果chat_id不存在数据库执行数据库对话初始化
        if conv_obj is None:
            messages = [{'role': 'system', 'content': '你是一个有用的助手'}]
            
            messages.append({"role": "user", "content":prompt})
            
            data = []
            
            model = os.getenv("MODEL")
            data.append(human) 
            
            # json_message = json.dumps(messages)
            # json_data = json.dumps(data)

            Conversation.objects.create(
                uuid=chat_id,
                model = model,
                messages=json.dumps(messages),
                data=json.dumps(data)
                )
            
        try:
            messages = json.loads(conv_obj.messages)
            data = json.loads(conv_obj.data)
            messages.append({"role": "user", "content":prompt})
            #判断是否重新作答
            if not regenerate:
                data.append(human) 
            # print(messages)
            # print(data)
            
        except:  # noqa: E722
            pass
        
        response = completions.chat(messages[-10:],)  #默认数据库中后10条历史消息
        status_code = response.status_code
        try:
            if status_code == 200:
                
                ChatDate = datetime.now()
               
                chatgpt = {
                "createTime": ChatDate.strftime("%Y-%m-%d %H:%M:%S"),
                "idx":0,
                "speaker": "ai",
                "speeches":[""],
                "suitable": [0],   
                 }
                
                #判断是否重新作答
                if not regenerate:
                    data.append(chatgpt) 

                response = StreamingHttpResponse(
                    completions.ChatStream(response,chat_id,messages,data,regenerate), 
                    content_type='text/event-stream'
                    )
                response['Content-Type'] = 'text/event-stream; charset=utf-8'
                return response
            else:
                return HttpResponse(response.text,status=400)
        except:  # noqa: E722
            error = "服务器请求或解析报文出现异常,请联系当前所属站点管理员处理！"
            return HttpResponse(error,status=500)
    return ResError("访问受限！")





@api_view(['POST'])
def conversation(request,conv_id):
    conversation = Conversation.objects.get(uuid=conv_id)
    serializer = ConversationSerializer(conversation)
    return Response(serializer.data)



#标题
def gen_title(request,conv_id):
    conv_obj = Conversation.objects.filter(uuid=conv_id).first()
    title = json.loads(conv_obj.messages)[-1]['content'][0:12]
    return ResSuccess(title)