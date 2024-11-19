import streamlit as st
 # 텍스트
st.header('🚗 텍스트 출력')
st.write('') # 빈 줄 삽입

st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')

st.title('제목 : st.title()') 
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')
st.markdown('마크다운 : st.markdown()')
st.markdown('''
 1. ordered item- unordered item- unordered item
 2. ordered item
 3. ordered item
 ''')
 
st.divider() # 구분선



