import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. API 설정 (지은이 키로 꼭 바꿔줘!)
genai.configure(api_key="AIzaSyBHPDNvnmErSBU6TxsBSueKeKZnOZx0Wxw")
model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')

# 2. 앱 화면 꾸미기
st.set_page_config(page_title="지은 AI", page_icon="📱")
st.title("✨ 지은이의 비밀 챗봇")

# 3. 대화 저장용 메모리 만들기
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 4. 왼쪽 사이드바에 사진 올리기 버튼
with st.sidebar:
    st.header("📸 사진/파일")
    img_file = st.file_uploader("이미지를 선택해줘", type=['jpg', 'png', 'jpeg'])

# 5. 채팅창 보여주기
for content in st.session_state.chat.history:
    role = "assistant" if content.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(content.parts[0].text)

# 6. 질문 입력받기
if prompt := st.chat_input("무엇이든 물어봐!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 사진이 있으면 사진이랑 같이, 없으면 글자만!
    if img_file:
        img = Image.open(img_file)
        response = model.generate_content([prompt, img])
    else:
        response = st.session_state.chat.send_message(prompt)
        
    with st.chat_message("assistant"):
        st.markdown(response.text)
