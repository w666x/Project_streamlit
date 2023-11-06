"""streamlit-优化问题

* streamlit速度比较慢，咋处理嘞
    1. st.empty()创建1个空的元素占位，用于后续更新时展示结果
    2. 在触发器上使用@st.cache装饰器来缓存结果，避免重复计算
        - @st.cache：比较早的实现方式了，当前版本已经deprecated了
        - @st.cache_data：在每次函数调用时创建一个新的数据副本；**只有在第一次执行的时候才会读数，其他时间直接从缓存拿数据**
        - @st.cache_resource：是缓存诸如 ML 模型或数据库连接之类的全局资源（不想多次加载的对象）的推荐方法，全局共享哦
    3. 在异步操作中，使用with st.spinner()来显示加载状态
    4. 在异步操作完成后，使用empty_elem.write()来更新结果
"""

from datetime import datetime
from numpy import empty, not_equal
import streamlit as st
import time
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from functools import wraps


def timer(func):
    """time装饰器
    
    打印脚本执行时间的啦
    """
    @wraps(func)
    def wrap(*args, **kwargs):
        begin_time = int(time.time() * 1000)
        result = func(*args, **kwargs)
        start_time = int(time.time() * 1000)
        print('func:%r took: %2.4f ms' % (func.__name__, start_time - begin_time))
        return result
    return wrap


if __name__ == '__main__':
    # 1) empty
    with st.empty():
       st.write("not empty here")    
    empty = st.empty()
    empty.text("still not empty")
    time.sleep(3) #替换
    empty.text("change")
    time.sleep(1) #清除
    empty.empty()

    st.header("cache 测试啦")
    
    # 2) cache
    @timer
    @st.cache_data
    def fetch_and_clean_data(url):
        """同一地址请求，第二次会从缓存取数"""
        df = pd.read_csv(url)
        return df

    df1 = fetch_and_clean_data("../datas/predict_result_bak_20200901.csv")
    st.table(df1.head())
    df1 = fetch_and_clean_data("../datas/predict_result_bak_20200901.csv")
    st.table(df1.head())
    df1 = fetch_and_clean_data("../datas/predict_result_bak_20200902.csv")
    st.table(df1.head())    

    @timer
    @st.cache_resource(ttl=10800)  # 3小时过期
    def fetch_data(url):
        """全局的哦直接，不会多次加载执行"""
        df = pd.read_csv(url)
        return df

    df2 = fetch_data("../datas/predict_result_bak_20200901.csv")
    st.table(df2.head())
    df2 = fetch_data("../datas/predict_result_bak_20200901.csv")
    st.table(df2.head())
    df2 = fetch_data("../datas/predict_result_bak_20200902.csv")
    st.table(df2.head())   
    
    st.button("Rerun")


    # 3) spinner
    with st.spinner('Wait for it...'):
       time.sleep(3)
    st.success('Done!')

    # 4) 往empty占位位置写入数据
    empty.write(df2.head())