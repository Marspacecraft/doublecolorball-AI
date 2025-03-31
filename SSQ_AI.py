#!/usr/bin/python3

import OpenAI_Agent as opa
from datetime import datetime
import re

MODE_DEEPSEEK=f"DeepSeek R1"
MODE_QWEN=f"QWen Max"

METHOD_QIMENDUNJIA=f"奇门遁甲"
METHOD_MEIHUAYISHU=f"梅花易数"
    

class SSQForecast:
    def __init__ (self,mode:str,method:str,time, balls,result:str):
        self.mode = mode
        self.method = method
        self.time = time   
        self.balls = balls   
        self.result = result

    def __str__(self):
        tostr=f"\n模型:"+self.mode+"\n方法:"+self.method+"\n时间:"+self.time.strftime("%Y年%m月%d日%H时%M分%S秒")+"\n结果:"
        if len(self.balls) == 0:
            return tostr+self.result
        else:
            return tostr+"红球:"+self.balls['Red'].__str__()+" 蓝球:"+self.balls['Blue'].__str__()

def regx(context:str):
    # 正则匹配红球和蓝球
    pattern = r"红球[：:]\s*([\d\s,、]+)[\s\S]*?蓝球[：:]\s*(\d+)"
    match = re.search(pattern, context, re.DOTALL)
    if match:

        # 处理红球：移除空格 -> 分割 -> 过滤空值
        red_str = match.group(1).replace(" ", "").strip()
        red_balls = [num for num in re.split(r"[,\s、]+", red_str) if num]
        
        # 处理蓝球
        blue_ball = match.group(2)
        
        # print(f"红球: {red_balls}")
        # print(f"蓝球: {blue_ball}\n")

        # 校验红球数量是否为6个
        if len(red_balls) != 6:
            print(f"红球数量错误，应为6个，实际得到 {len(red_balls)} 个: {red_balls}")
            return context

        # 校验蓝球是否为1-16之间的数字
        if not (blue_ball.isdigit() and 1 <= int(blue_ball) <= 16):
            print(f"蓝球数值异常: {blue_ball}")
            return context
        
        return {'Red':red_balls,'Blue':blue_ball}
    else:
        return context

def getquestion(time:str,method:str)->str:
    DATA_DIS=f"现在的时间是"+time
    HEAD_1=f""+DATA_DIS+",请根据这个时间，使用"
    HEAD_2=f"的方式，预测双色球结果。请直接给出预测结果，结果显示格式为：红球：xx,xx,xx,xx,xx,xx蓝球：xx"
    return HEAD_1+method+HEAD_2

def ask_deepseek(time,method:str)->SSQForecast:
    result=opa.ask_deepseek_r1(getquestion(time.strftime("%Y年%m月%d日%H时%M分%S秒"),method))

    if True!=result.startswith(f"错误"):
        balls=regx(result)
        forecast=SSQForecast(mode=MODE_DEEPSEEK,method=method,time=time,balls=balls,result=result)
        return forecast
    else:
        forecast=SSQForecast(mode=MODE_DEEPSEEK,method=method,time=time,balls={},result=result)
        return forecast

def ask_qwen(time,method:str)->SSQForecast:
    result=opa.ask_qwen_max_last(getquestion(time.strftime("%Y年%m月%d日%H时%M分%S秒"),method))

    if True!=result.startswith(f"错误"):
        balls=regx(result)
        forecast=SSQForecast(mode=MODE_QWEN,method=method,time=time,balls=balls,result=result)
        return forecast
    else:
        forecast=SSQForecast(mode=MODE_QWEN,method=method,time=time,balls={},result=result)
        return forecast


if __name__ == "__main__":
    # 获取当前时间并格式化为汉字形式
    current_time = datetime.now()
    print(ask_qwen(time=current_time,method=METHOD_MEIHUAYISHU))
    print(ask_qwen(time=current_time,method=METHOD_QIMENDUNJIA))
    print(ask_deepseek(time=current_time,method=METHOD_MEIHUAYISHU))
    print(ask_deepseek(time=current_time,method=METHOD_QIMENDUNJIA))

