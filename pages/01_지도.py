import streamlit as st
import folium
from streamlit.components.v1 import html

# 한국 인기 관광지 Top 10 (예시 좌표)
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

st.title("한국 인기 지역 Top 10 지도")

# Folium 지도 생성 (중심 좌표는 한국 중앙)
m = folium.Map(location=[36.5, 127.8], zoom_start=6)

# 마커 추가
for loc in locations:
    folium.Marker([loc["lat"], loc["lon"]], popup=loc["name"]).add_to(m)

# folium HTML 렌더링
m_html = m.get_root().render()

# Streamlit에 삽입
html(m_html, height=600)
