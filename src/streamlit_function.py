"""streamlit-基础方法

* 实现功能
    1. 相关组件，包括按钮、勾选框、滑动条、 **输入框和上传下载按钮以及图片音频链接应用部分**
    2. form表单，可嵌套滑动条
    3. 打印字典、altair图、table表格
    4. 表情包、魔术方法、进度条
"""

from datetime import datetime
from numpy import empty, not_equal
import streamlit as st
import time
import pandas as pd
import numpy as np
import streamlit.components.v1 as components


def t1():
    """测试on_change或 on_click"""
    st.text("t1-ing!")


if __name__ == '__main__':
    '''# 组件'''
    # 勾选框
    a = st.checkbox('test_checkbox', value=False, key=None, help="你猜呀", on_change=None, args=None, kwargs=None)
    # 按钮
    b = st.button(label="button", key=None, help="你猜呀", on_click=None)
    # 下载按钮
    c = st.download_button(label="download_button", data='testttt', file_name='test_.md', help='你猜呀', on_click=None)
    # 单选框
    d = st.radio(label="What's your favorite movie genre",options=('Comedy', 'Drama', 'Documentary'),index=2, help='你猜呀')
    # 下拉选项
    e = st.selectbox('slectbox',('Comedy', 'Drama', 'Documentary'),index=2, help='你猜呀')
    # 多选
    f = st.multiselect('multiselect',('Comedy', 'Drama', 'Documentary'), default=['Drama'], help='你猜呀')
    # 滑动条
    g = st.slider(label="slider", min_value=-10, max_value=10, value=-2, step=1, help="你猜呀", on_change=t1)
    # 选择滑动条
    h = st.select_slider(label='select_slider', options=[1,'test2',3], value=3, help="你猜呀")
    # 文本框
    i = st.text_input(label='text_input', max_chars=30, value='test1', help='你猜呀', placeholder='请输入')
    # 数字选择框
    j = st.number_input("number_input", min_value=-10, max_value=10, value=2, step=2, help="testing")
    # 文本区域
    k = st.text_area("text_area", value="test1",max_chars=60, help="你猜呀", placeholder="请输入")
    # 时间选择
    dt1 = datetime.today()
    dt2 = datetime.today()
    l = st.date_input(label="date_input", value=(dt1,dt2))
    # 时间选择
    m = st.time_input("time_input", value=None, help="你猜呀")
    # 上传按钮
    n = st.file_uploader(label='file_uploader', accept_multiple_files=True, help="你猜呀")
    # 拾色器
    o = st.color_picker('color_picker', '#00f900')
    # 图片
    p = st.image(image=['https://i.bmp.ovh/imgs/2021/10/3fd6c4674301c708.jpg',"./data/testimage.jpg"])
    # 音频
    q = st.audio("http://music.163.com/song/media/outer/url?id=1901371647.mp3")
    # 视频
    # html外链
    #arg = "<iframe src=\"//player.bilibili.com/player.html?aid=376524564&bvid=BV1wo4y1X7Tk&cid=365010431&page=1\" scrolling=\"yes\" border=\"100\" frameborder=\"yes\" framespacing=\"0\" allowfullscreen=\"true\"> </iframe>"
    #r = st.markdown(unsafe_allow_html=True, body=arg)
    #iframe conponent
    components.iframe(src="//player.bilibili.com/player.html?aid=376524564&bvid=BV1wo4y1X7Tk&cid=365010431&page=1", width=1080, height=720, scrolling=False)
    # video
    r = st.video("./data/testybb.mp4")
    # 展开框
    with st.expander(label="expander", expanded=False):
        st.write("展开框测试")
    #container
    with st.container():
        st.dataframe("container")
    container = st.container()
    container.write("containertext1")
    st.write("not container")
    #在container中继续调用组件
    container.write("containertext2")

    # 打印字典
    import pandas as pd
    st.write(pd.read_csv)
    st.write({"a": 123, "b":31})

    # 打印altair图
    import altair as alt
    import streamlit as st
    import pandas as pd
    import numpy as np
   
    df = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])
    c = alt.Chart(df).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
    st.write(c)


    #form表单
    with st.form(key="my_form1"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        #提交
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
        st.write("Outside the form")

    form = st.form(key="my_form2")
    form.slider("Inside the form")
    form.form_submit_button("Submit")

    # echo打印
    with st.echo("below"):
        st.write('This code will be printed')

    # help
    st.help(st.help)

    # 表格
    df1 = pd.DataFrame(
        np.random.randn(1, 5),
        columns=('col %d' % i for i in range(5)))
    my_table = st.table(df1)
    df2 = pd.DataFrame(
        np.random.randn(2, 5),
        columns=('col %d' % i for i in range(5)))
    my_table.add_rows(df2)

    # 表情包
    st.markdown(":smile:😁")
    st.text("😁")

    # 文字哦
    st.text(type(r))

    # 魔术方法
    # Draw a title and some text to the app:
    '''
    # This is the document title

    This is some _markdown_.
    '''
    df = pd.DataFrame({'col1': [1,2,3]})
    df  # <-- Draw the dataframe
    x = 10
    'x', x  # <-- Draw the string 'x' and then the value of x
    st.success("success 🎉")    


    # 进度条
    import time
    my_bar = st.progress(100)

    for percent_complete in range(100).__reversed__():
        time.sleep(0.01)
        my_bar.progress(percent_complete)