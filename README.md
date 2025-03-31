# doublecolorball-AI
 deepseek和qwen AI模型预测双色球

# 说明   
  * 让deepseek r1和qwen-max使用梅花易数和奇门遁甲预测双色球。  
  * 用程序运行时间起卦。  
  * 提示词：现在的时间是xx年xx月xx日xx时xx分xx秒,请根据这个时间，使用（梅花易数/奇门遁甲）的方式，预测双色球结果。请直接给出预测结果，结果显示格式为：红球：xx,xx,xx,xx,xx,xx蓝球：xx
# 安装与运行   
## 获取deepseek和qwen的API_KEY
* API可能有免费次数，如果没有免费次数需要付费  
* deepseek和qwen申请一个也可以  
* [deepseek API_KEY申请](https://platform.deepseek.com/usage),[申请方法参考](https://blog.csdn.net/m0_46272767/article/details/145568824)
* [qwen API_KEY申请](https://bailian.console.aliyun.com/detail/qwen-max),[申请方法参考](https://explinks.com/blog/ua-qwen2-5-api-application-and-usage-guide/)
* API_KEY可能只允许查询一次，注意保存好API_KEY
## API_KEY写入环境变量   
仅以mac为例，windows网上教程很多  
* 打开终端(Term)
* 运行`echo 'export DEEPSEEK_APIKEY="sk-xxxxxxxxxxx"' >> ~/.zshrc`
* 运行`echo 'export QWEN_APIKEY="sk-xxxxxxxxxxx"' >> ~/.zshrc`
* 运行`source ~/.zshrc`
* DEEPSEEK_APIKEY为deepseek的key，QWEN_APIKEY为qwen的key
## 安装python3及依赖   
* 安装python3及pip3
* 安装openai包`pip3 install openai`
## 运行  
* `python3 SSQ_AI.py`
* ![](https://github.com/Marspacecraft/doublecolorball-AI/blob/main/pic.png)    


