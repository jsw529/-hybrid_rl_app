import streamlit as st
import openai

st.set_page_config(page_title='AI GPT 튜터', layout='centered')
st.title('🎓 ChatGPT 학습 도우미')

# GPT API 연결
openai.api_key = st.secrets['OPENAI_API_KEY']

st.subheader('✏️ 궁금한 점을 입력하세요')
user_input = st.text_input('예: 벡터와 행렬의 차이가 뭐예요?', '')

if st.button('AI에게 질문하기'):
    if user_input.strip() != '':
        with st.spinner('AI 튜터가 답변 중입니다...'):
            try:
                response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo',
                    messages=[
                        {"role": "system", "content": "너는 친절하고 똑똑한 학습 도우미야."},
                        {"role": "user", "content": user_input}
                    ]
                )
                answer = response['choices'][0]['message']['content']
                st.success(answer)
            except Exception as e:
                st.error(f"에러 발생: {str(e)}")
    else:
        st.warning('질문을 입력해주세요!')