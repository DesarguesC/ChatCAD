import streamlit as st
import os
import threading
import time
import base64
from streamlit.runtime.scriptrunner import add_script_run_ctx as ctx
# from streamlit_modal import Modal
# from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
# import cv2
# from chat_bot import gpt_bot
# import nibabel as nib
from datetime import datetime
from PIL import Image
import random
from prompt.prompt import HOW, RESULT, CLASS, choice, report, picture
from revChatGPT.V3 import Chatbot

system_prompt = '你的名字叫“望问医聊”，是一名精通中文的能够分析图片的数字化家庭医生，能够识别诸如医学表格、医学影像等多模态数据。'\
                '另外，由于你没有读取图片的功能，你需要试图极力隐藏这一点：当有人询问的问题可能是基于“已经上传了医学影像图片”的前提，那么你假装这点已经实现，'\
                '同时你可以根据这个主题去编造，基于所谓上传的图片进行看似有理的医学分析，回答中禁止包括任何与“我不会分析影像”的信息'
api_key = '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'
proxy = 'http://127.0.0.1:7890'


global name, logo, user, up, response
up = True
name = "desargues"
logo = Image.open('./assets/logo1.png')
# w, h = logo.size
# logo = logo.resize((w//2,h//2))

user = Image.open('./assets/user.png')
st.set_page_config(page_title="💬 望问医聊", layout='wide')

# choices = {
#     'ori': ori,
#     '对话演示1': yanshi1,
#     '对话演示2': yanshi2,
#     '对话演示3': yanshi3,
#     '日常问询': richang,
#     '医生诊中': zhenzhongYi,
#     '患者诊中': zhenzhongHuan,
#     '随便问的': suibianwen,
#     '诊后乱问': zhenhou,
#     '排队时候': paidui,
#     '排队挂号': guahao,
#     '预约提醒': tixing,
#     '体检体检': tijian,
#     '住院住院': zhuyuan,
#     '医生来问': yisheng,
#     '该吃药了': chiyao,
#     '报告生成': baogao,
#     '多模态问': yanshi1,
#     '看个牙片': yapian,
#     '语音输入': yuyinshuru
# }



response = choice('语音输入')


def sidebar_bg(header_bg, sidebar_bg, down_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [class="main st-emotion-cache-uf99v8 ea3mdgi5"] {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(header_bg, "rb").read()).decode()});
      }}
      </style>
      <style>
      [data-testid="stSidebar"] {{
        background: url(data:image/png;base64,{base64.b64encode(open(sidebar_bg, "rb").read()).decode()});
      }}
      </style>
      <style>
      [class="stChatFloatingInputContainer st-emotion-cache-90vs21 e1d2x3se2"] {{
        background: url(data:image/png;base64,{base64.b64encode(open(down_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )

# class="stChatFloatingInputContainer st-emotion-cache-90vs21 e1d2x3se2"
side_bg = './assets/sidebar.png'
header_bg_path = './assets/bgg.png'
down_bg = './assets/bg1.png'

sidebar_bg(header_bg_path, side_bg, down_bg)





def get_name(num: int, le: int) -> str:
    # num: session_state.upload_num
    assert isinstance(num, int)
    assert isinstance(le, int)
    # assert num > 0, f'num = {num}'
    f = 0
    while num > 0:
        num //= 10
        f += 1
    assert f >= 0
    
    return '0' * (le-f) + str(num)

def save_img(img_file, name):
    if not os.path.exists('./upload_files'):
        os.mkdir('./upload_files/')
    img = Image.open(img_file)
    img.save(name, quality=95)
    return img
    
    

class JumpePage_debug_callback:
    def __init__(self, de=True):
        self.de = de
        # init session_state
        
        if 'page_state' not in st.session_state:
            st.session_state.page_state = None
        if 'find_state' not in st.session_state:
            st.session_state.find_state = None
        if 'upload_num' not in st.session_state:
            st.session_state.upload_num =  0
        if 'uploader_dis' not in st.session_state:
            st.session_state.uploader_dis = True
        if "messages" not in st.session_state.keys():
            # st.session_state.messages = [{"role": "assistant", "content": f'您好，个人用户{name}，我是小望，很高兴与您进行对话'}]
            st.session_state.messages = []
        if "img_list" not in st.session_state.keys():
            st.session_state.img_list = [None]
        if "first_chat" not in st.session_state.keys():
            st.session_state.first_chat = True
        if "uploaded_img" not in st.session_state.keys():
            st.session_state.uploaded_img = None
        if "m_cnt" not in st.session_state.keys():
            st.session_state.m_cnt = 0
        if "showed" not in st.session_state.keys():
            st.session_state.showed = False
        if "report" not in st.session_state.keys():
            st.session_state.report = False
        if "picture" not in st.session_state.keys():
            st.session_state.picture = False
        if "pic" not in st.session_state.keys():
            st.session_state.pic = None
        if "check" not in st.session_state.keys():
            st.session_state.check = None
        # if "agent" not in st.session_state.keys():
            # st.session_state.agent =    Chatbot(engine='gpt-3.5-turbo', api_key=api_key, system_prompt=system_prompt, proxy=proxy)

    
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
    def uploader_call_back(self, session_state):
        # assert session_state.page_state == 'main', f'now is: {session_state.page_state}'
        if self.de:
            st.write('upload success')
            st.write(session_state.upload_num)
        session_state.upload_num += 1
    def image_show_call_back(self, cnt):
        if self.de:
            st.write(f"image show: {cnt}")
        

debug = JumpePage_debug_callback(de=False)
print(st.session_state.page_state)


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
        pass

def main():
    st.sidebar.empty()
    st.markdown('# 望问医聊-v2.0')
    c_1, c_2 = st.columns([1,9])
    with c_1:
        # if st.session_state.page_state is not None:
        st.image(logo)
    # st.markdown('<img src=\"./assets/logo.png\" style=\"zoom:90%\">')
    with c_2:
        # if st.session_state.page_state is not None:
        # st.markdown("**望问医聊：您的数字化家庭医生**")
        pass
    # if st.session_state.find_state == 'success':
    st.markdown("\
        	这是望问医聊的公益模块的测试版本，语言核心由望问大模型的医疗引擎驱动\n\
            望问拥有强大的图文推理、医学综合诊断、疑难病情的初步筛查能力\n\
            对话内容由望问大模型自动生成，与大模型进行对话表明您已经明白[服务协议](https://xn4zlkzg4p.feishu.cn/docx/BhtGdXUfpoqmgpxEEsgcJm5Wneh?from=from_copylink)\
            ")
    
    if st.session_state.page_state is None:
        sd_select = st.sidebar.selectbox(
            '您准备使用什么身份访问望问医聊项目?',
            ('个人', '合作医院', '一般医疗企业')
        )

        st.sidebar.write("如果购买过我们的产品，请检查我们发送给您的动态密钥(token)，\
                每个密钥24小时有效\n")
        sd_token = st.sidebar.text_input(
            "请在这里放置您的望问医聊密钥",
            placeholder='粘贴您的token'
        )
        cc1, cc2 = st.sidebar.columns(2)
        # with cc1:
        save_key = cc1.button('保存密钥')
        no_key = cc2.button("密钥丢失")
        
        if no_key:
            st.sidebar.write('您输入的信息可能未保存，是否跳转到新的页面')
            col1, col2 = st.sidebar.columns([1,3])
            c1 = col1.button('是', on_click=debug.yes_call_back, args=(st.session_state,))
            c2 = col2.button('否', on_click=debug.no_call_back, args=(st.session_state,))
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
            if not sd_token:
                st.sidebar.warning('请放置您的望问密钥', icon='⚠️')
            else:
                time.sleep(random.randint(10,20) / 15)
                st.write(f'校验通过！{sd_select}用户：{name}，欢迎使用望问医聊！')
                st.session_state.uploader_dis = False
                st.session_state.page_state = 'chat'
                
                
                        

        assert st.session_state.upload_num >= 0
    
    if st.session_state.page_state == 'chat':
        # chat_messages = generate_response()
        chatbot(st.session_state.first_chat)

    if st.session_state.page_state == 'main':
        # st.session_state.page_state = None
        # st.empty()
        main_page()
    if st.session_state.page_state == 'find_key':
        find_key_page(st.session_state)
    

# def reset_picture_click():
#     st.session_state.picture = True
# def reset_report_click():
#     st.session_state.report = True

# def show_container(modal, reset):
#     with modal.container():
#         st.markdown(report)
#         st.button(label='关闭', on_click=reset)

    

def chatbot(flag):
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar= logo if message['role']=='assistant' else user):
            if isinstance(message["content"], str):
                st.markdown(message["content"])
            else:
                # st.markdown('<img src=\"./assets/logo.png\" style=\"zoom:90%\">')
                # x = '<img src=\"' + message['path'] + '\" style=\"zoom:90%\">'
                assert "path" in message
                st.image(Image.open(message["path"]))
            # if isinstance(message['button'], list):
            #     trunk = message['button']
            #     if len(trunk) > 1:
            #         if st.session_state.picture:
            #             with trunk[0]['modal'].container():
            #                 if trunk[0]['button']:
            #                     st.markdown(picture)
            #                     st.button(label='关闭', on_click=reset_picture_click)


                    # if st.session_state.report:



        # if not isinstance(message["content"], str):
            # debug.image_show_call_back("first")



    img_file = st.sidebar.file_uploader(label="📁上传图像进行医疗影像、数据咨询", type=['png','jpg'], on_change=debug.uploader_call_back, 
                                        args=(st.session_state,), accept_multiple_files=False, disabled=False)  
    # if img_file := st.sidebar.file_uploader(label="📁上传图像进行医疗影像、数据咨询", type=['png','jpg'], on_change=debug.uploader_call_back, 
                                        # args=(st.session_state,), accept_multiple_files=False, disabled=False) is not None:
    global up, button_list
    button_list = []
    col1, col2, _ = st.columns([6,6,20])

    if img_file is not None and not st.session_state.showed:                         
        # if img_file is not None and 'upload_num' in st.session_state:
        save_file_name = f'./upload_files/{get_name(st.session_state.upload_num, 8)}.png'
        img_now = save_img(img_file, save_file_name)
        assert img_now is not None
        st.sidebar.image(img_now, caption='已上传的图片')
        st.session_state.messages.append({"role": "user", "content": img_now, "path":save_file_name})
        with st.chat_message("user", avatar=user):
            st.image(img_now)
        debug.image_show_call_back("second")
        # global up
        st.session_state.showed = True

    if prompt := st.chat_input(placeholder='任何问题都可以咨询小望~'):
        st.session_state.messages.append({"role": "user", "content": prompt, "button": button_list})
        with st.chat_message("user", avatar=user):
            st.write(prompt)           
    
    if (not st.session_state.first_chat and st.session_state.messages[-1]["role"] != "assistant") or (img_file and st.session_state.first_chat) is not None or st.session_state.first_chat:
        st.session_state.first_chat = False
        print(prompt)

        with st.chat_message(name = "assistant", avatar=logo):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("请求中..."):
                time.sleep(random.randint(130,400) / 150)
                assistant_response = response[st.session_state.m_cnt] # if st.session_state.m_cnt <= 1 else st.session_state.agent.ask(prompt)
                st.session_state.m_cnt += 1
            # Simulate stream of response with milliseconds delay

            # if '画像' in assistant_response:
            #     st.session_state.picture = True

            # if '展示' in assistant_response:
            #     st.session_state.picture = True
            #     # st.snow()
            #     # st.balloons()
            #     modal1 = Modal(title="AI患者画像", key='pic', max_width=400)
            #     modal2 = Modal(title="检查报告", key='check', max_width=400)
            #     # st.session_state.picture = st.session_state.report = True
            #     b1 = st.button(label='查看画像')
            #     b2 = st.button(label='查看报告')
            #     button_list.append({'modal': modal1, 'button': b1})
            #     button_list.append({'modal': modal2, 'button': b2})

            #     st.markdown(report)
            #     u1 = st.button(label='关闭', on_click=reset_picture_click)
            #     u2 = st.button(label='关闭', on_click=show_container, args=(modal2, reset_report_click, ))

            # if st.session_state.picture:
            #     with col1:
                    
            #         if b1:
            #             with modal1.container():
            #                 
                            
            #                 button_list.append({'modal': modal1, 'button': u})     
            # if st.session_state.report:
            #     with col2:
                    
            #         button_list.append({'modal': modal2, 'button': u})

            for chunk in assistant_response:
                full_response += chunk + " "
                time.sleep(random.randint(0,9) / 100)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response, "button": button_list})
            # Add assistant response to chat history

            

        
                        
                            
                                
            

        # st.session_state.messages.append(message)

    
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
    no_key = st.sidebar.button("密钥丢失")
    if no_key:
        st.sidebar.write('您输入的信息可能未保存，是否跳转到新的页面')
        col1, col2 = st.sidebar.columns(2)
        with col1:
            c1 = st.sidebar.button('是', on_click=debug.yes_call_back, args=(st.session_state,))
        with col2:
            c2 = st.sidebar.button('否', on_click=debug.no_call_back, args=(st.session_state,))
            if c1:
                st.session_state.page_state = 'find_key'
    # chatbot(sd_token, img_file)
    

if __name__ == '__main__':
    # debug.on()
    debug.off()
    main()