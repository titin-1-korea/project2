import streamlit as st
import pandas as pd

# 한국 인기 지역 Top 10 좌표 데이터
locations = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052},
    {"name": "대구", "lat": 35.8714, "lon": 128.6014},
    {"name": "광주", "lat": 35.1595, "lon": 126.8526},
    {"name": "대전", "lat": 36.3504, "lon": 127.3845},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761},
    {"name": "속초", "lat": 38.2048, "lon": 128.5911},
]

# DataFrame으로 변환 및 열 이름 변경
df = pd.DataFrame(locations)
df = df.rename(columns={"lat": "latitude", "lon": "longitude"})

# Streamlit 앱 제목
st.title("한국 인기 지역 Top 10 지도 (folium 없이)")

# st.map()으로 지도 출력
st.map(df)

# 데이터 테이블로 보여주기
st.subheader("지역 리스트")
st.table(df[["name", "latitude", "longitude"]])
