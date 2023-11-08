from prompt.choice import *

choices = {
    'ori': ori,
    '对话演示1': yanshi1,
    '对话演示2': yanshi2,
    '对话演示3': yanshi3,
    '日常问询': richang,
    '医生诊中': zhenzhongYi,
    '患者诊中': zhenzhongHuan,
    '随便问的': suibianwen,
    '诊后乱问': zhenhou,
    '排队时候': paidui,
    '排队挂号': guahao,
    '预约提醒': tixing,
    '体检体检': tijian,
    '住院住院': zhuyuan,
    '医生来问': yisheng,
    '该吃药了': chiyao,
    '报告生成': baogao
}

def choice(x: str):
    assert x in choices.keys(), f'x = {x}'
    return choices[x]
    


# response = ...