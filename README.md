# law_chatbot(v1.0)(Streamlit+FastAPI+Langchain+RAG+OllamaMistral)
这是一个简易的法律助手chatbot，基于提供的美国宪法pdf，做RAG，但只能一次的Q&A。
用Streamlit做前端简易的UI交互，用fastapi做前端和后端的中间层API，用langchain作为chatbot架构，下载ollama下的mistial模型到本地。
未来添加功能方向：多次对话，对话记录保留和展示，登录权限,etc

#####
```text
| 功能类别     | 功能名称                       | 意义                        | 技术关键词                                                       |
| -------- | -------------------------- | ------------------------- | ----------------------------------------------------------- |
| 🧠 对话能力  | ✅ 多轮对话记忆                   | 支持上下文跟进提问（如“那它是哪一年生效的？”）  | LangChain `ConversationBufferMemory` / `ChatMessageHistory` |
| 📚 知识管理  | ✅ 多文档支持                    | 处理多个法律文档，如美国宪法 + 州法 + 案例法 | LangChain DocumentLoader + 文档metadata                       |
| 🔍 精准控制  | ✅ 引用出处（source attribution） | 返回哪一条法律内容、哪一页PDF          | `return_source_documents=True`                              |
| 🧩 交互体验  | ✅ 用户反馈按钮                   | 用户可标记回答“满意 / 不满意”         | Streamlit按钮 + 本地日志记录                                        |
| 💬 控制生成  | ✅ 模型温度/长度控制                | UI允许用户设置回答风格（简洁/详细）       | Streamlit表单 + OpenAI/Mistral参数调节                            |
| 🛠️ 文本能力 | ✅ 答案重写/纠错                  | 对生成的答案重新措辞或修复语义逻辑         | 二次调用LLM + prompt改写                                          |
| 🗃️ 结构功能 | ✅ 会话历史查看                   | 显示用户和Bot的聊天记录             | Streamlit会话state / local JSON                               |
| 🔐 安全边界  | ✅ 限制非法问题                   | 防止用户问与法律无关的内容             | 规则判断 or 分类模型过滤                                              |
| 🧪 工程能力  | ✅ 自动化测试接口                  | 对 API 提交合法问题，验证输出         | FastAPI TestClient / pytest                                 |
| 🚀 性能优化  | ✅ 嵌入缓存                     | 对相同问题不重复嵌入，提高速度           | FAISS / SQLite 缓存向量或LangChain Retriever Cache               |
```

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
