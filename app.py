import streamlit as st
import google.generativeai as genai

# 1. 화면 설정
st.set_page_config(page_title="지은이의 비밀 챗봇", page_icon="✨")

# 2. 지은이의 유료 열쇠 (여기에 API 키 꼭 넣어줘!)
genai.configure(api_key="지은이의_진짜_API_키_넣기")

# 3. 모델 설정 (가장 안전하고 똑똑한 이름으로 변경!)
# 'gemini-1.5-pro-latest'라고 쓰면 무조건 최신 3.1급 지능을 찾아와!
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest", 
    system_instruction="너는 지은이가 만든 가장 똑똑한 AI 친구야. 지은이는 대학생이고 겐신 임팩트를 좋아해. 항상 다정하게 말해줘!"
)

st.title("✨ 지은이의 비밀 챗봇")

# 4. 채팅 기억 주머니
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. 채팅방 예쁘게 보여주기 (지은이는 오른쪽, AI는 왼쪽!)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. 무엇이든 물어봐!
if prompt := st.chat_input("지은아, 궁금한 게 뭐야?"):
    # 지은이 말 (오른쪽)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 대답 (왼쪽)
    try:
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"지은아 미안해, 잠시 문제가 생겼어: {e}")
