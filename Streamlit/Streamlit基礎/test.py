import streamlit
import numpy
import pandas
from PIL import Image
import time

streamlit.title('超入門')

latest_itaration = streamlit.empty()
bar = streamlit.progress(0)

for i in range(100):
    latest_itaration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

streamlit.write('DataFrame')

df = pandas.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

streamlit.write(df)
# 動的、引数により表サイズやハイライトを指定できる
streamlit.dataframe(df,width=500,height=200)
streamlit.dataframe(df.style.highlight_max(axis=0),width=500,height=200)
# 静的な表を作成
streamlit.table(df.style.highlight_max(axis=0))

"""
# タイトル1
## タイトル2
```py
import streamlit
import numpy
import pandas
```
"""

df=pandas.DataFrame(
    numpy.random.rand(20,3),
    columns=['1','2','3']
)

streamlit.line_chart(df)
streamlit.area_chart(df)

df = pandas.DataFrame(
    numpy.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)
# streamlit.map(df)

streamlit.write('Display Image')

if streamlit.checkbox('Show Image'):
    img = Image.open('test.jpg')
    streamlit.image(img,caption='white-bear',use_column_width=True)

option = streamlit.selectbox(
    'あなたの好きな数字は？',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です'

# text = streamlit.sidebar.text_input('あなたの趣味は？')
# 'あなたの趣味：',text

# condition = streamlit.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition


left_column, right_column = streamlit.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander = streamlit.expander('問い合わせ')
expander.write('問い合わせの回答')

