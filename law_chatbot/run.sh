#!/bin/bash

# 启动 FastAPI 服务
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# 启动 Streamlit 前端
streamlit run streamlit_app.py --server.address=0.0.0.0 --server.port=8501