import streamlit as st
import requests

st.title("法律问答机器人")

# 用户输入问题
user_input = st.text_area("请输入您的问题:")

# 添加发送按钮
if st.button("发送"):
    if user_input:
        with st.spinner('正在处理您的问题...'):
            try:
                # 向 FastAPI 后端发送请求
                response = requests.post("http://law_chatbot:8000/ask", json={"query": user_input})

                # 处理不同的响应状态码
                if response.status_code == 200:
                    # 如果状态码是 200，显示答案
                    answer = response.json().get("answer", "抱歉，未找到答案。")
                    st.success("答案:")
                    st.write(answer)
                elif response.status_code == 400:
                    # 如果状态码是 400，表示请求有问题（比如输入为空）
                    st.error("请求无效，可能是输入格式问题。请确保您的问题已正确提交。")
                else:
                    st.error(f"出现错误，状态码: {response.status_code}，请稍后再试。")

            except requests.exceptions.RequestException as e:
                # 捕获请求异常（如网络问题）
                st.error(f"请求失败: {e}")
    else:
        # 如果没有输入，提示用户
        st.warning("请输入您的问题以获取答案。")
