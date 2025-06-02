from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from . import rag_chain
import traceback

app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(question: Question):
    try:
        # 验证输入
        if not question.query:
            raise HTTPException(status_code=400, detail="问题不能为空")

        # 调用 rag_chain 模块处理问题
        answer = rag_chain.retrieve_and_generate(question.query)
        
        # 如果没有生成答案，返回默认反馈
        if not answer:
            raise HTTPException(status_code=404, detail="未找到答案")
        
        # 正常返回答案
        return {"answer": answer}

    except HTTPException as e:
        # 捕获并返回 HTTP 错误，例如 400 和 404
        raise e

    except Exception as e:
        # 打印堆栈信息到容器日志
        print("/ask 接口发生未预期错误：")
        traceback.print_exc()
        # 返回给前端调试信息（正式部署可关闭）
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")
