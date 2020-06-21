import requests, json
import openpyxl

wb = openpyxl.Workbook() #创建工作簿
ws = wb.active #创建工作表
ws.title = 'LOL数据'
ws.append(['胜负', '击杀', '死亡', '助攻', '总伤害', '放置守卫数', '击杀守卫数', '挣金币数', '击杀小兵数', '摧毁水晶数'])#创建第一行
url = 'https://lol.sw.game.qq.com/lol/api/?c=Battle&a=matchList&areaId=2&accountId=2387597048366336&queueId=70,72,73,75,76,78,96,98,100,300,310,313,317,318,325,400,420,430,450,460,600,610,940,950,960,980,990,420,440,470,83,800,810,820,830,840,850&r1=matchList'
headers = {'Cookie': 'pgv_pvid=8662076176; pgv_pvi=6065800192; RK=z6owxiYTc7; ptcz=4e72aa081ca497e6cb5508393e762bf42613ec661832bed3da614c085b06038b; pgv_info=ssid=s5910606700; eas_sid=51U5Y9W2A6H7L0A6H7g8h8Q293; tokenParams=%3Fe_code%3D507042; _qpsvr_localtk=0.2820418539687559; pgv_si=s3299445760; ptui_loginuin=1480594519; LOLWebSet_AreaBindInfo_1480594519=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221480594519%2522%252C%2522rolename%2522%253A%2522%25E7%2596%25AF%25E7%258B%2582%25E8%2583%258C%25E5%258C%2585123%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1480594519%257C2%257C1480594519*%257C%257C%257C%257C%2525E7%252596%2525AF%2525E7%25258B%252582%2525E8%252583%25258C%2525E5%25258C%252585123*%257C%257C%257C1592670713%2522%252C%2522md5str%2522%253A%2522EA459D784200E1D67BD26C5F63A491DB%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D; lolqqcomrouteLine=index-tool_index-page_index-page_index-page_main_data_space; uin=o3581780173; skey=@oXsMsYY1O; p_uin=o3581780173; pt4_token=rTfGFfP5c7uEPFcLcl2A9N2JlQt0FGq0SnfAdihLDCQ_; p_skey=J1PeEq5RzqDipvrsJ0nXaLPhzlXqZ9WmzZ07bWMiGmQ_; IED_LOG_INFO2=userUin%3D3581780173%26nickName%3D%2525E5%2525B9%2525B3%2525E8%2525B3%252580%2525E9%25259B%2525BB%2525E7%2525AE%252597%2525E9%25259D%252588%2525E5%2525BC%25258F%2525E8%2525A9%2525A6%2525E8%2525A1%25258C%2525E6%2525A9%25259F%26nickname%3D%25E5%25B9%25B3%25E8%25B3%2580%25E9%259B%25BB%25E7%25AE%2597%25E9%259D%2588%25E5%25BC%258F%25E8%25A9%25A6%25E8%25A1%258C%25E6%25A9%259F%26userLoginTime%3D1592729090%26logtype%3Dqq%26loginType%3Dqq%26uin%3D3581780173; uin_cookie=o3581780173; ied_qq=o3581780173; LOLWebSet_AreaBindInfo_3581780173=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25223581780173%2522%252C%2522rolename%2522%253A%2522Karlkono%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C3581780173%257C2%257C3581780173*%257C%257C%257C%257CKarlkono*%257C%257C%257C1592729094%2522%252C%2522md5str%2522%253A%2522582A268524E4A70C2B28B5B089119E81%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,      		like Gecko) Chrome/80.0.3987.122 Safari/537.36'}  # 防止反爬虫
# 获取网页源代码
res = requests.get(url, headers=headers)  # 解析这个网页
json_1 = json.loads(res.text[16:])  # 因为response的前面16个字符不是json格式的,所有要去除
# 获取所有游戏的gameId
games = json_1['msg']['games']  # 获取所有game信息的列表
gameIds = []  # 创建一个存放gameId的列表
for game in games:
    gameId = game['gameId']
    gameIds.append(gameId)
for i in gameIds[:20]:
    url2 = 'https://lol.sw.game.qq.com/lol/api/?c=Battle&a=combatGains&areaId=2&gameId=' + str(i) + '&r1=combatGains'#导入一局游戏的url
    headers = {'cookie': 'pgv_pvid=8662076176; pgv_pvi=6065800192; RK=z6owxiYTc7; ptcz=4e72aa081ca497e6cb5508393e762bf42613ec661832bed3da614c085b06038b; pgv_info=ssid=s5910606700; eas_sid=51U5Y9W2A6H7L0A6H7g8h8Q293; tokenParams=%3Fe_code%3D507042; _qpsvr_localtk=0.2820418539687559; pgv_si=s3299445760; ptui_loginuin=1480594519; LOLWebSet_AreaBindInfo_1480594519=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25221480594519%2522%252C%2522rolename%2522%253A%2522%25E7%2596%25AF%25E7%258B%2582%25E8%2583%258C%25E5%258C%2585123%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C1480594519%257C2%257C1480594519*%257C%257C%257C%257C%2525E7%252596%2525AF%2525E7%25258B%252582%2525E8%252583%25258C%2525E5%25258C%252585123*%257C%257C%257C1592670713%2522%252C%2522md5str%2522%253A%2522EA459D784200E1D67BD26C5F63A491DB%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D; lolqqcomrouteLine=index-tool_index-page_index-page_index-page_main_data_space; uin=o3581780173; skey=@oXsMsYY1O; p_uin=o3581780173; pt4_token=rTfGFfP5c7uEPFcLcl2A9N2JlQt0FGq0SnfAdihLDCQ_; p_skey=J1PeEq5RzqDipvrsJ0nXaLPhzlXqZ9WmzZ07bWMiGmQ_; IED_LOG_INFO2=userUin%3D3581780173%26nickName%3D%2525E5%2525B9%2525B3%2525E8%2525B3%252580%2525E9%25259B%2525BB%2525E7%2525AE%252597%2525E9%25259D%252588%2525E5%2525BC%25258F%2525E8%2525A9%2525A6%2525E8%2525A1%25258C%2525E6%2525A9%25259F%26nickname%3D%25E5%25B9%25B3%25E8%25B3%2580%25E9%259B%25BB%25E7%25AE%2597%25E9%259D%2588%25E5%25BC%258F%25E8%25A9%25A6%25E8%25A1%258C%25E6%25A9%259F%26userLoginTime%3D1592729090%26logtype%3Dqq%26loginType%3Dqq%26uin%3D3581780173; uin_cookie=o3581780173; ied_qq=o3581780173; LOLWebSet_AreaBindInfo_3581780173=%257B%2522areaid%2522%253A%25222%2522%252C%2522areaname%2522%253A%2522%25E6%25AF%2594%25E5%25B0%2594%25E5%2590%2589%25E6%25B2%2583%25E7%2589%25B9%2520%25E7%25BD%2591%25E9%2580%259A%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25223581780173%2522%252C%2522rolename%2522%253A%2522Karlkono%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C3581780173%257C2%257C3581780173*%257C%257C%257C%257CKarlkono*%257C%257C%257C1592729094%2522%252C%2522md5str%2522%253A%2522582A268524E4A70C2B28B5B089119E81%2522%252C%2522roleareaid%2522%253A%25222%2522%252C%2522sPartition%2522%253A%25222%2522%257D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}  # 防止反爬虫
    res2 = requests.get(url2, headers=headers)
    json_2 = json.loads(res2.text[18:])  # 将源代码前面不是json格式的去掉
    participants = json_2['msg']['participants']  # 获取战绩列表
    #找到自己的战绩
    for own in participants:
        if own['summonerName'] == 'Karlkono':  # 输入自己的游戏ID,如果匹配,就继续执行下面的代码,否则跳过
            try:  # 有的游戏某一项没有数据,用try防止报错,
                stats = own['stats']  # 转到stats这一项中,有战斗数据
                win = stats['win']
                kills = stats['kills']
                deaths = stats['deaths']
                assists = stats['assists']
                damage = stats['totalDamageDealtToChampions']
                wardsPlaced = stats['wardsPlaced']
                wardsKilled = stats['wardsKilled']
                goldEarned = stats['goldEarned']
                minionsKilled = stats['minionsKilled']
                inhibitorKills = stats['inhibitorKills']
                ws.append([win, kills, deaths, assists, damage, wardsPlaced, wardsKilled, goldEarned, minionsKilled, inhibitorKills])
            except:
                print(i)  # 输出没游戏数据的gameId
    else:
        pass
wb.save('LOL数据.xlsx')