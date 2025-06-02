# law_chatbot-2025_06_02
这是一个简易的法律助手chatbot，基于提供的美国宪法pdf，做RAG，但只能输入一次问题和输出一次回答。并且是基于docker部署和管理，用langchain作为架构，下载本地的ollama下的mistial模型，最后用fastapi做中间层。

### 运行这个Hub：

cd ./desktop

github clone https://github.com/Guilin-Jiang/law_chatbot-2025_06_02

start docker

docker-compose up --build

open URL http://0.0.0.0:8501
