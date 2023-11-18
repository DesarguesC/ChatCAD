CLASS = '肺部CT影像'  # '心脏核磁共振表单'
RESULT = "小望观察到正位x线片显示右肺上叶节段性塌陷。尤其需要注意的是小裂和右肺门抬高，纵隔向右轻微移位；同时有粘液栓被识别到，存在低密度影灶，部分充盈缺损\
    这很有可能是一位有哮喘的病人，但也不能排除是肺炎引起的可能。"

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


ori = [
        # 保存望问token后 
    f'您好，个人用户，我是小望，很高兴与您进行对话，我将尽我所能为您提供各种医学问答服务，您可以直接向我提问，也可以上传一些医学影像让我进行分析。',
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

yanshi1 = [
    f'尊敬的用户您好，我是小望，您的多模态医疗问答助手。'\
        '您可以输入医疗影像或者医疗领域相关问题，我会尽我所能作出回答。'\
        '注意我所给出的建议仅仅具有指导意义，请联系专业医生以获取更专业的答复。',
    
    '检测到您输入了一张脑部冠状面T1加权的MRI扫描影像，'\
    '图中脑部的蝶鞍内可见较强的肿块病变，目前已经延伸至左侧的海绵窦。如果您有关于图片更多的需求，请告知我。',

    # 可以简单分析一下这张图并给我一些就诊建议吗？

    '根据MRI扫描结果，推测您在蝶鞍区域内出现了组织增生或者肿瘤，这可能是由各种垂体腺瘤所导致。'\
    '蝶鞍区肿瘤一般是常见的肿瘤疾病，蝶鞍区肿瘤是一种良性的肿瘤。但是良性的肿瘤也是需要及早采取治疗的，一般手术治疗是唯一方法，在早期治疗效果还是非常不错的。'\
    '建议您一定要放松心情，保持良好心态；给您的就医建议是：尽快前往医院就诊和安排手术，以免耽误病情。', 

    # 可以为我推荐医院吗？

    '好的，小望收到～在杭州市区范围内治疗蝶鞍区肿瘤较好的医院依次为：浙江大学医学院附属第二医院（神经外科）、浙江大学医学院附属第一医院（神经外科）、浙江省肿瘤医院等等。'


]

yanshi2 = [
    '尊敬的用户您好，我是小望，您的多模态医疗问答助手。'\
    '您可以输入医疗影像或者医疗领域相关问题，我会尽我所能作出回答。注意我所给出的建议仅仅具有指导意义，请联系专业医生以获取更专业的答复。',
    
    # 特异性皮炎是什么，有哪些应对手段？

    '特异性皮炎是一种慢性皮肤病，通常又称作湿疹，往往由人体因接触特定过敏原物质而导致皮肤产生过敏性炎症反应，常见症状包括皮肤瘙痒及红肿等。'\
    '疾病多在婴幼儿期初发，并容易在患者一生各个年龄段反复出现。疾病发病人群非常广泛，且目前没有非常有效的根治手段，非常影响患者的生活质量。\n'\
    '特异性皮炎的应对手段需要根据病情和患者情况进行具体选择，其主要手段包含：\n'\
    '1、保持良好的生活习惯。患者可以通过医学鉴定等多种方式确认自身的过敏原，在日常生活中尽可能避免这些过敏原，从而避免疾病的产生。\n'\
    '2、外敷药物以解决局部症状。患者日常可以使用保湿剂以保持皮肤湿润，从而减轻瘙痒等症状，如果局部红肿严重，可以选用类固醇霜剂、'\
        '抗炎药膏来缓解症状。\n'\
    '3、当前最新的研究成果显示，对于具有易产生严重过敏反应的人群，可以采用脱敏治疗法以减轻过敏症状，'\
        '采用的手段为将过敏原制成不同浓度的制剂，让患者渐进性暴露于过敏原下从而提升患者对过敏原的耐受性。\n'\
    '4、对于病情急性发作的中重度特异性皮炎患者，可以采用阿布昔替尼等抑制剂药物进行临床治疗，具体请遵循医生指导。',

    # 阿布昔替尼的价格多少，可以在哪里买到？

    '阿布昔替尼片（希必可）原价3150元/盒（14片），目前已降价为1177元/盒（14片）。'\
    '本院附属药品店可购买该药品。但是阿布昔替尼为处方药，使用前请先咨询医生，您可以联系本院皮肤科门诊专家做进一步咨询。'

]

yanshi3 = [
    '尊敬的用户您好，我是骨科小望，您的多模态医疗问答助手。'\
    '您可以输入医疗影像或者医疗领域相关问题，我会尽我所能作出回答。注意我所给出的建议仅仅具有指导意义，请联系专业医生以获取更专业的答复。',

    # 刚刚体育课上脚踝扭伤了，怎么处理？

    '脚踝扭伤是最为常见的运动损伤，需要根据具体的病情采取不同的应对措施，在扭伤后您应当及时考虑以下步骤：\n'\
    '1、立即停止运动，从而减少伤处出血，避免淤青加重，同时应当采用支撑物固定脚踝位置，避免关节发生移动。'\
        '注意切忌强行支撑进行活动，这可能导致伤情加重，不利于后续治疗。\n'\
    '2、抬高脚踝，这有利于促进血液循环，避免伤口处产生水肿现象。\n'\
    '3、使用冰袋或者包裹冰块的毛巾轻轻覆盖在伤处以上，通常一次性持续10-20分钟，每2小时一次，切忌长时间冰敷，这可能导致组织冻伤。\n'\
    '4、在肿痛减轻后，可以使用弹性绷带进行加压包扎，注意不要过度加压，这容易导致受伤肢体出现缺血症状。\n\n'\
    '请注意，以上步骤仅仅适用于轻度扭伤，您可以用以下方法对扭伤程度作出初步判断：\n'\
    '1、如果伤口出现淤青症状并伴随较强或剧烈肿痛，可能是韧带严重或完全撕裂，请及时寻求医生获取帮助。\n'\
    '2、如果伴随有脚踝畸形或者脚踝产生麻木或刺痛，可能发生骨折，需要及时寻求医生获取帮助。\n'\
    '特别注意，以上诊断措施仅用于初步进行判断，建议您向专业医生咨询以进行具体评估。'



]

richang = [
    '尊敬的用户您好，我是骨科小望，您的多模态医疗问答助手。'\
    '您可以输入医疗影像或者医疗领域相关问题，我会尽我所能作出回答。注意我所给出的建议仅仅具有指导意义，请联系专业医生以获取更专业的答复。',

    # 刚刚体育课上脚踝扭伤了，怎么处理？

    '脚踝扭伤是最为常见的运动损伤，需要根据具体的病情采取不同的应对措施，在扭伤后您应当及时考虑以下步骤：\n'\
    '1、立即停止运动，从而减少伤处出血，避免淤青加重，同时应当采用支撑物固定脚踝位置，避免关节发生移动。'\
        '注意切忌强行支撑进行活动，这可能导致伤情加重，不利于后续治疗。\n'\
    '2、抬高脚踝，这有利于促进血液循环，避免伤口处产生水肿现象。\n'\
    '3、使用冰袋或者包裹冰块的毛巾轻轻覆盖在伤处以上，通常一次性持续10-20分钟，每2小时一次，切忌长时间冰敷，这可能导致组织冻伤。\n'\
    '4、在肿痛减轻后，可以使用弹性绷带进行加压包扎，注意不要过度加压，这容易导致受伤肢体出现缺血症状。\n\n'\
    '请注意，以上步骤仅仅适用于轻度扭伤，您可以用以下方法对扭伤程度作出初步判断：\n'\
    '1、如果伤口出现淤青症状并伴随较强或剧烈肿痛，可能是韧带严重或完全撕裂，请及时寻求医生获取帮助。\n'\
    '2、如果伴随有脚踝畸形或者脚踝产生麻木或刺痛，可能发生骨折，需要及时寻求医生获取帮助。\n'\
    '特别注意，以上诊断措施仅用于初步进行判断，建议您向专业医生咨询以进行具体评估。'
  
]

zhenzhongYi = [
    '王医生您好！89号患者李建国在平台进行了诊前咨询，先将其画像发送给您，请注意查收。\n\n'\
    '\t姓名：李建国\n'\
    '\t年龄：56岁\n'\
    '\t性别：男性\n'\
    '\t联系信息：手机号：13567712186，地址：杭州市钱塘区白杨街道2号大街1189号\n\n'\
    '既往病史：\n\n'\
    '\t高血压：李建国自20年前被诊断患有高血压，曾经在过去十年里一直接受抗高血压药物治疗。'\
        '最近的血压测量结果显示，他的收缩压（舒张压）在140-150 mmHg范围内，尤其在早晨时分。他还经历过高血压引起的头痛和轻度眩晕。\n'\
    '\t糖尿病：他在5年前被诊断患有2型糖尿病，目前通过口服药物来管理血糖。他定期监测血糖水平，但最近的检查记录(创建于2023年10月24日15:43:23)显示，'\
        '他的空腹血糖水平已经达到了150 mg/dL左右，比正常水平高。\n'
    '\t高胆固醇：李建国也有高胆固醇的问题，接受药物治疗以降低胆固醇水平。最近的检测结果显示，他的LDL胆固醇水平处于正常范围。\n\n'
    '用药情况：\n\n'\
    '\t抗高血压药物：他目前每天服用贝他受体拮抗剂（Beta-blocker）和ACE抑制剂（ACE Inhibitor）来管理高血压。他坚持按医嘱服药。'\
    '\t2型糖尿病药物：他每天服用二甲双胍（Metformin）来帮助控制血糖。他在饮食方面也有所控制，但仍然偶尔放纵。\n'\
    '\t降胆固醇药物：他服用他汀（Statins）来降低胆固醇水平，同时在医生的建议下也采取一定的饮食改变。\n\n'\
    '本次症状表述：\n'\
    '\t李建国报告最近几个星期感到疲劳，尤其是早晨起床后。他也注意到在上午时分出现头晕的情况，有时伴随耳鸣。'\
        '此外，他有时会感到心跳急促，尤其在进行体力活动时。他描述这些症状似乎与他的高血压有关，尽管他在服用药物，'\
            '但他担心可能需要重新评估治疗计划，以确保疾病控制得当。他还表达了担忧自己的糖尿病管理可能不够有效。\n',

    # 展示上次检测的具体数值

    '\t姓名：李建国\n'\
    '\t年龄：56岁\n'\
    '\t性别：男性\n'\
    '\t查询日期：2023年11月06日\n\n'\
    '\t检测项目及结果：\n'\
    '\t血糖检测：\n'\
    '\t空腹血糖：145 mg/dL\n'\
    '\tHbA1c：6.9%\n'\
    '\t分析：李小明的空腹血糖水平高于正常范围，HbA1c水平也高于目标（通常小于6.5%）。这表明糖尿病控制不佳。'
    '\t建议：增加药物治疗或调整药物剂量，加强血糖监测，改善饮食和增加体育活动。\n\n'\
    '\t血脂检测：\n'\
    '\t总胆固醇：180 mg/dL\n'\
    '\tLDL胆固醇：130 mg/dL\n'\
    '\tHDL胆固醇：40 mg/dL\n'\
    '\t甘油三酯：150 mg/dL\n'\
    '\t分析：总胆固醇和LDL胆固醇水平在正常范围内。HDL胆固醇水平正常，但甘油三酯水平稍高。\n'\
    '\t建议：继续监测，遵循健康饮食，控制甘油三酯水平，考虑适量的锻炼。\n\n'\
    '\t肝功能检测：\n'\
    '\t谷丙转氨酶（ALT）：42 U/L\n'\
    '\t谷草转氨酶（AST）：38 U/L\n'\
    '\t总胆红素：0.8 mg/dL\n'\
    '\t分析：肝功能测试结果显示轻度升高，可能与高胆固醇药物有关。\n'\
    '\t建议：继续监测肝功能，与患者讨论可能的药物调整。\n\n'\
    '\t肾功能检测：\n'\
    '\t肌酐：1.2 mg/dL\n'\
    '\t尿素氮：20 mg/dL\n'\
    '\t分析：肾功能测试结果正常。\n'\
    '\t建议：继续监测肾功能，鼓励保持良好的水分摄入。\n\n'\
    '综合分析和建议：\n'\
    '\t抽血结果表明，李建国的糖尿病控制不佳，高血压和高胆固醇的管理也需要进一步关注。'\
        '建议与患者一起讨论治疗方案，可能需要增加药物治疗，改进饮食和体育活动，以帮助控制疾病。'\
            '定期的随访和监测对于维持患者的健康状况至关重要。'

]

zhenzhongHuan = [
    '您好我是小望，我将全程陪伴您完成此次检查，有任何疑问都可以问我~',
    # 你好，我需要去抽血室，不知道它在医院的哪个位置？
    '您好！抽血室在医院的主大厅右侧，距离大厅入口不远。您会看到标志指引你前往那里。',
    # 明白了，谢谢。还有一个问题，抽完血之后，检验报告在哪里可以拿到？
    '抽完血后，您可以前往医院的检验报告领取窗口，通常也在医院的大厅内。他们会为您提供相应的报告。',
    # 好的，我拿到报告之后，需要交给谁？
    '一般来说，您可以保留一份报告供自己查看，然后根据需要与您的主治医生分享。如果医生要求将报告送到他们那里，'\
        '医院通常会有渠道来完成这一过程，您可以向领取窗口的工作人员咨询具体的交付方式。',
    # 明白了，谢谢你的帮助！
    '不客气，祝您一切顺利，如果还有其他问题，随时可以问我。祝您早日康复！'
]

suibianwen = [
    '您好，我是小望，很高兴与您进行对话，我将尽我所能为您提供各种医学问答服务。您可以直接向我提问，也可以上传一些医学影像让我进行分析。',
    # 我突然肚子很痛
    '请问在肚脐眼上面还是下面呢？',
    # 上面
    '请问您最近有恶心、呕吐、 发热、腹泻等症状吗？',
    # 今天早上开始一直拉肚子
    '请问您这两天有吃油炸、辛辣、不卫生的事物吗？',
    # 昨天晚上吃了烧烤
    '根据您的症状描述与近期饮食习惯，判断您的疾病为急性肠胃炎的概率为87.6%，阑尾炎的概率为10.2%。\n\n'\
    '急性胃肠炎：\n'\
    '\t由细菌、病毒、寄生虫等多种致病原导致的胃、小肠、大肠消化道内膜的急性炎症，'\
        '以呕吐、腹泻、腹痛、恶心等为主要症状[1]。如因进食过敏、刺激性食物、药物引起，'\
            '则为非感染性胃肠炎，症状与感染性胃肠炎相仿。\n'\
    '诊断：\n'
    '\t一般情况下检查粪便常规、血常规、C 反应蛋白、降钙素原等指标\n'\
    '\t如果是细菌感染，则表现为白细胞计数、中性粒细胞计数、C 反应蛋白、降钙素原部分或全部升高[1]。\n'\
    '\t如果病毒感染的话一般血常规白细胞不升高、大便常规也没有白细胞。\n'\
    '\t如果症状比较重，应完善电解质、血气分析等检查，了解有无水、电解质及酸碱平衡紊乱。\n'\
    '治疗：\n'\
    '\t流质饮食，必要时暂禁食，以有利于胃肠道的功能恢复；\n'\
    '\t补液，能口服补液尽量口服补液。对脱水明显者，应及时采用静脉输液治疗。\n'\
    '\t对症治疗，比如患者呕吐时使用胃复安等止吐药，腹痛时可用匹维溴铵等解痉药，帮助缓解症状，如有细菌感染，'\
        '给予抗生素治疗[1]， 常用药物如阿奇霉素、左氧氟沙星等，患者使用后可能出现恶心、呕吐、药疹等不良反应；\n'\
    '生活：\n'\
    '\t早期应进流食，清淡饮食，如米粥、藕粉、果汁等流质饮食，以免肠道产气，'\
        '引起腹胀。避免刺激性食物（如油腻、辛辣食品），以免对胃肠道产生刺激。少吃多餐，'\
            '待症状消失可正常饮食。\n\n'\
    '参考文献：\n'\
        '[1] 周国营，杨兴华，郑德生，等．急性胃肠炎调查国内外研究进展[J]．医学动物防制，2018，34(10): 947-950．',

    # 帮我查询该医院最早的挂号信息，普通门诊
    '已为您查询到浙江大学医学院附属邵逸夫医院（钱塘园区）最近一个半小时内的消化科挂号信息：\n\n'\
    '\t2023年11月6日 13:00~13:30 剩2号\n'\
    '\t2023年11月6日 13:30~14:00 剩5号\n'\
    '\t2023年11月6日 14:00~14:30 剩5号\n\n',

    # 帮我挂最早的号
    '已为您预约浙江大学医学院附属邵逸夫医院（钱塘园区）消化科2023年11月6日 13:00~13:30，'\
        '详细信息稍后发送至您的手机，请您注意查收，祝您早日康复，有任何问题可以继续咨询。'

]

zhenhou = [
    '今天是2023年11月04日，距离您最近一次关于\"脚踝疼痛\"的线下问诊已经过去3天，现在由小望对您发起诊后回访。\n以下是您上次的症状：\n'\
    '\t走路时脚踝不疼、脚内旋外旋会疼痛、踝部发力会疼、按压不疼，突出的骨头用力可以动但发出骨头摩擦的声音\n'\
    '就医及用药情况：\n'\
    '\t酮洛芬凝胶+药店给的膏药，建议配合外用止痛药物扶他林软膏或泽普思贴膏一起使用。\n不知道您用药后脚踝的疼痛症状是否有改善？',

    # 比前几天稍微不疼一点，休息就好了，但打羽毛球运动后又开始疼（一运动就会严重一点）感觉不太严重、但是怕留下后遗症。
    
    '从您描述的情况。主要是踝关节用力的时候会疼痛。踝关节外侧的骨头按压会活动，还可以感觉到摩擦感。'\
    '对于您踝关节外侧的骨头这个突出的部位，是叫做外踝，也是腓骨远端的一个骨性突起，'\
    '正常人都会有这样一个骨性突起，首先建议您对比一下另外一侧没有疼痛的，这两边的骨性突起是否一样？'\
    '按压的时候是否也有摩擦感？如果两侧对比一样，那这里的骨头不一定有太大的问题。因为如果有骨折的话，'\
    '那么会有明显的肿胀，淤血和疼痛的情况。从明目前提供的照片和症状看不太像有骨头的问题。'\
    '但是因为您现在有踝关节的疼痛，而且也有打羽毛球，那么也不能排除会有韧带的问题。'\
    '建议您目前暂时避免踝关节剧烈的运动，行走时可以带一个护踝保护，另外可以进行适当的热敷，'\
    '看这个踝关节的疼痛症状能否缓解，如果没办法缓解或者持续加重的话，那么建议你还是到医院进一步检查治疗，'\
    '一般情况下如果要检查是否有韧带的问题的话，需要做一个踝关节的磁共振才能够判断。',

    # 那我还须怎么用药？
    
    '这边建议您使用泽普思贴膏，用法是每天两次，每次一片。'\
    '第一次可以起床的时候贴，到晚上洗完澡之后再换另外一贴。'
]

paidui = [
    '您好，我是您的智能助手小望，有任何关于医疗、医院的问题都可以咨询我~',
    # 您好，我想咨询一下今天下午内科的就诊情况，有可能知道现在排队的人数吗？
    '您好，让我来为您查询一下。稍等片刻\n\n'\
    '根据最新数据显示，当前内科的就诊队列中大约有15人在等待就诊。n\n'\
    '同时，医院也提供了预约挂号服务，您可以提前预约时间来避免长时间等待。',
    # 哦，好的，谢谢。那骨科呢？我想了解一下骨科的情况。
    '目前骨科就诊队列中有约12人在等待。'\
        '如果您有其他问题或需要更多信息，随时都可以问我。',
    # 好的，谢谢你的帮助！
    '不用谢，祝您就诊顺利。如有其他需要，欢迎随时向我咨询。'
]

shenye = [
    '您好，我是小望，现在是2023年11月05日深夜02：31分，我将尽我所能为您提供医学问答服务。',
    # 我现在突然肚子很痛
    '请问在肚脐眼上面还是下面呢？',
    # 上面
    '请问您最近有恶心、呕吐、 发热、腹泻等症状吗？',
    # 昨天晚上开始有几次拉肚子
    '请问您这两天有吃油炸、辛辣、不卫生的事物吗？',
    # 我昨天晚上吃了烧烤
    '如果你感到肚子痛，可能是由昨晚食用烧烤引起的消化不适。小望人为您可以采取以下一些简单的措施来缓解不适：\n\n'\
    '\t\t保持水分摄入：\n'\
    '\t休息可以帮助消化系统放松，同时保持足够的水分摄入有助于消化。\n'\
    '\t\t饮食调整：\n'\
    '\t避免食用油腻、辛辣、刺激性食物，选择清淡易消化的食物，如米粥、面包和蔬菜。\n\n'\
    '\t\t温和运动\n'\
    '\t适量的散步或轻度运动可以促进肠胃蠕动，有助于消化。\n'\
    '\t\t服用抗酸药物： \n'\
    '\t如果疼痛与胃酸分泌过多有关，可以考虑服用一些非处方的抗酸药物来缓解不适。\n\n',

    # 现在医院的急诊有排班吗，我觉得我还是得去一趟医院
    '已经帮您查询到距离您最近的浙江大学医学院附属邵逸夫医院（钱塘园区），当前住院部急诊科室有两名拥有肠胃炎就诊经验的医生\n'\
    # 好的谢谢，我现在就过去
    '不客气，如果路上遇到任何不适都可以咨询我~'
]

guahao = [
    '您好，我是您的智能助手小望，有任何关于医疗、医院的问题都可以咨询我~',
    # 你好，我已经在医院了，想知道前面还有多少人在排队挂号。
    '你好，当然可以帮你查看排队情况。请稍等片刻...\n'\
    '当前情况是这样的，前面还有3位患者在排队等候挂号，你会是第4位。'\
        '估计等待时间不会太长，但请耐心等待。如果有需要，'\
            '还请提前准备好挂号所需的证件和信息，以加快挂号流程。'\
                '如果有其他问题或需要，随时向我咨询。希望你早日康复！',
]

tixing = [
    '您好，我是小望~距离您预定的\n\n'\
        '浙江大学医学院附属邵逸夫医院（钱塘园区）\n'\
        'X光拍片时间（2023/11/8 13:30~14:00）\n\n'\
        '已不足30分钟，小望建议您提前做好准备并按时前往医院进行检查。'\
        '为了顺利完成检查，请携带好您的身份证明和医保卡。如果您有任何疑问或需要帮助，'\
        '请随时联系我们。祝您健康！',
    # 请问拍X光片有什么注意事项吗？
    '当您准备去医院拍X光片时，这里有一些特定的注意事项：\n\n'\
    '\t\t1、金属物品：在进行X光检查之前，需要脱掉所有可能干扰影像的金属物品，'\
    '如首饰、眼镜、皮带和可取下的牙齿。\n'\
    '\t\t2、饮食：大多数X光检查不要求空腹，但如果是腹部X光，'\
    '医生可能会要求您在检查前几小时内不要进食。\n'\
    '\t\t3、怀孕：如果您怀孕或怀疑自己怀孕，一定要告知医生，'\
    '因为X光辐射可能对胎儿有害。\n'\
    '\t\t4、过敏史：虽然拍摄X光片通常不涉及注射对比剂，但如果有涉及，'\
    '请告知任何已知的过敏反应。\n\n',
    
]

tijian = [
    '您好，我是您的智能助手小望，有任何关于医疗、医院的问题都可以咨询我~',
    # 请问你们医院有哪些体检项目？
    '我们的医院提供一系列全面的体检项目，以满足不同的健康需求：\n\n'
    '\t\t1、基础体检套餐：包括血常规、尿常规、肝功能、肾功能、血脂四项和胸部X光。'\
    '这个套餐适用于定期健康检查，费用为500元。目前空闲时间为每周一至周五的上午9点至下午3点。\n'\
    '\t2、高级体检套餐：除了基础套餐的所有项目外，还包括心电图、腹部超声和甲状腺功能检测。'\
    '这个套餐适合想要进行更为全面检查的患者，费用为1000元。可预约时间为每周二和周四全天。\n'\
    '\t3、女性专属体检套餐：包括高级体检套餐的所有项目，并增加了乳腺超声和妇科检查（包括宫颈涂片）。'\
    '这个套餐专为女性设计，费用为1200元。空闲时间为每周三和周五的上午10点至下午4点。\n'\
    '\t4、老年人体检套餐：针对老年人的需求，增加了骨密度测定、听力检查和视力检查。费用为800元。\n'\
    '体检时间为每周六的上午8点至下午2点。\n\n'\
    '请注意，所有的体检套餐都需要提前预约，我们还提供个性化体检服务，可以根据个人需求添加或更换检查项目。'\
    '更多信息请访问我们的官方网站或直接到医院咨询台了解。',
    # 请问基础体检套餐去之前有哪些注意事项？
    '在进行基础体检套餐之前，请注意以下几点：\n\n'\
    '\t\t1、空腹：体检前8至10小时不要进食任何食物，以确保血液检测的准确性。可以喝少量清水。\n'\
    '\t2、睡眠：确保前一晚有充足的睡眠，避免熬夜，因为疲劳会影响某些检测指标。\n'\
    '\t3、避免剧烈运动：体检前一天应避免剧烈运动和饮酒，这些活动可能会影响检测结果。\n'\
    '\t4、携带身份证明：请携带有效的身份证件，以便在登记时使用。\n'\
    '\t5、慢性病药物：如果您有长期使用的药物，请在体检前咨询医生是否需要停药，或者体检当天携带药物。\n'
    '\t6、女性注意事项：女性患者在月经期间应避免进行尿液和妇科检查，最好在月经结束后的一周内进行体检。\n'\
    '\t7、避免使用化妆品：体检当天，请尽量不要化妆或使用护肤品，尤其是在脸部和颈部，以免影响某些检查项目。\n\n'
]

zhuyuan = [
    '您好，我是您的智能助手小望，有任何关于医疗、医院的问题都可以咨询我~',
    # 你好，我听说绍兴市立医院非常好，我想了解一下关于住院检查、床位和费用的情况。
    '你好，欢迎来到绍兴市立医院。我很高兴为您提供这些信息。首先，可以告诉我您需要住院治疗的具体情况吗？',
    # 我最近一直感到不舒服，需要进一步的检查和治疗。我希望了解一下住院的流程。
    '明白了。通常情况下，您需要先咨询我们的专科医生，他们会评估您的病情，'\
    '并根据需要建议是否需要住院。如果需要住院，我们将为您安排床位。',
    # 好的，那关于床位，我想了解一下床位的类型和可用性。
    '我们医院提供不同类型的床位，包括普通病房、私人病房以及特别护理病房。目前，我们医院目前还有200个床位，'\
    '其中包括20个私人病房和10个特别护理病房。床位的可用性会根据患者数量和医院的工作负荷而变化。'\
    '您可以随时联系我们的床位服务部门，他们会提供最新的床位可用性信息。',
    # 了解了，最后一项是费用。我担心住院治疗会很昂贵。
    '费用会根据您的病情、所选床位类型和治疗方案而有所不同。一般来说，'\
        '普通病房的费用较低，私人病房和特别护理病房的费用会略高一些。'\
            '我们的财务部门可以为您提供明细的费用清单，以便您了解相关费用。'\
                '此外，您还可以咨询是否有医疗保险可以覆盖一部分费用。'\
                    '我们鼓励您在入院前与我们的财务部门或保险代理人联系，'\
                        '以获取关于费用和支付选项的详细信息。',
    # 非常感谢您的解答，我会尽快咨询医生并与床位服务部门、财务部门联系以获取更多信息。
    '不客气，如果您有任何其他问题或需要进一步帮助，都请随时联系我们。祝您早日康复！'\
        '如果您需要了解床位情况，也可以致电我们的床位服务部门，他们会随时提供最新的信息。'

]

yisheng = [
    '您好，我是您的智能医疗助理小望，是您的智能副驾，欢迎咨询我~如果遇到我的判断和您不相符'\
        '的情况，建议您相信您的判断',
    # 我的病人经常干咳，常常觉得头痛，请问你觉得这可能是哪种疾病？
    '患者如果存在持续性咳嗽和头痛，这有可能是普通感冒、流感、过敏反应、'\
        '气管炎或其他呼吸道感染，当然也有可能是其他更严重的健康问题的症状，'\
            '例如支气管炎、哮喘、甚至是 COVID-19 等，建议您可以进一步为患者测量体温，'\
            '并且咨询患者是否有其它明显症状。',
    # 患者近期普遍有低烧的症状
    '如果患者的咳嗽伴随着低烧，这可能是身体对感染的典型反应。低烧通常指体温略高于正常范围，'\
    '即高于摄氏37度或华氏98.6度，但不到高烧的程度，而感染包括呼吸道感染、'\
        '流感、尿路感染、支气管炎等。此外您所述的这种症状也可能由风湿性关节炎、炎症性'\
        '肠病等慢性疾病的恶化所引起，您可以根据患者的既往病史进行X光、CT扫描等影像学检查，也可以通过血液和'\
        '尿液检查等来对患者的症状进行综合判断。'
]

chiyao = [
    '您好，我是小望，医生为您开具的处方药“阿布昔替尼”已到预定服用时间（每日19：00-20：00），'\
        '请尽快口服100mg（一片）“阿布昔替尼”，祝您身体健康!',
    # 这个药品有什么作用
    '该药品适用于对其他治疗手段应答不佳或不适宜的难治性、中重度特应性皮炎成人患者，'\
    '可有效应对此类皮肤性疾病的急性发作，有效缓解瘙痒和红肿症状。',
    # 我需要服用该药品什么时候
    '该药品的使用主要按照医嘱进行，治疗周期一般为2周，若医生无特殊说明，'\
    '您可以根据您的康复程度进行服用，当瘙痒和红肿症状消失即可停止。如果服用时间超过医'\
        '嘱或大于2周后仍无明显改善，请您重新咨询医生并尝试换用其它治疗手段。'

]

baogao = [
    '根据MRI扫描结果，推测您在蝶鞍区域内出现了组织增生或者肿瘤，这可能是由各种垂体腺瘤所导致。根据您的描述，'\
    '手部明显胖肿可能是肢端肥大症（Acromegaly）的典型症状，病因很可能为生长激素分泌过多。结合图像特征和您的描述，'\
    '您很可能患有生长激素腺瘤，需要结合进一步的医学检查来确认，如测算血清生长激素水平等。'\
    '生长激素腺瘤的治疗需要同时结合药物治疗和外科手术治疗，例如使用奥曲肽等生长抑素类似物、多巴胺受体激动剂等，'\
    '对于较大的肿瘤则需要进行过手术切除。如果效果仍然不佳，可能需要进行放射手术治疗。注意以上意见仅供参考，'\
    '具体的诊断和治疗请咨询相关医生。'
]


yapian = [
    '尊敬的用户您好，我是小望，您的多模态医疗问答助手。'\
    '您可以输入医疗影像或者医疗领域相关问题，我会尽我所能作出回答。注意我所给出的建议仅仅具有指导意义，请联系专业医生以获取更专业的答复。',

    # (传图片)

    '监测到您上传了一张牙齿部位的X光影像，小望已经在后台分析，您可以继续像我咨询～',

    # 你好，我最近感到牙床有些不适，可能是智齿的问题。我上传了一张牙片，能帮我分析一下吗？

    '当然可以～根据小望的初步分析，牙片显示了智齿区域。目前，小望注意到一些牙龈肿胀和周围软组织的炎症迹象。这可能是因为智齿正在冲破牙龈，导致您出现了局部不适。',

    # 那应该怎么处理呢

    '首先，小望建议您要保持口腔卫生，同时每天刷牙并可以考虑使用牙线。同时，用温盐水漱口液可以达到缓解炎症的目的。另外，如果症状继续，小望建议您尽快就医，'\
    '以便医生进行更详细的检查。在一些情况下，可能需要考虑智齿的拔除，但具体的治疗方案需要医生根据实际情况评估后决定。',

    # 什么情况下需要考虑拔除智齿呢
    '拔除智齿是一种常见的口腔手术，通常在以下情况下考虑：\n\n'\
    '\t\t智齿不正常生长： 智齿可能不正常生长，例如横生、歪斜、倾斜或嵌入在颌骨中。这种情况可能导致牙齿对其他牙齿的挤压，影响咬合和口腔卫生。\n'\
    '\t\t难忍疼痛与不适： 智齿的不正常生长可能引起牙床肿胀、疼痛、压力感或牙龈感染。这些症状可能需要拔除智齿来缓解病症。\n'\
    '\t\t反复发作的口腔感染： 智齿周围容易滞留食物残渣，易引起感染。如果出现反复的口腔感染，可能需要考虑拔除智齿。\n'\
    '\t\t囊肿或肿瘤形成： 智齿周围可能形成囊肿或肿瘤，尤其是当智齿没有完全长出口腔表面时。拔除智齿可能是治疗这些情况的一种方法。\n'\
    '\t\t对其他牙齿产生压力： 智齿的不正常生长可能对邻近的牙齿产生压力，导致牙齿移位、咬合问题和其他口腔健康问题。\n'\
    '\t\t智齿发生龋齿或牙周病： 由于智齿处于口腔最后位置，牙刷和牙线难以达到，易发生龋齿或牙周病。在这些情况下，拔除智齿可以改善口腔卫生。\n\n'\
    '决定是否拔除智齿通常需要口腔医生或牙科医生的评估。医生会考虑智齿的位置、生长状况、患者的症状以及口腔健康情况来制定最适合的治疗计划。',

    # 谢谢你的建议。还有其他我需要注意的事项吗？
    '当然。如果症状加剧、伴随发热、或者出现吞咽困难等严重症状，建议尽快就医。此外，避免食用过硬或容易引起刺激的食物，以免加重症状。'

]



baogaoDIA = [
    '王医生您好！89号患者李建国在平台进行了诊前咨询，他将于20分钟内抵达医院。',
    # 总结生成一下患者画像
    '小望收到，您可以点击查看画像'
    # 再展示一下他最近一次的检查报告
    '小望收到，您可以点击查看检查数据'
]

picture1 = """"
    ## AI患者画像

    **主诉**：咨询高血压、糖尿病和高胆固醇治疗
    **现病史**：患者患有高血压20年，服用抗高血压药物治疗，血压控制不佳，近期出现疲劳、头晕、耳鸣、
        心悸等不适；5年前诊断为2型糖尿病，口服二甲双胍治疗，血糖控制不佳；
            同时合并高胆固醇，服用他汀治疗。患者担心疾病控制不佳，就诊咨询。

            **既往史**：高血压、2型糖尿病、高胆固醇。

            **个人史**：吸烟史20年，已戒烟10年；饮酒史20年，平均每周饮酒3次。
            
            **家族史**：父亲患有高血压。

            **过敏史**：无特殊记录。
            
            **月经婚育史**：无特殊记录。

            ### 过去的处理建议
            
            增加药物治疗或调整药物剂量，加强血糖监测，改善饮食和增加体育活动。
                继续监测肝功能，与患者讨论可能的药物调整。继续监测肾功能，鼓励保持良好的水分摄入。
                    定期随访和监测对于维持患者的健康状况至关重要。
    """

report1 = """
    # 检查报告

    检查时间: 2023年11月04日14：39

    ## 血压 
    
    收缩压（舒张压）：140-150 mmHg

    ## 空腹血糖 
    
    150 mg/dL，且LDL胆固醇水平正常

    ## 其他数据

    ```bash
    总胆固醇：180 mg/dL
    LDL胆固醇：130 mg/dL
    HDL胆固醇：40 mg/dL
    甘油三酯：150 mg/dL
    谷丙转氨酶（ALT）：42 U/L
    谷草转氨酶（AST）：38 U/L
    总胆红素：0.8 mg/dL
    肌酐：1.2 mg/dL
    尿素氮：20 mg/dL
    ```

    ## 整体结论

    总胆固醇和LDL胆固醇水平在正常范围内。HDL胆固醇水平正常，但甘油三酯水平稍高。
    肝功能测试结果显示轻度升高，可能与高胆固醇药物有关。
    """
