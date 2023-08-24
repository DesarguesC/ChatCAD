import streamlit as st
import os
import threading
import time
from streamlit.runtime.scriptrunner import add_script_run_ctx as ctx
# from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
# import cv2
# from chat_bot import gpt_bot
# import nibabel as nib
from datetime import datetime
from PIL import Image
import random

global name, logo, user, CLASS, RESULT, up
up = True
name = "desargues"
logo = Image.open('./assets/logo.png')
user = Image.open('./assets/user.png')
CLASS = '肺部CT影像'  # '心脏核磁共振表单'
RESULT = "小望观察到正位x线片显示右肺上叶节段性塌陷。尤其需要注意的是小裂和右肺门抬高，纵隔向右轻微移位；同时有粘液栓被识别到，存在低密度影灶，部分充盈缺损\
    这很有可能是一位有哮喘的病人，但也不能排除是肺炎引起的可能。"
st.set_page_config(page_title="💬 望问医聊", layout='wide')


HOW = "哮喘是一种慢性气道疾病，通常表现为气道的炎症和痉挛，导致呼吸困难、喘息和咳嗽。\
        如果这是您自己的胸片CT影像，请记得及时去医院就诊，服用相关药物。治疗哮喘的药物可以分为两大类：控制性药物和急性发作时使用的缓解性药物。\
            以下是一些适合您病症的药物清单：\
        \n①-控制性药物：\n\t1.吸入型类固醇（ICS）： 这是哮喘治疗的主要药物，用于减轻气道炎症和防止哮喘发作。常见的ICS药物包括氟替卡松、布地奈德等。\
            \n\t2.长效β2受体激动剂（LABA）： 通常与ICS联合使用，帮助扩张气道，减轻痉挛。常见的LABA药物包括沙丁胺醇、福莫特罗等。\
            \n\t3.长效抗胆碱能药物（LAMA）： 也可以用于扩张气道，有时与ICS或LABA合用。例如，噻托溴铵是一种常见的LAMA药物。\
            \n\t4.联合制剂： 一些药物将ICS和LABA合并在一个吸入器中，以便于患者使用。例如，沙美特罗/氟替卡松是一种常见的联合制剂。\
        \n②-缓解性药物：\n\t短效β2受体激动剂（SABA）： 这是急性哮喘发作时的常用药物，通过扩张气道，快速缓解症状。常见的SABA药物包括沙丁胺醇、特布他林等。\
        \n请注意，每个人的哮喘情况可能不同，药物的选择和剂量应该由医生根据患者的病情和需要进行个性化的调整。\
        同时，由于哮喘治疗药物为处方药需要由医生开具处方，由专业医生根据具体情况制定合适的治疗方案。另外，与小望聊天并不能待替直接就医\
            ,请不要自行服用药物，以免影响治疗效果和产生药物反映"

response = [
        # 保存望问token后 
    f'您好，个人用户{name}，我是小望，很高兴与您进行对话，我将尽我所能为您提供各种医学问答服务，您可以直接向我提问，也可以上传一些医学影像让我进行分析。',
        # 上传一张医学影像
    '检测到您上传了一张'+CLASS + '，经过初步分析，' + RESULT + '\n您可以针对该影像进行更具体的提问，小望将针对您的问题做出更加细致的回答。',
        # 提问：我确实患有哮喘病，当前哮喘是否有加重的倾向？
    '首先，' + HOW + '。根据当前的信息，小望并不能断定您的哮喘是否有加重的倾向，但是请您依次回答以下问题，以便小望进行分析：\
            \n1.平日里出现呼吸困难、喘息的频率是否有增加？\n2.夜间是否有因为突然咳嗽而苏醒的状况？',
        # 回答： 1.是   2.无
    '您最近咳嗽时是否为干咳没有痰，且伴有嗓子干痒、恶心、干呕？',
        # 回答：干咳，偶尔有恶心的感觉，
    '您是否会感到胸痛，不时伴有晕厥、烦躁不安、心悸、惊恐等感受？',
        # 回答：偶尔胸痛，有烦躁不安
    '您的哮喘症状可能有加重的趋势，同时结合您上传的影像可能是肺栓塞出现的征兆，这是比较严重的，根据数据库数据查询，您患有或将出现肺栓塞症状的概率高于80%.\
        \n当然，小望也有可能有犯错的时候，因此为了您的健康，请您务必尽快到附近的医院就诊，\
        您可以提供您的位置信息，由小望综合医疗资源和门诊挂号余量查询最近的诊疗，推荐较好的就诊选择',
        # 浙江省杭州市钱塘新区，二号大街
    '您好，为您查询到<浙大邵逸夫医院钱塘院区>，已经通过平台预留手机号 15958152006 关联到您在<浙大邵逸夫医院钱塘院区>的就诊信息，\
        查询到截至当前时间 [2023-08-24 | 10:11]，最近的有余量呼吸内科门诊时间为 【8月29日 周二】下午，余量为【3】个：\n【15：57 \
            - 22号】余量1个，【16：04 - 23号】余量1个，【16：18 - 25号】余量1个。\
        \n查询到的医生信息为： \n【 周勇 | 主任医师 】\n您可以选择合适的时段确认，由小望进行一键预约，或者更换其他时段、医师的门诊。',
        # 请预约16：18的门诊 
    '您将预约的门诊信息为：\n<浙大邵逸夫医院钱塘院区> ---【16：18 - 25号】余量1个，坐诊医生【 周勇 | 主任医师】\n请确认以上预约信息',
        # 确认
    '好的，小望已经成功为您预约：<浙大邵逸夫医院钱塘院区> ---【16：18 - 25号】余量1个，坐诊医生【 周勇 | 主任医师】\n稍后您将会收到医院发来的成功预约短信，\
        请及时查收。感谢您使用望问医疗！'
    ]

# video_html = """
# 		<style>

# 		#myVideo {
# 		  position: fixed;
# 		  right: 0;
# 		  bottom: 0;
# 		  min-width: 100%; 
# 		  min-height: 100%;
# 		}

# 		.content {
# 		  position: fixed;
# 		  bottom: 0;
# 		  background: rgba(0, 0, 0, 0.5);
# 		  color: #f1f1f1;
# 		  width: 100%;
# 		  padding: 20px;
# 		}

# 		</style>	
# 		<video controls>
# 	<source type="video/mp4" src="/root/ChatCAD/assets/try.mp4:video/mp4;base64,AAAAHGZ0eXBtcDQyAAAAAG1wNDJpc29....../l/L+X8v5AAAAMgfDg==">
# </video>
#         """

# st.markdown(video_html, unsafe_allow_html=True)


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
        no_key = cc2.button("密钥丢失？")
        
        if no_key:
            st.sidebar.write('您输入的信息可能未保存，是否跳转到新的页面？')
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
                # if st.session_state.page_state == 'chat':
                    # chatbot()
                        

        assert st.session_state.upload_num >= 0
    
    if st.session_state.page_state == 'chat':
        chat_messages = generate_response()
        chatbot(st.session_state.first_chat)

    if st.session_state.page_state == 'main':
        # st.session_state.page_state = None
        # st.empty()
        main_page()
    if st.session_state.page_state == 'find_key':
        find_key_page(st.session_state)
    



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
        if not isinstance(message["content"], str):
            debug.image_show_call_back("first")



    img_file = st.sidebar.file_uploader(label="📁上传图像进行医疗影像、数据咨询", type=['png','jpg'], on_change=debug.uploader_call_back, 
                                        args=(st.session_state,), accept_multiple_files=False, disabled=False)  
    # if img_file := st.sidebar.file_uploader(label="📁上传图像进行医疗影像、数据咨询", type=['png','jpg'], on_change=debug.uploader_call_back, 
                                        # args=(st.session_state,), accept_multiple_files=False, disabled=False) is not None:
    global up

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

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=user):
            st.write(prompt)        
             
    
    if (not st.session_state.first_chat and st.session_state.messages[-1]["role"] != "assistant") or (img_file and st.session_state.first_chat) is not None or st.session_state.first_chat:
        st.session_state.first_chat = False   
        assistant_response = response[st.session_state.m_cnt]
        st.session_state.m_cnt = 0 if st.session_state.m_cnt == len(response)-1 else (st.session_state.m_cnt + 1)
        # st.sidebar.write(assistant_response)
        with st.chat_message(name = "assistant", avatar=logo):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner("数据查询中..."):
                time.sleep(random.randint(5,10) / 10)
            # Simulate stream of response with milliseconds delay

            for chunk in assistant_response:
                full_response += chunk + " "
                time.sleep(random.randint(0,9) / 100)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # st.session_state.messages.append(message)



def generate_response():
    i = 0
    response = [
        # 保存望问token后 
    f'您好，个人用户{name}，我是小望，很高兴与您进行对话，我将尽我所能为您提供各种医学问答服务，您可以直接向我提问，也可以上传一些医学影响让我进行分析',
        # 上传一张医学影像
    f'检测到您上传了一张{CLASS}，经过初步分析，f{RESULT}，您可以针对该影像进行更具体的提问，小望将针对您的问题做出更加细致的回答',
        # 提问：肺部...
    f'①...', 
    f'②...',
    f'③...',
    f'④...'
    ]
    while True:
        yield response[i]
        if i == len(response):
            i = -1
        i += 1

    

    
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
    # chatbot(sd_token, img_file)
    

if __name__ == '__main__':
    # debug.on()
    debug.off()
    main()