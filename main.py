import streamlit as st
from datetime import datetime, timedelta
import random

# 앱의 타이틀 설정
st.title('남은 일자 조회하기 ✅')

# 사용자 인터페이스
# 사용자로부터 핸드폰 번호 입력 받기
phone_number = st.text_input('핸드폰 번호를 입력하세요', '')

# 버튼을 클릭했을 때 작동
if st.button('조회'):
    if phone_number:
        # 데모용으로 랜덤 남은 일자 생성
        remaining_days = random.randint(1, 365)
        # 남은 일자 출력
        st.success(f'핸드폰 번호 {phone_number}의 남은 일자는 {remaining_days}일입니다.')
    else:
        st.error('핸드폰 번호를 입력해주세요.')

# 사이드바 예제
st.sidebar.header('안내')
st.sidebar.text('공생마케팅을 통해서 계약하신 서비스의')
st.sidebar.text('잔여일을 조회할 수 있습니다.')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            <meta name="공생마케팅 남은 일자 조회하기" content="남은 서비스 일자를 조회하세요:)" />
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
