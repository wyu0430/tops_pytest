# coding=utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import os
import datetime


# 一直等待某元素可见，默认超时10秒
def is_visible(locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


# 一直等待某个元素消失，默认超时10秒
def is_not_visible(locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False


def upload_photo(imgpath):
    os.system('upload.exe %s' % imgpath)

lp_xpath = '//*[@id="side-menu"]/li[2]/a'
ht_xpath = '//*[@id="side-menu"]/li[3]/a'
ht1_xpath = '//*[@id="side-menu"]/li[3]/ul/li[1]/a'
fyk_xpath = '//*[@id="side-menu"]/li[4]/a'
fyk_xflp_xpath = '//*[@id="side-menu"]/li[4]/ul/li[1]/a'
gzl_xpath = '//*[@id="side-menu"]/li[5]/a'
gzl_sh_xpath = '//*[@id="side-menu"]/li[5]/ul/li/a'
zzjg_xpath = '//*[@id="side-menu"]/li[6]/a'
zzjg_zz_xpath = '//*[@id="side-menu"]/li[6]/ul/li[1]/a'
building_list_xpath = '//*[@id="side-menu"]/li[2]/ul/li[1]/a'
url = 'http://bopsadmin.test.apitops.com'
user_name = 'autotest'
user_password = '123456'
user_building = 'auto_building'

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
begin = datetime.datetime.now()
driver.get(url)
i = 24
building_name = u'测试自动化楼盘' + str(i)
enterprise = u'杭州卡考一号'
driver.find_element_by_id('loginName').send_keys(user_name)
driver.find_element_by_id('password').send_keys(user_password)
driver.find_element_by_id('btnLoginCRM').click()
time.sleep(5)
# *************添加房源库****************
# ***************房源库************
# 滚动到房源库菜单
target = driver.find_element_by_xpath(fyk_xpath)
driver.execute_script("arguments[0].scrollIntoView();", target)
is_visible(fyk_xpath)
# 点击房源库
driver.find_element_by_xpath(fyk_xpath).click()
is_visible(fyk_xflp_xpath)
# 点击新房楼盘
driver.find_element_by_xpath(fyk_xflp_xpath).click()
time.sleep(2)
driver.switch_to.frame(1)
# *****************************************************
# 点击新增按钮
driver.find_element_by_xpath(u"//button[text()='新增']").click()
time.sleep(2)
# 输入内容
driver.find_element_by_id('name').send_keys(building_name)
driver.find_element_by_id('alias').send_keys(u"推广名称")
driver.find_element_by_id('projectCompany').send_keys(u"杭州销冠网络项目公司")
driver.find_element_by_id('developer').send_keys(u"杭州绿城开发商")
Select(driver.find_element_by_id('country')).select_by_visible_text(u'中国')
Select(driver.find_element_by_id('province')).select_by_visible_text(u'浙江省')
Select(driver.find_element_by_id('city')).select_by_visible_text(u'杭州市')
Select(driver.find_element_by_id('district')).select_by_visible_text(u'上城区')
Select(driver.find_element_by_id('block')).select_by_visible_text(u'钱江新城')
driver.find_element_by_id('address').send_keys(u"杭州市上城区钱江路58号太和广场8号楼_" + str(i))
driver.find_element_by_id('plotCode').send_keys('1122334455')
driver.find_element_by_class_name('icheckbox_minimal-orange').click()
driver.execute_script("$('#sellDate').removeAttr('readonly')") # jQuery，移除属性
driver.find_element_by_id('sellDate').send_keys('2017-12-15')
driver.find_element_by_id('sellDate').click()
driver.find_element_by_id('sellArea').send_keys('7777.77')
driver.find_element_by_id('floorAreaPrice').send_keys('3456.78')
# jQuery，移除属性
driver.execute_script("$('#preStartDate').removeAttr('readonly')")
driver.find_element_by_id('preStartDate').send_keys('2018-12-15')
driver.find_element_by_name('floorArea').send_keys('8000.88')
driver.find_element_by_name('coveredArea').send_keys('8888.88')
driver.find_element_by_name('averagePrice').send_keys('3000.23')
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/div/ul/li[2]/a/span[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/div/ul/li[3]/a/span[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/div/ul/li[5]/a/span[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/div/ul/li[15]/a/span[1]').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[18]/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[19]/div/div/label[3]/div/ins').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[20]/div/div/label[1]/div/ins').click()
driver.find_element_by_xpath('/html/body/div[1]/form/div[20]/div/div/label[2]/div/ins').click()
driver.find_element_by_id('introduction').send_keys(
   u'''这是一套自动化测试楼盘，总占地面积为2000万㎡，涵盖建面约88-130㎡精宅及建面约20-60㎡公寓产品。社区拥有现代典雅建筑、
艺术园林、六大全龄乐活空间，更配有约6667㎡商业、生活会所、泳池、休闲广场等。 项目地处东莞中心交通门户，
毗邻东莞火车站、轻轨R2号线茶山站；更有莞深高速、从莞深高速、东部快速干线等高速环绕，快速畅达广惠深等地。'''
)
for i in range(1, 7):
    driver.find_element_by_xpath("//div[@id='filePicker']/div[2]").click()
    time.sleep(1)
    upload_photo(r"E:\Image\building\{}.jpg".format(str(i)))
    time.sleep(1)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/form/div[25]/div/button[2]').click()
time.sleep(5)

driver.find_element_by_id('keyWord').send_keys(building_name)
time.sleep(1)
driver.find_element_by_class_name('search').click()
time.sleep(2)
driver.execute_script("$('.dis_n').addClass('show').removeClass('dis_n')")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tableList"]/tr/td[10]/div/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[3]').click()
time.sleep(1)
driver.find_element_by_id('zhouBianEdit').click()
time.sleep(1)
driver.find_element_by_id('site').clear()
driver.find_element_by_id('site').send_keys(u'位于中国杭州西湖边上，神一样的存在，很好很好的地段')
driver.find_element_by_id('facility').clear()
driver.find_element_by_id('facility').send_keys(
    u'''1、医疗：美国第四大医疗集团UIW /Christus，低成本享受亚洲顶尖的养老、医疗环境。周边有鹰阁医院、KPJ柔佛专科医院、立康专科医院，医疗有保障； '
2、生活：国际会所、滨海商业街、沙滩公园已投入使用，高星级酒店也即将开业！')'''
)
driver.find_element_by_id('transportation').clear()
driver.find_element_by_id( 'transportation').send_keys(
    u'''1、交通中心已投入使用。规划24小时穿梭巴士，直达新加坡莱佛士码头、樟宜机场；
2、乘坐飞机4-6小时到达大部分中国城市；
3、专属跨海大桥计划于2016年10月通车，快速连通新马大桥（2号桥），往返新加坡更便捷；
4、隆新高铁15分钟从新山到新加坡，90分钟从新加坡到吉隆坡。'''
)
driver.find_element_by_id('education').clear()
driver.find_element_by_id('education').send_keys(
   u'''1、已签约北京大学，清华大学，复旦大学，哈佛大学，反正就是很牛逼；
2、项目临近新加坡国立大学、南洋理工等多所世界一流高校名校。'''
)
driver.find_element_by_id('environment').send_keys(
    u''' 1、分层立体：十几平方公里的森林城市，地面都是公园；
2、垂直绿化：全世界独一无二，全城建筑外墙长满植物，目之所及皆是森林，让生活回归自然，回归健康。'''
)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/form/div[17]/div/button[1]').click()
time.sleep(1)

# ***************进入新房楼盘，在楼盘列表添加数据*******************
driver.switch_to.default_content()
driver.find_element_by_xpath(lp_xpath).click()
time.sleep(1)
driver.find_element_by_xpath(building_list_xpath).click()
time.sleep(1)

driver.switch_to.frame(2)
driver.find_element_by_id('js_add').click()
time.sleep(2)
driver.find_element_by_id('building_name').send_keys(building_name)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[3]/td/ul/li').click()
time.sleep(1)
Select(driver.find_element_by_id('js_CityCompanyOrgSel')).select_by_visible_text(u'杭州卡考网络科技有限公司')
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[8]/td/label[1]/div/ins').click()
# driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[9]/td/label[1]/div/ins').click()
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[10]/td/label[1]/div/ins').click()
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[10]/td/label[3]/div/ins').click()
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[10]/td/label[5]/div/ins').click()
driver.find_element_by_name('linkPhone').send_keys('057187770000')
driver.find_element_by_id('beginTime').send_keys('2017-12-01')
driver.find_element_by_id('endTime').send_keys('2020-12-01')
Select(driver.find_element_by_name('developerId')).select_by_visible_text(enterprise)
Select(driver.find_element_by_id('js_TasteAdminSel')).select_by_visible_text(u'杭州城市用体')
Select(driver.find_element_by_id('js_zhuChangSel')).select_by_visible_text(u'测试杭州用体')
Select(driver.find_element_by_id('js_saleAdminSel')).select_by_visible_text(u'用体专员吴')
driver.find_element_by_name('saleDivideRate').clear()
driver.find_element_by_name('saleDivideRate').send_keys('40')
driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[19]/td/div/div/div/span[2]').click()
driver.find_element_by_xpath('//*[@id="js_statu"]/div/div/span[2]').click()
# jQuery，移除属性
driver.execute_script("$('#sellDate').removeAttr('readonly')")
driver.find_element_by_id('openTime').send_keys('2017-12-1')
driver.find_element_by_id('openTime').click()
driver.find_element_by_xpath("//div[@id='pickerL']/div[2]").click()
time.sleep(1)
upload_photo(r"E:\Image\building\c.jpg")
time.sleep(5)
# 上传套图
for i in range(1, 6):
    driver.find_element_by_xpath("//div[@id='pickerT']/div[2]").click()
    time.sleep(1)
    upload_photo(r"E:\Image\building\a{}.jpg".format(str(i)))
    time.sleep(5)
# 上传户型图
for i in range(1, 4):
    driver.find_element_by_xpath("//div[@id='pickerR']/div[2]").click()
    time.sleep(1)
    upload_photo(r"E:\Image\building\b{}.jpg".format(str(i)))
    time.sleep(5)
for i in range(1, 4):
    driver.find_elements_by_id('hxTitle_')[i-1].send_keys(u'户型' + str(i) )
    driver.find_elements_by_id('hxArea_')[i * 2 - 1 - 1].send_keys('155.55')
    driver.find_elements_by_id('hxArea_')[i * 2 - 1].send_keys('170.77')
    driver.find_elements_by_id('hxDescription_')[i - 1].send_keys(u'平层')
    driver.find_elements_by_id('hxPrice_')[i - 1].send_keys('25500.64')
    driver.find_elements_by_class_name('item_sort')[i - 1].send_keys(str(i))
    driver.find_elements_by_class_name('item_houseRoomTypeS')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeT')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeC')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeW')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeY')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeK')[i - 1].clear()
    driver.find_elements_by_class_name('item_houseRoomTypeS')[i - 1].send_keys(3)
    driver.find_elements_by_class_name('item_houseRoomTypeT')[i - 1].send_keys(2)
    driver.find_elements_by_class_name('item_houseRoomTypeC')[i - 1].send_keys(1)
    driver.find_elements_by_class_name('item_houseRoomTypeW')[i - 1].send_keys(2)
    driver.find_elements_by_class_name('item_houseRoomTypeY')[i - 1].send_keys(1)
    driver.find_elements_by_class_name('item_houseRoomTypeK')[i - 1].send_keys(1)
driver.find_element_by_name('plate').send_keys(u'自动化的板块')
driver.find_element_by_name('mainHouseType').send_keys(u'主打户型1')
driver.find_element_by_name('theAvgPrice').clear()
driver.find_element_by_name('theAvgPrice').send_keys('25500.64')
driver.find_element_by_name('theLowestPrice').clear()
driver.find_element_by_name('theLowestPrice').send_keys('18000')
Select(driver.find_element_by_id('F_WeiXinPushTimeStart')).select_by_visible_text('6:30')
Select(driver.find_element_by_id('F_WeiXinPushTimeEnd')).select_by_visible_text('22:00')
# 标签
# print driver.find_elements_by_class_name('icheckbox_minimal-orange')
driver.find_elements_by_class_name('icheckbox_minimal-orange')[0].click()
driver.find_elements_by_class_name('icheckbox_minimal-orange')[1].click()
driver.find_elements_by_class_name('icheckbox_minimal-orange')[2].click()
time.sleep(5)
driver.find_element_by_id('js_save').click()
# ***************添加合同**********************
# driver.switch_to.default_content()
# driver.switch_to.frame(3)
driver.switch_to.default_content()
driver.find_element_by_xpath(ht_xpath).click()
time.sleep(1)
driver.find_element_by_xpath(ht1_xpath).click()
time.sleep(2)
driver.switch_to.frame(3)
driver.find_element_by_xpath('//*[@id="toolBox"]/div[2]/button[1]').click()
time.sleep(3)
Select(driver.find_element_by_class_name('form-control')).select_by_visible_text(u'新房-本地分销')
time.sleep(2)
driver.find_element_by_id('PartyABusiness').send_keys(enterprise)

time.sleep(2)
driver.find_element_by_xpath('//*[@id="contstepbussiness"]/div/div/div[2]/div[1]/div/div/div/ul').click()
time.sleep(1)
driver.find_element_by_id('products').send_keys(building_name)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="contstepbussiness"]/div/div/div[3]/div[1]/div/div/div/ul').click()
time.sleep(1)
driver.find_element_by_id('PartyBBusiness').send_keys(u'杭州卡考网络科技有限公司')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="contstepbussiness"]/div/div/div[2]/div[2]/div/div/div/ul').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[2]/div[9]/button[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button[1]').click()
time.sleep(2)
# 基本信息页面
driver.find_element_by_name('forsaleAmount').send_keys(1000)
# # jQuery，移除属性
# driver.execute_script("$('#sellDate').removeAttr('readonly')")
driver.find_element_by_id('conteffectBeginTime').send_keys('2017-12-20')
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[1]/ul/li[2]').click()
driver.find_element_by_id('conteffecteffectEndTime').send_keys('2020-12-20')
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[1]/ul/li[2]').click()
driver.find_element_by_name('expireDaysDeal').send_keys(20)
driver.find_element_by_name(u'甲方联系人1').send_keys(u'吕俊杰')
driver.find_element_by_name(u'甲方联系人2').send_keys('18958033079')
driver.find_element_by_name(u'甲方联系人3').send_keys('lvjunjie2757@tops001.com')
driver.find_element_by_name('foreVisitProtectDays').send_keys(5)
driver.find_element_by_name('foreCallinProtectDays').send_keys(6)
driver.find_element_by_name('mustVisitInDays').send_keys(7)
driver.find_element_by_name('backProtectDays').send_keys(8)
driver.find_element_by_name('paybackInDays').send_keys(25)
driver.find_elements_by_name('accountsIdentifiedCondition')[0].click()
driver.find_elements_by_name('dealConfirmMethod')[1].click()
driver.find_elements_by_name('dealConfirmMethod')[0].click()
driver.find_elements_by_name('docType')[2].click()

driver.find_element_by_xpath("//div[@id='filePicker1']/div[2]").click()
time.sleep(5)
upload_photo(r"E:\Image\building\ht1.pdf")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[2]/div[9]/button[2]').click()
time.sleep(2)
# 回款方案
driver.find_element_by_xpath(u"//button[text()='+新建']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="regongshi"]/form/div[1]/div[2]/div/div/div[4]').click()
driver.find_element_by_name('amount').send_keys('1000')
driver.find_element_by_name('ratio').send_keys('5')
time.sleep(3)
driver.find_element_by_id('choose2').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[2]/div[9]/button[2]').click()
time.sleep(2)
# print driver.find_elements_by_xpath(u"//button[text()='+新建']")
driver.find_elements_by_xpath(u"//button[text()='+新建']")[1].click()
time.sleep(1)
driver.find_elements_by_name('amount')[1].send_keys(1000)
driver.find_elements_by_name('ratio')[1].send_keys(5)
driver.find_element_by_xpath('//*[@id="choosesubmitUnify"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[2]/div[9]/button[2]').click()
time.sleep(2)
# 合同标签
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[1]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[2]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[3]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[4]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[5]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[6]/div/div/div[2]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[7]/div/div/div[3]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[8]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[9]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[10]/div/div/div[1]/label').click()
driver.find_element_by_xpath('//*[@id="contsteptags"]/div/div/div[11]/div/div/div[1]/label').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="routeWrapper"]/div/div/div/div/div[2]/div[9]/button[3]').click()
# ************工作流审核*****************
driver.switch_to.default_content()
target = driver.find_element_by_xpath(gzl_xpath)
driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_xpath(gzl_xpath).click()
time.sleep(2)
driver.find_element_by_xpath(gzl_sh_xpath).click()
time.sleep(2)
driver.switch_to.frame(4)
driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
driver.switch_to.default_content()
driver.switch_to.frame(5)
driver.find_element_by_id('btnPass').click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame(4)

driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[11]/a').click()
driver.switch_to.default_content()
driver.switch_to.frame(5)
driver.find_element_by_id('btnPass').click()
time.sleep(5)
# ***************返回新房楼盘，开通销冠经纪*****************
driver.switch_to.default_content()
driver.find_element_by_xpath(lp_xpath).click()
time.sleep(1)
driver.find_element_by_xpath(building_list_xpath).click()
time.sleep(1)
driver.switch_to.frame(2)
driver.find_element_by_xpath('//*[@id="js-table-list"]/tr[1]/td[13]/a[1]').click()
target = driver.find_element_by_xpath('//*[@id="js-infosCtBuliding"]/div[1]/table/tbody/tr[35]/th')
driver.execute_script("arguments[0].scrollIntoView();", target)
driver.find_element_by_xpath('//*[@id="js_wei"]/div/div/span[2]').click()
driver.find_element_by_xpath('//*[@id="CheckIsRealTime"]/div/div/span[2]').click()
time.sleep(2)
target = driver.find_element_by_id('js_save')
driver.execute_script("arguments[0].scrollIntoView();", target)
time.sleep(5)
# print driver.find_elements_by_id('js_save')
driver.find_element_by_id('js_save').click()
# *************组织架构增加新房管理员*************
driver.switch_to.default_content()
driver.find_element_by_xpath(zzjg_xpath).click()
time.sleep(1)
driver.find_element_by_xpath(zzjg_zz_xpath).click()
time.sleep(1)
driver.switch_to.frame(5)

driver.find_element_by_id('company-keyWord').send_keys(building_name)
time.sleep(1)
driver.find_element_by_id('companySearchBtn').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/div/ul[2]/li[2]/span[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="p-treeList"]/li[2]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[4]/div[1]/span[4]').click()
time.sleep(1)
Select(driver.find_element_by_id('selUserType')).select_by_visible_text(u'登录名')
driver.find_element_by_id('txtTestFocus').send_keys(user_building)
driver.find_element_by_id('btnSearchUser').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="searchUserResults"]/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="am-pannel-add-3"]/div/div[2]/form/div[3]/button[1]').click()
end = datetime.datetime.now()
print building_name + '添加完成'
print '耗时：' + str(end - begin)
time.sleep(10)
driver.quit()
