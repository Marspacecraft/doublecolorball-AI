#!/usr/bin/python3

import os
from openai import OpenAI
from openai import APIError


DEEPSEEK_APIKEY_ENV="DEEPSEEK_APIKEY"
QWEN_APIKEY_ENV="QWEN_APIKEY"

class AI_MODE:
    mode_stream=False
    mode_temperature=0.7
    def __init__ (self, modename, baseurl, apikey):
        self.mode_name = modename   
        self.base_url = baseurl   
        self.api_key = apikey  

    def ask(self, content: str) -> str:
        client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
                )
        # 构建对话历史
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": content}
            ]

        try:
            # 调用模型 API
            response = client.chat.completions.create(
                model=self.mode_name,  # 指定模型名称‌
                messages=messages,
                stream=self.mode_stream, 
                temperature=self.mode_temperature
            )
            return response.choices[0].message.content

        except APIError as e:
            return f"错误1: {e}"
        except Exception as e:
            return f"错误2: {e}"


def ask_qwen_max_last(content: str) -> str:
    qwenmax=AI_MODE(modename="qwen-plus",
                baseurl="https://dashscope.aliyuncs.com/compatible-mode/v1",
                apikey=os.getenv(QWEN_APIKEY_ENV))
    return qwenmax.ask(content)

def ask_deepseek_r1(content: str) -> str:
    deepseekr1=AI_MODE(modename="deepseek-reasoner",
                baseurl="https://api.deepseek.com/v1" ,
                apikey=os.getenv(DEEPSEEK_APIKEY_ENV))
    return deepseekr1.ask(content)

# 示例调用
if __name__ == "__main__":
    import sys

    # 示例命令：python script.py arg1 arg2 arg3
    args = sys.argv  # 返回列表，第一个元素是脚本路径

    if len(args) <= 2:
        print("usage:\n\t"+args[0]+" [deepseek|qwen] [context]")
        exit()

    user_input = args[2]
    print(f"用户输入: \n\t{user_input}")
    
    if args[1] == "qwen":
        print(f"QWen Max 回答：\n\t")
        print(ask_qwen_max_last(user_input))
    elif args[1] == "deepseek":
        print(f"DeepSeek R1 回答：\n\t")
        print(ask_deepseek_r1(user_input))
    else:
        print("usage:\n\t"+args[0]+" [deepseek|qwen] [context]")
        exit()

    
    

    

    
