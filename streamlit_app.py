import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import openai

# GPT 키 불러오기
openai.api_key = st.secrets["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"]

st.set_page_config(page_title="AI 하이브리드 학습 플랫폼", layout="centered")
st.title("🤖 AI 맞춤형 학습 대시보드 (강화학습 + GPT 튜터)")

# 세션 상태 초기화
if 'progress' not in st.session_state:
    st.session_state.progress = 0
if 'quiz_scores' not in st.session_state:
    st.session_state.quiz_scores = []

# -----------------------
# 진행률 및 점수 시뮬레이션
# -----------------------
st.subheader("📊 학습 진행률")
progress_bar = st.progress(st.session_state.progress)

if st.button("학습 진행 시뮬레이션 시작"):
    for i in range(st.session_state.progress, 101, 5):
        st.session_state.progress = i
        progress_bar.progress(i)
        st.session_state.quiz_scores.append(np.random.randint(80, 100))
        time.sleep(0.1)

st.markdown(f"현재 학습 진도: **{st.session_state.progress}%**")

# -----------------------
# GPT 질문 섹션
# -----------------------
st.subheader("🧠 AI 튜터에게 질문하기")
user_input = st.text_input("궁금한 점이나 의견을 입력하세요")

if st.button("AI에게 질문하기"):
    if user_input.strip() != '':
        with st.spinner("AI 튜터가 답변 중입니다..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "너는 친절하고 똑똑한 학습 도우미야."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response["choices"][0]["message"]["content"]
                st.success(answer)
            except Exception as e:
                st.error(f"에러 발생: {str(e)}")
    else:
        st.warning("질문을 입력해주세요!")

# -----------------------
# 점수 그래프 출력
# -----------------------
st.subheader("📈 퀴즈 점수 추적 (강화학습 기반)")
if st.session_state.quiz_scores:
    fig, ax = plt.subplots()
    ax.plot(range(1, len(st.session_state.quiz_scores)+1), st.session_state.quiz_scores, marker='o')
    ax.set_xlabel("시도 횟수")
    ax.set_ylabel("점수")
    ax.set_title("퀴즈 점수 변화 추적")
    st.pyplot(fig)
else:
    st.info("진행률을 시뮬레이션하면 점수가 생성됩니다.")
