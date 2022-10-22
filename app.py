import yfinance as yf
import streamlit as st
import datetime
import plotly.graph_objects as go

st.write("# 주식 차트")

# ticker = "TSLA"
ticker = st.text_input("티커 입력 >> ")
data = yf.Ticker(ticker) # Ticker : 주식시장에서의 이름
today = datetime.datetime.today().strftime("%Y-%m-%d")
df = data.history(period="1d", start="2015-01-01", end=today)   # 기간 -> 하루
st.dataframe(df)

st.write("## 종가 기준")
st.line_chart(df["Close"])

st.write("## 거래량 기준")
st.bar_chart(df["Volume"])

st.write("## 캔들 차트")
candle = go.Candlestick(x=df.index, open=df["Open"], close=df["Close"], high=df["High"], low=df["Low"])
layout = go.Layout(yaxis={"fixedrange":False}) #그래프 옵션 변경
fig = go.Figure(data=[candle], layout=layout) # 피규어 안에 리스트 변수로 캔들을 넣어줌
st.plotly_chart(fig) # 웹페이지에서 띄우기 위해 plotly_chart사용


