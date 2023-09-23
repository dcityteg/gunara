import requests
from dotenv import load_dotenv
import os
import json
import time

from chatgpt.models import Conversation

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ENDPOINT = os.getenv("ENDPOINT")  
   
# ENDPOINT = "https://syntaxez.com/v1/chat/completions"   
          
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}",
}

def chat(prompt):
    
    data = {
        "messages": prompt,
        "model":os.getenv("MODEL") ,
        "max_tokens": 1000,
        "temperature": 0.5,
        "top_p": 1,
        "n": 1,
        "stream":True
    }
    
    response = requests.post(
        ENDPOINT, headers=headers, 
        json=data,stream=True
        )
    return response



# ChatGPT 流式内容输出

def ChatStream(response,chat_id,messages,json_data,regenerate):
    try:
        speech = ""
        conv_obj = Conversation.objects.filter(uuid=chat_id).first()
        
    except:  # noqa: E722
        pass
    
    for line in response.iter_lines():  
        if line:
            data = line.decode('utf-8')[6:]
            if data == "[DONE]":
                
                #判断是否重新作答
                if regenerate:
                    json_data[-1]["speeches"].append(speech)
                    json_data[-1]["suitable"].append(0)
                    json_data[-1]["idx"] += 1
                else:
                    json_data[-1]["speeches"][0] = speech
                    
                assistant = {"role": "assistant", "content":speech}
                
                messages.append(assistant)
                
                conv_obj.messages = json.dumps(messages)
                conv_obj.data = json.dumps(json_data)
                
                conv_obj.save()
                
                # print("message：",json.loads(conv_obj.messages))
                # print("data：",json.loads(conv_obj.data))
                # print(conv_obj.__dict__) 
                
                response.close()
                break
            content = json.loads(data).get('choices', [{}])[0].get("delta", {}).get("content")  # noqa: E501
            
            if content is not None: 
                speech += content
                yield content



#自定义模拟流式内容返回      

def stream(message):
        time.sleep(1)
        for char in message:
            time.sleep(0.05)
            yield f"{char}"
            
            
