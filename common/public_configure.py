# coding=utf-8

base_url = 'http://gateway.test.apitops.com'
gateway_url_test = 'http://gateway.test.apitops.com'
gateway_url_dev = 'http://gateway.dev.apitops.com'
gateway_url_beta = 'http://gateway.beta.apitops.com'
active_url_dev = 'http://activity.dev.apitops.com'
gateway_url_ga = 'http://gateway.apitops.com'
brokerService_url_dev = 'http://broker-service.dev.apitops.com'
brokerService_url_test = 'http://broker-service.test.apitops.com'
brokerService_url_ga = 'http://broker-service.apitops.com'
active_url_test = 'http://activity.test.apitops.com'
active_url_beta = 'http://activity.beta.apitops.com'
active_url_ga = 'http://activity.apitops.com'
bops_url_test = 'http://bopsadmin.test.apitops.com/'
bops_url_test = 'http://bopsadmin.test.apitops.com/'

brokeroa_url_test = 'http://brokeroa.test.apitops.com'
brokeroa_url_ga = 'http://brokeroa.apitops.com'



class PublicConfigure(object):


    @staticmethod
    def random_name():  # 随机姓名
        import random as r
        a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何',
              '吕',
              '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘',
              '葛',
              '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费',
              '廉',
              '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐',
              '康',
              '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米',
              '贝',
              '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

        a2 = ['玉', '明', '龙', '芳', '军', '玲', '俊', '赫', '梦', '天', '人', '阿', '加', '来', '顺', '仍', '严']

        a3 = ['', '立', '玲', '杰', '国']

        name = r.choice(a1) + r.choice(a2) + r.choice(a3)
        return name

    @staticmethod
    def random_family_name():  # 随机生成姓
        import random as r
        a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许', '何',
              '吕',
              '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘',
              '葛',
              '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费',
              '廉',
              '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐',
              '康',
              '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹', '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米',
              '贝',
              '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
        family_name = r.choice(a1)
        return family_name

    @staticmethod
    def random_phone():  # 随机手机号码
        import random
        phone_no = random.choice(
            ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '147', '151', '153', '155', '157', '170',
             '177', '180', '181', '183', '185', '186', '187', '189']) + "".join(
            random.choice("0123456789") for i in range(8))
        return phone_no

