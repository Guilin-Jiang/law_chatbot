# law_chatbot(v1.0)(Streamlit+FastAPI+Langchain+RAG+OllamaMistral)
这是一个简易的法律助手chatbot，基于提供的美国宪法pdf，做RAG，但只能一次的Q&A。
用Streamlit做前端简易的UI交互，用fastapi做前端和后端的中间层API，用langchain作为chatbot架构，下载ollama下的mistial模型到本地。
未来添加功能方向：多次对话，对话记录保留和展示，登录权限,etc

## 上手试试吧！快速开始！
#### 需要提前下载
1.Docker(https://www.docker.com/)
2.官网下载Ollama(https://ollama.com/) 
  在terminal运行
  ```bash
  ollama run mistral
  ```

#### 准备文件
下载文件夹 CMD：
```bash
cd ./desktop
github clone https://github.com/Guilin-Jiang/law_chatbot
```

#### 开始运行
```bash
cd ./law_chatbot
docker-compose up --build
```

#### 本地测试效果
open URL http://0.0.0.0:8501

## 项目文件概述
```text
law_chatbot/
├── app/
│   ├── main.py            # FastAPI 接口服务
│   ├── rag_chain.py       # RAG 构建逻辑
│   ├── load_documents.py  # 加载并嵌入法律文件
├── data/
│   ├── leagl_documents    # 美国宪法的pdf
├── streamlit_app.py       # 前端页面逻辑
├── run.sh                 # 启动脚本
├── Dockerfile             # 构建镜像
├── docker-compose.yml     # 容器管理
├── requirements.txt       # 依赖列表
└── README.md              # 项目说明文档
```
