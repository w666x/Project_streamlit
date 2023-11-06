"""streamlit，可以非常快的搞出1个网页引用demo出来啦"""


## 项目内容说明

- 内容简介
    - streamlit方法介绍，包括函数、组件、常用命令等
    - 优化提高方式，streamlit速度较慢，总得提高下吧


### 方法概览

#### 方法简介

- Streamlit基于python脚本文件来实现网页应用，本质上，**是在整个python脚本上不断重复从头运行到结尾的过程**
- **两个if…else分支中的部分是完全隔离**，且通过按钮等方式运行一个又运行另一个时，其中一个的作用将完全不会对另一个分支产生任何影响，实际上Streamlit是从if…else语句的开头重新运行了这部分代码直到下一个暂停点
    - 比如，点击第一个按钮使得if…else进入第一个分支修改一个全局变量tmp的值（初始为 0），使其自增 1，随后点击另一个按钮进入另一个分支，使tmp再次自增 1，最终tmp的值会是 1，因为两个分支最终只会运行一个，即第二个分支，第一个分支的操作会被Streamlit回滚而取消
    - 另外，所有可交互的组件如按钮和勾选框，对其进行一次交互只是修改了一次它的状态，与其绑定的on_click函数仅在其被激活的状态下运行一次，其没有激活时(按钮点击一次后，点击其他交互组件即会自动退回未激活状态)与其绑定的on_click函数就会回撤而变为未运行过的状态
- 因此，基于Streamlit的这种从前到后的脚本运行的特性，很多应用程序的编写逻辑可能与其他框架不同，**当需要对某个数据反复修改时，需要考虑使用外部存储的方法**
- 内容参考自 [Streamlit中文文档（笔记）](https://blog.csdn.net/qq_31034569/article/details/122152973)


#### demo

- 任务说明
    - 指定端口为8882
    - 获取使用统计信息
    - 前端查询，不等待，直接刷新
    - 主题设置为黑色

```shell
streamlit run --server.port 8882 --browser.gatherUsageStats True --runner.fastReruns True --theme.base dark --theme.font 'sans serif' streamlit_function.py
```


#### 功能清单

- 功能方法汇总
    - 比较常用的命令哈，也就是 ``port、fastReruns、theme、logger``这些命令啦

| 是否常用 | 命令 | 命令分类 | 功能
|:-|:-|:-|:-
|  | `streamlit docs` | docs | 查看帮助文档
| 是 | `streamlit cache clear` | cache | 清空缓存
| 是 | `streamlit config show` | config | 打印配置文件
| 是 | `streamlit run streamlit_demo.py` | run | 运行文件啦
|  | `streamlit run --logger.level TEXT` | run | 设置日志等级，<br>值可以为，``error/warning/info/debug``.
| 是 | `streamlit run --runner.fastReruns BOOLEAN` | run |  快速返回结果，而不需要等待
|  | `streamlit run --server.address TEXT` | run |  设置server的地址
| 是 | `streamlit run --server.port INTEGER` | run |  设置server的端口
|  | `streamlit run --browser.serverAddress TEXT` | run |  用户连接APP的地址
|  | `streamlit run --browser.serverPort INTEGER` | run |  用户连接APP的端口
|  | `streamlit run --server.scriptHealthCheckEnabled BOOLEAN` | run |  脚本检查
|  | `streamlit run --browser.gatherUsageStats BOOLEAN` | run |  返回使用统计
|  | `streamlit run --theme.base TEXT` | run |  主题基础，可选择的为``light/dark``
|  | `streamlit run --theme.font TEXT` | run |  主题字体，可选择的为``sans serif/serif/monospace``


- 函数方法汇总简介
    - 打印基础信息

| 是否常用 | 命令  | 功能
|:-|:-|:-   
| 是 | ``st.dataframe(data=None, width=None, height=None)`` | 打印dataframe
| 是 | ``st.table(data=None)`` | 打印表格
|  | ``st.metric(label, value, delta=None, delta_color="normal")`` | 
|  | ``st.json(body)`` | 打印json数据
|  | ``st.caption(body)`` | 
| 是 | ``st.code(body, language="python")`` | 打印脚本
| 是 | ``st.text(body)`` | 打印纯文本
|  | ``st.latex(body)`` | 打印latex输入


### 详细方法介绍

#### 组件

- 包括按钮、勾选框、滑动条、 **输入框和上传下载按钮以及图片音频链接应用部分**

| 是否常用 | 命令 | 命令分类 | 功能
|:-|:-|:-|:-
| 是 | `st.checkbox('test_checkbox', value=False, key=None, help="你猜呀", on_change=None, args=None, kwargs=None)` |	box | 勾选框 |
| 是 | `st.button(label="button", key=None, help="你猜呀", on_click=None)` |	button | 按钮 |
| 是 | `st.download_button(label="download_button", data='testttt', file_name='test_.md', help='你猜呀', on_click=None)` |	button | 下载按钮 |
| 是 | `st.radio(label="What's your favorite movie genre",options=('Comedy', 'Drama', 'Documentary'),index=2, help='你猜呀')` | box 	 | 单选框 |
| 是 | `st.selectbox('slectbox',('Comedy', 'Drama', 'Documentary'),index=2, help='你猜呀')` | box 	 | 下拉选项 |
| 是 | `st.multiselect('multiselect',('Comedy', 'Drama', 'Documentary'), default=['Drama'], help='你猜呀')` |	box | 多选 |
| 是 | `st.slider(label="slider", min_value=-10, max_value=10, value=-2, step=1, help="你猜呀", on_change=t1)` |	slider | 滑动条 |
| 是 | `st.select_slider(label='select_slider', options=[1,'test2',3], value=3, help="你猜呀")` |	slider | 选择滑动条 |
| 是 | `st.text_input(label='text_input', max_chars=30, value='test1', help='你猜呀', placeholder='请输入')` |	input | 文本框 |
| 是 | `st.number_input("number_input", min_value=-10, max_value=10, value=2, step=2, help="testing")` |	input | 数字选择框 |
| 是 | `st.text_area("text_area", value="test1",max_chars=60, help="你猜呀", placeholder="请输入")` | input 	 | 文本区域 |
| 是 | `st.date_input(label="date_input", value=(dt1,dt2))` |	input | 时间选择 |
| 是 | `st.time_input("time_input", value=None, help="你猜呀")` | input 	 | 时间选择 |
| 是 | `st.file_uploader(label='file_uploader', accept_multiple_files=True, help="你猜呀")` |file_uploader	 | 上传按钮 |
| 是 | `st.color_picker('color_picker', '#00f900')` |	color_picker | 拾色器 |
|    | `st.image(image=['https:**.jpg',"./data/testimage.jpg"])` |	image | 图片 |
|    | `st.audio("http://**.mp3")` |	audio | 音频 |



#### st.write

- 方法简介
    - 将参数写入应用。这是 Streamlit 命令的瑞士军刀：它可根据你提供的内容完成不同的任务。
    - 与其他 Streamlit 命令不同，write（） 具有一些独特的属性：
        - 1. 您可以传入多个参数，所有这些参数都会被写入。
        - 2. 其行为取决于输入类型，如下表所示。
        - 3. **它返回 None，因此它在 App 中的“slots”不能重复使用。**

| 是否常用 | 命令  | 功能
|:-|:-|:-   
| 是 | write(string) | 打印markdown字符串 
| 是 | write(data_frame) | 将data_frame显示为表格  
|  | write(error)   | 打印错误
| 是 | write(func) | 打印一个函数的相关信息 
|  | write(module)  | 打印一个module的相关信息
|  | write(class) | 打印一个类的相关信息
| 是 | write(dict) | 打印字典
|  | write(mpl_fig)  | 打印Matplotlib图片
|  | write(altair)  | 打印 Altair 图表
|  | write(keras)  | 打印keras模型
| 是 | write(graphviz)  | 打印Graphviz图
|   | write(plotly_fig)  | 打印Plotly图
|   | write(bokeh_fig)  | 打印bokeh图
|   | write(sympy_expr)  | 使用 LaTeX 打印 SymPy 表达式
|  | write(htmlable)  | 打印html
|  | write(obj)  | 以str(obj)形式打印结果


#### magic

- 方法简介
    - **任何时候如果Streamlit看到一个变量或常量值， 它就会自动将其使用st.write写入应用。**
    - 另外，魔术命令也能够忽略docstrings，也就是说它会忽略文件和函数 头部的字符串。
    - 如下例所示，内容都是会被打印的哦

```python
# Draw a title and some text to the app:
'''
# This is the document title
This is some _markdown_.
'''
df = pd.DataFrame({'col1': [1,2,3]})
df
x = 10
'x', x
```

#### 文本内容

| 是否常用 | 命令  | 功能
|:-|:-|:-   
| 是 | ``st.markdown(body, unsafe_allow_html=False)`` | 打印makrdown内容
| 是 | ``st.title(body, anchor=None)`` | 打印标题
|  | ``st.header(body, anchor=None)`` | 打印标题
|  | ``st.subheader(body, anchor=None)`` | 打印标题
|  | ``st.caption(body)`` | 
| 是 | ``st.code(body, language="python")`` | 打印脚本
| 是 | ``st.text(body)`` | 打印纯文本
|  | ``st.latex(body)`` | 打印latex输入


### 优化提高

* streamlit速度比较慢，咋处理嘞
    1. st.empty()创建1个空的元素占位，用于后续更新时展示结果
    2. 在触发器上使用@st.cache装饰器来缓存结果，避免重复计算
        - @st.cache：比较早的实现方式了，当前版本已经deprecated了
        - @st.cache_data：在每次函数调用时创建一个新的数据副本；**只有在第一次执行的时候才会读数，其他时间直接从缓存拿数据**
        - @st.cache_resource：是缓存诸如 ML 模型或数据库连接之类的全局资源（不想多次加载的对象）的推荐方法，全局共享哦
    3. 在异步操作中，使用with st.spinner()来显示加载状态
    4. 在异步操作完成后，使用empty_elem.write()来更新结果

```python
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
# 3) spinner
with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')
# 4) 往empty占位位置写入数据
empty.write(df2.head())
st.button("Rerun")
```

<!-- #region -->
## 项目其他内容



### 目录树
- 可以看到，``transformer_nmt_clear.py`` 和 ``transformer_nmt.py`` 两个文件是几乎一致的啊
- 本文注释都按照 ``transformer_nmt.py`` 的来了  

```sh
diff -y --suppress-common-lines --minimal transformer_nmt_clear.py transformer_nmt.py > diff.log
diff -y --left-column  transformer_nmt_clear.py transformer_nmt.py  > diff.log
```


- 项目路径

```
.
├── FAQ.md 【ks】
├── PROJECT.md 【其他相关项目】
├── README.md
├── README_en.md 【ks】
├── UPDATE.md 【ks】
├── api.py
├── cli_demo.py
├── cli_demo_vision.py
├── docs
│   ├── build
│   └── source
├── examples 【示例图片-ks】
├── improve 【提升方法说明-ks】
│   └── README.md
├── limitations 【局限性-ks】
├── ptuning 【模型微调】
│   ├── README.md
│   ├── README_en.md
│   ├── arguments.py
│   ├── deepspeed.json
│   ├── main.py
│   ├── trainer.py
│   ├── trainer_seq2seq.py
│   └── web_demo.py
├── resources 【入群交流-ks】
│   └── WECHAT.md
├── utils.py
├── web_demo.py
├── web_demo2.py
├── web_demo_old.py
└── web_demo_vision.py
```


- 生成项目明细目录
    * `tree -P "*.py|*.md|*.ini|*.conf|*.txt|*.json|*.csv" -I "__pycache__|data/cover" -o tree_project.txt`
    * `tree -P "*.py|*.md|*.ini|*.conf|*.rst|*.json|*.csv" -I "__pycache__|data/cover" -L 2 src/ -o project.txt`


- 模型打包
    * `zip -r ../project_ie.zip ./ -x@exclude.lst`


<details>
<summary> 主要介绍本项目的各个文件及相应功能 </summary>

```sh
./chatglm/
├── FAQ.md 【ks】
├── PROJECT.md 【其他相关项目】
├── README.md
├── README_en.md 【ks】
├── UPDATE.md 【ks】
├── api.py
├── cli_demo.py
├── cli_demo_vision.py
├── docs
│   ├── build
│   └── source
├── examples 【示例图片-ks】
├── improve 【提升方法说明-ks】
│   └── README.md
├── limitations 【局限性-ks】
├── ptuning 【模型微调】
│   ├── README.md
│   ├── README_en.md
│   ├── arguments.py
│   ├── deepspeed.json
│   ├── main.py
│   ├── trainer.py
│   ├── trainer_seq2seq.py
│   └── web_demo.py
├── resources 【入群交流-ks】
│   └── WECHAT.md
├── utils.py
├── web_demo.py
├── web_demo2.py
├── web_demo_old.py
└── web_demo_vision.py
```
</details>
<!-- #endregion -->

<!-- #region -->
### 环境版本说明

- linux系统相关依赖
```sh
Ubuntu: 20.04.1
python: 3.8.10
cuda: '11.4'
docker: 20.10.17
```

- Python环境依赖
    - 具体可参考requirements_py38.txt文件
    
```sh
streamlit==1.27.2
```
<!-- #endregion -->

<!-- #region -->
### 帮助文档

#### 部署环境
- 主要就是docker镜像啦
- 具体参考， ``images_build/`` 文件的readme文档，搭建自己的环境



#### 生成帮助文档

- 生成文档

```sh
cd .. # 切换到doc上一级目录下
sphinx-apidoc -o ./docs/source ./src/ EXCLUDE_PATTERN=docs -f

# 编译
cd docs
make clean & make html
# or 这个结果没有跳转关系直接了
cd docs
sphinx-build -b singlehtml source build

# 查看文档
cd docs
python3 -m http.server 8885 --cgi

# 查看tensorboard结果
tensorboard --port=8885 --logdir=./runs/
```

#### 查看帮助文档

- 1、linux上
```sh
# 切到docs路径下，linux下启用服务
cd docs
python3 -m http.server 8885 --cgi
# 在build→html→index.html下即可查看帮助文档了
```

- 2、window上
```sh
# 下载docs文件到windows本地
# 在build→html→index.html下即可查看帮助文档了
```

- 测试
    - 就是这个啊[test1](ptuning markdown)

:doc:`引用本地的其它rst文档,rst后缀要省略，如about_us <../../ptuning/README.md>`
<!-- #endregion -->


