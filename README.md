# 🎨 Streamlit UI 컴포넌트 체험관

Streamlit의 모든 UI 컴포넌트를 한 곳에서 체험할 수 있는 종합적인 웹 애플리케이션입니다.

## 📋 주요 기능

### 🏠 홈
- 애플리케이션 소개 및 개요
- 샘플 데이터 미리보기

### 📝 입력 위젯
- **텍스트 입력**: `st.text_input()`, `st.text_area()`, `st.text_input(type="password")`
- **숫자 입력**: `st.number_input()`, `st.slider()`, 범위 슬라이더
- **선택 위젯**: `st.selectbox()`, `st.multiselect()`, `st.radio()`, `st.checkbox()`
- **날짜/시간**: `st.date_input()`, `st.time_input()`, `st.color_picker()`

### 📊 데이터 표시
- **데이터프레임**: `st.dataframe()`, `st.table()`
- **메트릭**: `st.metric()` - 주요 지표 표시
- **JSON**: `st.json()` - JSON 데이터 시각화

### 📈 차트 & 그래프
- **기본 차트**: `st.line_chart()`, `st.area_chart()`, `st.bar_chart()`
- **Plotly 차트**: 산점도, 파이 차트 등 인터랙티브 차트
- **지도**: `st.map()` - 지리적 데이터 시각화

### 🖼️ 미디어
- **이미지**: `st.image()` - 이미지 표시 및 업로드
- **오디오**: `st.audio()` - 오디오 파일 재생
- **비디오**: `st.video()` - 비디오 파일 재생
- **파일 업로드**: `st.file_uploader()` - 다양한 파일 형식 지원

### 📋 레이아웃
- **컬럼**: `st.columns()` - 다중 컬럼 레이아웃
- **컨테이너**: `st.container()` - 요소 그룹화
- **익스팬더**: `st.expander()` - 접을 수 있는 섹션
- **탭**: `st.tabs()` - 탭 기반 네비게이션

### 🎯 상태 & 제어
- **버튼**: `st.button()` - 다양한 스타일의 버튼
- **다운로드**: `st.download_button()` - 파일 다운로드
- **진행률**: `st.progress()` - 진행 상황 표시
- **상태 메시지**: `st.success()`, `st.info()`, `st.warning()`, `st.error()`
- **특수 효과**: `st.balloons()`, `st.snow()`

### 🔧 유틸리티
- **코드 표시**: `st.code()` - 구문 강조 코드 블록
- **마크다운**: `st.markdown()` - 마크다운 렌더링
- **LaTeX**: `st.latex()` - 수학 공식 렌더링
- **공간 제어**: `st.empty()` - 레이아웃 조정

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone <repository-url>
cd streamlit_ui-1
```

### 2. 가상환경 생성 (권장)
```bash
# Windows
python -m venv venv
venv\\Scripts\\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 애플리케이션을 사용할 수 있습니다.

## 📦 필요한 패키지

- **streamlit**: 웹 애플리케이션 프레임워크
- **pandas**: 데이터 처리 및 분석
- **numpy**: 수치 연산
- **plotly**: 인터랙티브 차트 생성
- **matplotlib**: 기본 차트 생성
- **seaborn**: 통계 시각화
- **Pillow**: 이미지 처리
- **requests**: HTTP 요청 처리

## 🎯 사용법

1. **네비게이션**: 왼쪽 사이드바에서 원하는 컴포넌트 카테고리를 선택합니다.
2. **상호작용**: 각 페이지에서 다양한 위젯들과 상호작용해보세요.
3. **실시간 업데이트**: 입력값 변경 시 실시간으로 결과가 업데이트됩니다.
4. **파일 업로드**: 이미지, 오디오, 비디오 파일을 업로드하여 테스트할 수 있습니다.

## 🌟 주요 특징

- **완전한 한국어 지원**: 모든 인터페이스가 한국어로 제공됩니다.
- **실용적인 예제**: 실제 사용 사례를 반영한 예제들
- **반응형 디자인**: 다양한 화면 크기에 대응
- **상세한 주석**: 모든 코드에 한국어 주석 포함
- **즉시 실행 가능**: 별도 설정 없이 바로 실행 가능

## 🔧 커스터마이징

`app.py` 파일을 수정하여 다음과 같은 커스터마이징이 가능합니다:

- 새로운 컴포넌트 추가
- 기존 예제 수정
- 스타일링 변경
- 추가 데이터 소스 연결

## 📱 지원되는 브라우저

- Chrome (권장)
- Firefox
- Safari
- Edge

## 🤝 기여하기

이 프로젝트에 기여하고 싶으시다면:

1. Fork this repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 📞 지원

문제가 발생하거나 질문이 있으시면 이슈를 생성해주세요.

---

**🎨 Streamlit UI 컴포넌트 체험관으로 Streamlit의 모든 기능을 탐험해보세요!**
