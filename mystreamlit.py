import streamlit as st
import geopandas as gpd 
from folium import Choropleth
import folium
import fiona
import pyogrio
from streamlit_folium import st_folium
# geopandas 라이브러리 불러오기
# geopandas의 read_file 함수로 데이터 불러오기
gdf_seoul_gu = gpd.read_file('C:/Users/junlo/Desktop/데이터시각/TL_SCCO_SIG.json')
gdf_seoul_gu

import chardet    #문자 인코딩을 감지하는데 사용되는 라이브러리
import pandas as pd

# 파일의 인코딩 감지
with open('C:/Users/junlo/Desktop/데이터시각/연령별_출산율_및_합계출산율_행정구역별__20241121103459.csv', 'rb') as file:
    result = chardet.detect(file.read())
    print(result['encoding'])  # 파일의 인코딩 출력

# 감지된 인코딩으로 파일 읽기 
df_seoul_pop = pd.read_csv(
    'C:/Users/junlo/Desktop/데이터시각/연령별_출산율_및_합계출산율_행정구역별__20241121103459.csv',
    encoding=result['encoding'],
    header=1
)
df_seoul_pop

df_seoul_pop.columns = ['행정구', '인구수']   #컬럼 네임 지정

df_seoul_pop

import folium  #대화형 지도를 생성하는데 사용되는 라이브러리

title = '시군구별 출생률' # 타이틀

# Folium 지도 생성
city_hall = [37.566345, 126.977893]
gu_map = folium.Map(
    location=city_hall,
    zoom_start=11,
    tiles='cartodbpositron'
)

# Choropleth 지도 추가
Choropleth(
    geo_data=gdf_seoul_gu,
    data=df_seoul_pop,
    columns=('행정구', '인구수'),
    key_on='feature.properties.SIG_KOR_NM',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='시군구별 출생률'
).add_to(gu_map)

# Streamlit 앱 인터페이스
st.title("시군구별 출생률을 시각화")
st.write("아래는 시군구별 출생률 지도 입니다.")

# Folium 지도 Streamlit에 렌더링
st_folium(gu_map, width=725, height=500)



