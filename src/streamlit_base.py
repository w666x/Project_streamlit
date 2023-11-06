"""streamlit-页面设置

* 实现功能
    1. 页面配置，帮助信息
    2. 页边栏，列布局
    3. 打印告警、错误等文本信息
"""

from datetime import datetime
from numpy import empty, not_equal
import streamlit as st
import time
import pandas as pd
import numpy as np
import streamlit.components.v1 as components


if __name__ == '__main__':
    about_message = '''
    # Are you ok
    ## this is a test
    :smile:
    '''

    st.set_page_config(
        page_title="Streamlit base",
        page_icon="../docs/source/savefig/about_demo.jpg",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://www.baidu.com/',
            'Report a bug': None,
            'About': about_message
        }
    )

    st.header("Streamlit Demo")
    # 图片引用
    st.image("../docs/source/savefig/about_demo.jpg")

    # 边栏
    add_selectbox = st.sidebar.selectbox(
        label="How would you like to be contacted?",
        options=("Email", "Home phone", "Mobile phone"),
        key="t1"
    )

    add_selectbox2 =  st.sidebar.selectbox(
        label="How would you like to be contacted?",
        options=("Email", "Home phone", "Mobile phone"),
        key="t2"
    )

    # 列布局
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("pic1")
        st.image("../docs/source/savefig/about_demo.jpg")

    with col2:
        st.header("pic2")
        st.image("../docs/source/savefig/about_demo.jpg")

    with col3:
        st.header("pic3")
        st.image("../docs/source/savefig/about_demo.jpg")

    #放气球
    #st.balloons()

    #错误信息
    st.error('error！💀')

    #警告信息
    st.warning("warning! :warning:")

    #信息
    st.info('message ℹ')

    #成功
    st.success("success 🎉")

    #exception
    e = RuntimeError("an exception")
    st.exception(e)

    #stop
    name = st.text_input('Name')
    if not name:
        st.warning('Please input a name.')
        st.stop()
    st.success('Thank you for inputting a name.')

