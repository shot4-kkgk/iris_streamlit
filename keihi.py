import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

st.sidebar.header('新規入力')
name = st.sidebar.text_input('氏名')
category = st.sidebar.text_input('費目')
amount = st.sidebar.text_input('費用')
tax = st.sidebar.text_input('消費税')
approval = st.sidebar.text_input('承認済み')

st.title('入力結果')
'氏名：' , name
'費目：' , category
'費用：' , amount
'消費税：' , tax
'承認済み：' , approval

st.title('経費一覧')

df = pd.DataFrame({
    '氏名' : ['木村太郎', '小林翔一', '松本涼', '木下駿', '高良祐果', '竹内正幸', '佐藤一樹', '上村雅人', '塚井綾香', '柳澤礼美'],
    '費目' : ['新聞図書費', '交通費', 'ソフトウェア', '交際費', '交際費', '交通費', '新聞図書費', '新聞図書費', 'ソフトウェア', '交際費'],
    '費用' : [3000, 900, 15000, 10000, 8000, 400, 2500, 900, 900, 3000],
    '消費税' : [300, 90, 1500, 1000, 800, 40, 250, 90, 90, 300],
    '承認' : ['あり', 'なし', 'なし', 'あり', 'あり', 'なし', 'あり', 'なし', 'なし', 'あり']
})
df = df.rename(index=lambda x: x + 1)
df.index.name = 'No'

st.write(df)