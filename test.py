import streamlit as st
import os
import threading
import time
from streamlit.runtime.scriptrunner import add_script_run_ctx as ctx
# from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
# import cv2
from chat_bot import gpt_bot
import nibabek as nib
from datetime import datetime
from PIL import image

name = "desargues"
logo = image.open('./assets/logo.png')


class JumpePage_debug_callback:
    def __init__(self, de=True):
        self.de = de
        # 初始化 session_state
        if 'page_state' not in st.session_state:
            st.session_state.page_state = None
        if 'find_state' not in st.session_state:
            st.session_state.find_state = None
    
    def on(self):
        self.de = True
        st.write(f'now is: {self.de}')
    
    def off(self):
        self.de = False
        # st.write(f'now is: {self.de}')

    def yes_call_back(self, session_state):
        if self.de:
            st.write('yes')
        session_state.page_state = 'find_key'
    def no_call_back(self, session_state):
        if self.de:
            st.write('no')
        session_state.page_state = None
    def back_to_previous(self, session_state):
        if self.de:
            st.write('done')
        session_state.page_state = 'main'
    def login_call_back(self, session_state):
        if self.de:
            st.write('login')
            st.write('page_state: ', session_state.page_state)
            st.write('find_state:', session_state.find_state)
        session_state.page_state = 'find_key'
    def suc_call_back(self, session_state):
        assert session_state.page_state == 'find_key'
        if self.de:
            st.write('success')
        session_state.find_state = 'success'

debug = JumpePage_debug_callback(de=False)



def find_key_page(session_state):
    st.write("请输入您在望问医聊公众号中申请登记的手机号和登录密码，以便我们确认您的身份，并重新发送密钥")
    temp_col1, temp_col2 = st.columns([1,2])
    with temp_col1:
        phone = st.text_input("手机号：")
    with temp_col2:
        st.write(' ')
    _temp_col1, _temp_col2 = st.columns([1,2])
    with _temp_col1:
        pwd = st.text_input("密码：", type='password')
    with _temp_col2:
        st.write(' ')

    login = st.button("重置密钥", on_click=debug.login_call_back, args=(st.session_state,))
    if login:
        # 模拟异步处理身份验证
        session_state.find_state = 'processing'
        for i in range(int(1e7)):
            pass
        session_state.find_state = 'success'
        # def verify_identity():
        #     time.sleep(1)
        #     session_state.find_state = 'success'
        #                 # elif st.session_state.page_state == 'failure':
        #     #     st.write("您输入的身份信息有误，请重新输入，或访问我们的公众号")
        
        # # time.sleep(3000)
        # # session_state.find_state = 'success'


        # thread = threading.Thread(target=verify_identity)
        # # ctx(thread)
        # thread.start()

    back = st.button('Back to previous page', on_click=debug.back_to_previous, args=(st.session_state,))
    # set_flag = 0
    if session_state.find_state == 'success':
        st.write("身份核验成功\n新的密钥已经创建，请于手机公众号查收", on_change=debug.suc_call_back, args=(st.session_state,))
    elif session_state.find_state == 'processing':
        st.write("核验中...")
        # set_flag = 1
    else:
        st.write('')
    if back:
        session_state.page_state = 'main'

def main():
    st.markdown('# 望问医聊-v1.0')
    st.image(logo, width=11, caption='望问医聊')
    
    if st.session_state.page_state is None:
        sd_select = st.sidebar.selectbox(
            '您准备使用什么身份访问望问医聊项目?',
            ('个人', '合作医院', '一般医疗企业')
        )

        st.sidebar.write("如果购买过我们的产品，请检查我们发送给您的动态密钥(token)，\
                每个密钥24小时有效\n")
        sd_token = st.sidebar.text_input(
            "请在这里放置你的望问医聊密钥",
            placeholder='粘贴您的token'
        )
        cc1, cc2 = st.sidebar.columns(2)
        # with cc1:
        save_key = cc1.button('保存密钥')
        no_key = cc2.button("密钥丢失？")
        if no_key:
            st.sidebar.write('您输入的信息可能未保存，是否跳转到新的页面？')
            with st.sidebar.row():
                c1 = st.sidebar.button('是', on_click=debug.yes_call_back, args=(st.session_state,))
                c2 = st.sidebar.button('否', on_click=debug.no_call_back, args=(st.session_state,))
            # col1, col2 = st.sidebar.columns(2)
            # with col1:
            #     c1 = st.sidebar.button('是', on_click=debug.yes_call_back, args=(st.session_state,))
            # with col2:
            #     c2 = st.sidebar.button('否', on_click=debug.no_call_back, args=(st.session_state,))
            if c1:
                st.session_state.page_state = 'find_key'
            if c2:
                pass

        if save_key:
            st.write('密钥校验中...')
            for i in range(int(1e8)):
                i=i
            st.write(f'校验通过！{sd_select}用户：{name}，欢迎使用望问医聊！')

    if st.session_state.page_state == 'main':
        main_page()
    if st.session_state.page_state == 'find_key':
        find_key_page(st.session_state)
    

    
def main_page():
    sd_select = st.sidebar.selectbox(
        '您准备使用什么身份访问望问医聊项目?',
        ('个人', '医疗企业/医院', '合作医院')
    )

    st.sidebar.write("如果购买过我们的产品，请检查我们发送给您的动态密钥(token)，\
            每个密钥24小时有效\n")
    sd_token = st.sidebar.text_input(
        "请在这里放置你的望问医聊密钥",
        placeholder='粘贴您的token'
    )
    no_key = st.sidebar.button("密钥丢失？")
    if no_key:
        st.sidebar.write('您输入的信息可能未保存，是否跳转到新的页面？')
        col1, col2 = st.sidebar.columns(2)
        with col1:
            c1 = st.sidebar.button('是', on_click=debug.yes_call_back, args=(st.session_state,))
        with col2:
            c2 = st.sidebar.button('否', on_click=debug.no_call_back, args=(st.session_state,))
            if c1:
                st.session_state.page_state = 'find_key'
    
    


    
if __name__ == '__main__':
    # debug.on()
    debug.off()
    main()