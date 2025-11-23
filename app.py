import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, time
import requests
from PIL import Image
import io
import base64

# 페이지 설정
st.set_page_config(
    page_title="Streamlit UI 컴포넌트 체험관",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 메인 타이틀
st.title("🎨 Streamlit UI 컴포넌트 체험관")
st.markdown("---")

# 사이드바 네비게이션
st.sidebar.title("🧭 네비게이션")
st.sidebar.markdown("**체험할 컴포넌트 카테고리를 선택하세요:**")
st.sidebar.markdown("")  # 공백 추가

# 메뉴 옵션 리스트
menu_options = [
    "🏠 홈",
    "📝 입력 위젯",
    "📊 데이터 표시",
    "📈 차트 & 그래프",
    "🖼️ 미디어",
    "📋 레이아웃",
    "🎯 상태 & 제어",
    "🔧 유틸리티"
]

# 세션 상태 초기화 (현재 선택된 페이지 저장)
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 홈"

# 메뉴 스타일링을 위한 CSS 추가
st.sidebar.markdown("""
    <style>
    /* 버튼 스타일 개선 */
    .stButton > button {
        width: 100%;
        text-align: left;
        padding: 10px 15px;
        margin: 2px 0;
        border-radius: 8px;
        border: 2px solid #e0e4e8;
        background-color: #f8f9fa;
        color: #1f2937;
        font-size: 15px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #e9ecef;
        border-color: #1f77b4;
        transform: translateX(5px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    /* 선택된 버튼 스타일 */
    .stButton > button[kind="primary"] {
        background-color: #1f77b4;
        color: white;
        border-color: #1f77b4;
        font-weight: 600;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #1a5f8f;
        border-color: #1a5f8f;
    }
    </style>
""", unsafe_allow_html=True)

# 각 메뉴 항목을 버튼으로 표시
for option in menu_options:
    # 현재 선택된 페이지인지 확인
    is_selected = (st.session_state.current_page == option)
    
    # 버튼 타입 설정 (선택된 항목은 primary, 나머지는 secondary)
    button_type = "primary" if is_selected else "secondary"
    
    # 버튼 클릭 시 해당 페이지로 이동
    if st.sidebar.button(option, key=option, type=button_type, use_container_width=True):
        st.session_state.current_page = option

# 현재 선택된 페이지 사용
page = st.session_state.current_page

def show_footer():
    """페이지 하단에 푸터 정보를 표시하는 함수"""
    st.markdown("---")
    # 푸터 정보를 한 줄로 중앙 정렬하여 표시 (영어)
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 20px 0; font-size: 14px;'>
            Last updated: 2025.11.23 | Created by NaYoung Kim | © 2025 NaYoung Kim. All rights reserved.
        </div>
        """,
        unsafe_allow_html=True
    )

def show_home():
    """홈 페이지를 표시하는 함수"""
    st.header("🏠 Streamlit UI 컴포넌트 체험관에 오신 것을 환영합니다!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📝 **입력 위젯**\n\n사용자 입력을 받는 다양한 위젯들을 체험해보세요.")
    
    with col2:
        st.success("📊 **데이터 표시**\n\n데이터를 표시하는 다양한 방법들을 알아보세요.")
    
    with col3:
        st.warning("📈 **차트 & 그래프**\n\n시각화를 위한 다양한 차트들을 체험해보세요.")
    
    st.markdown("---")
    
    # 샘플 데이터프레임
    st.subheader("📋 샘플 데이터")
    sample_data = pd.DataFrame({
        '이름': ['김철수', '이영희', '박민수', '최지영', '정다은'],
        '나이': [25, 30, 35, 28, 32],
        '직업': ['개발자', '디자이너', '기획자', '마케터', '분석가'],
        '급여': [5000, 4500, 5500, 4200, 5800]
    })
    st.dataframe(sample_data, width='stretch')
    
    # 푸터 표시
    show_footer()

def show_input_widgets():
    """입력 위젯들을 보여주는 함수"""
    st.header("📝 입력 위젯 컴포넌트")
    
    # 텍스트 입력
    st.subheader("📄 텍스트 입력")
    col1, col2 = st.columns(2)
    
    with col1:
        # 일반 텍스트 입력
        text_input = st.text_input("텍스트 입력", "기본값을 입력하세요")
        st.write(f"입력된 텍스트: {text_input}")
        
        # 패스워드 입력
        password = st.text_input("패스워드 입력", type="password")
        if password:
            st.write("패스워드가 입력되었습니다 🔒")
    
    with col2:
        # 텍스트 영역
        text_area = st.text_area("텍스트 영역", "여러 줄의\n텍스트를\n입력할 수 있습니다")
        st.write(f"입력된 텍스트 길이: {len(text_area)}자")
    
    st.markdown("---")
    
    # 숫자 입력
    st.subheader("🔢 숫자 입력")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # 숫자 입력
        number = st.number_input("숫자 입력", min_value=0, max_value=100, value=50)
        st.write(f"입력된 숫자: {number}")
    
    with col2:
        # 슬라이더
        slider_val = st.slider("슬라이더", 0, 100, 25)
        st.write(f"슬라이더 값: {slider_val}")
    
    with col3:
        # 범위 슬라이더
        range_val = st.slider("범위 슬라이더", 0, 100, (20, 80))
        st.write(f"범위: {range_val[0]} ~ {range_val[1]}")
    
    st.markdown("---")
    
    # 선택 위젯
    st.subheader("🎯 선택 위젯")
    col1, col2 = st.columns(2)
    
    with col1:
        # 셀렉트박스
        option = st.selectbox(
            "선택 옵션",
            ["옵션 1", "옵션 2", "옵션 3", "옵션 4"]
        )
        st.write(f"선택된 옵션: {option}")
        
        # 멀티셀렉트
        multi_option = st.multiselect(
            "다중 선택",
            ["Python", "JavaScript", "Java", "C++", "Go"],
            default=["Python"]
        )
        st.write(f"선택된 언어들: {multi_option}")
    
    with col2:
        # 라디오 버튼
        radio = st.radio(
            "라디오 선택",
            ["선택지 A", "선택지 B", "선택지 C"]
        )
        st.write(f"라디오 선택: {radio}")
        
        # 체크박스
        checkbox = st.checkbox("체크박스", value=True)
        if checkbox:
            st.write("✅ 체크박스가 선택되었습니다")
        else:
            st.write("❌ 체크박스가 선택되지 않았습니다")
    
    st.markdown("---")
    
    # 날짜/시간 입력
    st.subheader("📅 날짜 및 시간 입력")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # 날짜 입력
        date_input = st.date_input("날짜 선택", date.today())
        st.write(f"선택된 날짜: {date_input}")
    
    with col2:
        # 시간 입력
        time_input = st.time_input("시간 선택", time(12, 30))
        st.write(f"선택된 시간: {time_input}")
    
    with col3:
        # 색상 선택
        color = st.color_picker("색상 선택", "#FF6B6B")
        st.write(f"선택된 색상: {color}")
        # 색상 미리보기
        st.markdown(f'<div style="width:100px; height:50px; background-color:{color}; border:1px solid #ccc;"></div>', unsafe_allow_html=True)
    
    # 푸터 표시
    show_footer()

def show_data_display():
    """데이터 표시 컴포넌트들을 보여주는 함수"""
    st.header("📊 데이터 표시 컴포넌트")
    
    # 샘플 데이터 생성
    df = pd.DataFrame({
        '제품명': ['노트북', '마우스', '키보드', '모니터', '스피커'],
        '가격': [1200000, 50000, 120000, 300000, 80000],
        '재고': [15, 50, 30, 8, 25],
        '평점': [4.5, 4.2, 4.8, 4.6, 4.1],
        '출시일': pd.date_range('2023-01-01', periods=5, freq='2ME')
    })
    
    # 데이터프레임
    st.subheader("📋 데이터프레임")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**기본 데이터프레임:**")
        st.dataframe(df)
    
    with col2:
        st.write("**스타일링된 데이터프레임:**")
        st.dataframe(
            df.style.highlight_max(axis=0),
            width='stretch'
        )
    
    st.markdown("---")
    
    # 테이블
    st.subheader("📊 정적 테이블")
    st.table(df.head(3))
    
    st.markdown("---")
    
    # 메트릭
    st.subheader("📈 메트릭 표시")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("총 매출", "₩2,750,000", "12%")
    
    with col2:
        st.metric("주문 수", "156", "8")
    
    with col3:
        st.metric("평균 평점", "4.44", "0.1")
    
    with col4:
        st.metric("재고 총합", "128", "-12")
    
    st.markdown("---")
    
    # JSON 표시
    st.subheader("🔧 JSON 데이터")
    sample_json = {
        "사용자": {
            "이름": "김개발",
            "이메일": "kim@example.com",
            "권한": ["읽기", "쓰기", "수정"]
        },
        "설정": {
            "테마": "다크",
            "언어": "한국어",
            "알림": True
        }
    }
    st.json(sample_json)
    
    # 푸터 표시
    show_footer()

def show_charts():
    """차트 및 그래프 컴포넌트들을 보여주는 함수"""
    st.header("📈 차트 & 그래프 컴포넌트")
    
    # 샘플 데이터 생성
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    # 라인 차트
    st.subheader("📊 라인 차트")
    st.line_chart(chart_data)
    
    # 영역 차트
    st.subheader("📈 영역 차트")
    st.area_chart(chart_data)
    
    # 바 차트
    st.subheader("📊 바 차트")
    st.bar_chart(chart_data)
    
    st.markdown("---")
    
    # Plotly 차트
    st.subheader("🎨 Plotly 차트")
    col1, col2 = st.columns(2)
    
    with col1:
        # 산점도
        fig_scatter = px.scatter(
            x=np.random.randn(50),
            y=np.random.randn(50),
            title="산점도 차트",
            labels={'x': 'X축', 'y': 'Y축'}
        )
        st.plotly_chart(fig_scatter, width='stretch')
    
    with col2:
        # 파이 차트
        fig_pie = px.pie(
            values=[30, 25, 20, 15, 10],
            names=['A', 'B', 'C', 'D', 'E'],
            title="파이 차트"
        )
        st.plotly_chart(fig_pie, width='stretch')
    
    st.markdown("---")
    
    # 지도
    st.subheader("🗺️ 지도")
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [37.5665, 126.9780],
        columns=['lat', 'lon']
    )
    st.map(map_data)
    
    # 푸터 표시
    show_footer()

def show_media():
    """미디어 컴포넌트들을 보여주는 함수"""
    st.header("🖼️ 미디어 컴포넌트")
    
    # 이미지
    st.subheader("🖼️ 이미지 표시")
    col1, col2 = st.columns(2)
    
    with col1:
        # 샘플 이미지 생성 (NumPy 배열)
        image_array = np.random.randint(0, 255, (200, 200, 3), dtype=np.uint8)
        st.image(image_array, caption="랜덤 생성 이미지", width='stretch')
    
    with col2:
        # 파일 업로드
        uploaded_file = st.file_uploader("이미지 파일 업로드", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="업로드된 이미지", width='stretch')
        else:
            st.info("이미지 파일을 업로드해주세요")
    
    st.markdown("---")
    
    # 오디오 (샘플 URL)
    st.subheader("🎵 오디오")
    st.write("**샘플 오디오 URL:**")
    sample_audio_url = "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav"
    st.audio(sample_audio_url)
    
    # 오디오 파일 업로드
    audio_file = st.file_uploader("오디오 파일 업로드", type=['mp3', 'wav', 'ogg'])
    if audio_file is not None:
        st.audio(audio_file)
    
    st.markdown("---")
    
    # 비디오
    st.subheader("🎬 비디오")
    video_file = st.file_uploader("비디오 파일 업로드", type=['mp4', 'mov', 'avi'])
    if video_file is not None:
        st.video(video_file)
    else:
        st.info("비디오 파일을 업로드해주세요")
    
    # 푸터 표시
    show_footer()

def show_layout():
    """레이아웃 컴포넌트들을 보여주는 함수"""
    st.header("📋 레이아웃 컴포넌트")
    
    # 컬럼
    st.subheader("📐 컬럼 레이아웃")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("첫 번째 컬럼")
        st.write("이것은 첫 번째 컬럼입니다.")
    
    with col2:
        st.success("두 번째 컬럼")
        st.write("이것은 두 번째 컬럼입니다.")
    
    with col3:
        st.warning("세 번째 컬럼")
        st.write("이것은 세 번째 컬럼입니다.")
    
    st.markdown("---")
    
    # 컨테이너
    st.subheader("📦 컨테이너")
    with st.container():
        st.write("이것은 컨테이너 안의 내용입니다.")
        st.button("컨테이너 내부 버튼")
    
    st.markdown("---")
    
    # 익스팬더
    st.subheader("📂 익스팬더")
    with st.expander("클릭하여 확장"):
        st.write("숨겨진 내용이 여기에 표시됩니다!")
        st.image(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
    
    st.markdown("---")
    
    # 탭
    st.subheader("📑 탭")
    tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
    
    with tab1:
        st.write("첫 번째 탭의 내용입니다.")
        st.line_chart(np.random.randn(10, 2))
    
    with tab2:
        st.write("두 번째 탭의 내용입니다.")
        st.bar_chart(np.random.randn(10, 2))
    
    with tab3:
        st.write("세 번째 탭의 내용입니다.")
        st.area_chart(np.random.randn(10, 2))
    
    # 푸터 표시
    show_footer()

def show_status_control():
    """상태 및 제어 컴포넌트들을 보여주는 함수"""
    st.header("🎯 상태 & 제어 컴포넌트")
    
    # 버튼
    st.subheader("🔘 버튼")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("일반 버튼"):
            st.success("일반 버튼이 클릭되었습니다!")
    
    with col2:
        if st.button("주요 버튼", type="primary"):
            st.success("주요 버튼이 클릭되었습니다!")
    
    with col3:
        if st.button("보조 버튼", type="secondary"):
            st.success("보조 버튼이 클릭되었습니다!")
    
    st.markdown("---")
    
    # 다운로드 버튼
    st.subheader("📥 다운로드 버튼")
    sample_csv = pd.DataFrame({
        '이름': ['홍길동', '김철수', '이영희'],
        '나이': [25, 30, 35],
        '직업': ['개발자', '디자이너', '기획자']
    }).to_csv(index=False)
    
    st.download_button(
        label="CSV 파일 다운로드",
        data=sample_csv,
        file_name="sample_data.csv",
        mime="text/csv"
    )
    
    st.markdown("---")
    
    # 진행률 표시
    st.subheader("📊 진행률 표시")
    progress_bar = st.progress(0)
    
    if st.button("진행률 시뮬레이션"):
        import time
        for i in range(100):
            progress_bar.progress(i + 1)
            time.sleep(0.01)
        st.success("완료!")
    
    st.markdown("---")
    
    # 상태 메시지
    st.subheader("💬 상태 메시지")
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("성공 메시지")
        st.info("정보 메시지")
    
    with col2:
        st.warning("경고 메시지")
        st.error("오류 메시지")
    
    # 풍선 효과
    if st.button("축하 풍선 🎈"):
        st.balloons()
    
    # 눈 효과
    if st.button("눈 내리기 ❄️"):
        st.snow()
    
    # 푸터 표시
    show_footer()

def show_utilities():
    """유틸리티 컴포넌트들을 보여주는 함수"""
    st.header("🔧 유틸리티 컴포넌트")
    
    # 코드 표시
    st.subheader("💻 코드 표시")
    code = '''
def hello_streamlit():
    """Streamlit 인사 함수"""
    print("안녕하세요, Streamlit!")
    return "Hello, World!"

# 함수 실행
result = hello_streamlit()
    '''
    st.code(code, language='python')
    
    st.markdown("---")
    
    # 마크다운
    st.subheader("📝 마크다운")
    markdown_text = """
    ### 마크다운 예시
    
    - **굵은 글씨**
    - *기울임 글씨*
    - `인라인 코드`
    - [링크](https://streamlit.io)
    
    > 인용문입니다.
    
    | 컬럼1 | 컬럼2 | 컬럼3 |
    |-------|-------|-------|
    | 값1   | 값2   | 값3   |
    """
    st.markdown(markdown_text)
    
    st.markdown("---")
    
    # LaTeX
    st.subheader("🔢 LaTeX 수식")
    st.latex(r'''
    e^{i\pi} + 1 = 0
    ''')
    
    st.latex(r'''
    \sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
    ''')
    
    st.markdown("---")
    
    # 빈 공간
    st.subheader("📏 공간 제어")
    st.write("위 텍스트")
    st.empty()  # 빈 공간
    st.write("아래 텍스트")
    
    # 사이드바에 추가 정보
    st.sidebar.markdown("---")
    st.sidebar.info("💡 **팁**: 각 카테고리를 선택하여 다양한 Streamlit 컴포넌트들을 체험해보세요!")
    
    # 푸터 표시
    show_footer()

# 메인 애플리케이션 로직
if page == "🏠 홈":
    show_home()
elif page == "📝 입력 위젯":
    show_input_widgets()
elif page == "📊 데이터 표시":
    show_data_display()
elif page == "📈 차트 & 그래프":
    show_charts()
elif page == "🖼️ 미디어":
    show_media()
elif page == "📋 레이아웃":
    show_layout()
elif page == "🎯 상태 & 제어":
    show_status_control()
elif page == "🔧 유틸리티":
    show_utilities()

# 푸터
st.sidebar.markdown("---")
st.sidebar.markdown("**🎨 Streamlit UI 컴포넌트 체험관**")
st.sidebar.markdown("모든 Streamlit 컴포넌트를 한 곳에서!")
