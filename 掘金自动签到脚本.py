import requests
import time
import datetime

def my_function():
    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))) # 北京时间
    try:
        response = requests.get("https://api.juejin.cn/growth_api/v1/")
        response.raise_for_status()
        print(f"[{timestamp}] API 请求成功")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] API 请求失败: {e}")

def check_sign_in_status(base_url, headers):
    api = "get_today_status"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['err_no'] == 0:
            if data['data'] is True:
                print("【今日是否签到】", "已签到")
                return True
            elif data['data'] is False:
                print("【今日是否签到】", "未签到")
                return False
        else:
            print("【当前登录状态】", "未登录,请登录")
            pass
            return False
    else:
        print("【请求失败】", response.status_code)
        return False


def sign_in(base_url, params, headers):
    # data = '{}'
    data = ''
    url = f"{base_url}check_in"
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【当前签到状态】", "签到成功")
                return True
            elif data['err_no'] == 3013 and data['err_msg'] == "掘金酱提示：签到失败了~":
                print("【当前签到状态】", data['err_msg'])
                return False
            elif data['err_no'] == 15001:
                print("【当前签到状态】", '重复签到')
                return True
            else:
                print("【当前签到状态】", data['err_msg'])
                return False
        except requests.JSONDecodeError:
            print("【签到功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_points(base_url, headers):
    api = "get_cur_point"
    url = base_url + api
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【矿石最新余额】", data['data'])
                return data['data']
        except requests.JSONDecodeError:
            print("【获取余额功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_free(base_url,params, headers):
    url = f"{base_url}lottery_config/get"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                if data['data']['free_count'] > 0:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return True
                else:
                    print("【免费抽奖次数】", data['data']['free_count'])
                    return False
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False


def draw(base_url, params, headers):
    url = f"{base_url}lottery/draw"
    # data = '{}'
    data = ''
    response = requests.post(url, headers=headers, data=data,params=params)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                print("【今日抽奖奖品】", data['data']['lottery_name'])
        except requests.JSONDecodeError:
            print("【抽奖功能】服务器返回的数据无法解析为JSON格式。")
            return False


def get_win(base_url, aid, uuid, spider, headers):
    api = "lottery_lucky/my_lucky"
    url = base_url + api
    data = {
        "aid": aid,
        "uuid": uuid,
        "spider": spider
    }
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            if data['err_no'] == 0 and data['err_msg'] == "success":
                total_value = data['data']['total_value']
                points = get_points(base_url, header1)
                cha = points - (6000 - total_value) * 20
                print("【当前幸运数值】：", total_value)
                if cha >= 0:
                    print("【距离中奖还差】：0 矿石！")
                elif cha <= 0:
                    print("【距离中奖还差】：", str(abs(cha)) + "矿石！")
        except requests.JSONDecodeError:
            print("【获取免费抽奖次数功能】服务器返回的数据无法解析为JSON格式。")
            return False
    else:
        print("【请求失败】", response.status_code)
        return False



if __name__ == "__main__":
    my_function()
    # 点击任意类型为fetch的网络请求
    cookie ="__tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227419957518539048474%2522%252C%2522user_unique_id%2522%253A%25227419957518539048474%2522%252C%2522timestamp%2522%253A1727593501577%257D; is_staff_user=false; store-region=cn-sx; store-region-src=uid; _tea_utm_cache_2608={%22utm_source%22:%22web%22%2C%22utm_medium%22:%22banner%22%2C%22utm_campaign%22:%22xly2025%22}; _tea_utm_cache_2018={%22utm_source%22:%22web%22%2C%22utm_medium%22:%22banner%22%2C%22utm_campaign%22:%22xly2025%22}; passport_csrf_token=d6993ef9a9e67b33444bf4b3eb35fa41; passport_csrf_token_default=d6993ef9a9e67b33444bf4b3eb35fa41; odin_tt=b66d1ad63e0ca59f3b5d16a7201cabf3573ca8ea6c7c1ea59fded8c51eb3f8c7d2b48df790f8ddf985381e76080cda9c4050ae4b12078ad79110507c0e9e097c; n_mh=L87qwvCoqH7EAa9jtaR8r3BZ6rOsbnMXVkE8qLt7CuY; passport_auth_status=5dfc263473d68e920b9a990a3063c635%2C48a017f305b95384480ea1cb298b0f99; passport_auth_status_ss=5dfc263473d68e920b9a990a3063c635%2C48a017f305b95384480ea1cb298b0f99; sid_guard=ca35d2cdd9067fbcf9ca6155c1efe1b6%7C1750858285%7C31536000%7CThu%2C+25-Jun-2026+13%3A31%3A25+GMT; uid_tt=52bff8162dbe1c2ed813b1922bd1b687; uid_tt_ss=52bff8162dbe1c2ed813b1922bd1b687; sid_tt=ca35d2cdd9067fbcf9ca6155c1efe1b6; sessionid=ca35d2cdd9067fbcf9ca6155c1efe1b6; sessionid_ss=ca35d2cdd9067fbcf9ca6155c1efe1b6; sid_ucp_v1=1.0.0-KGQ3MzczMTBjODdmYzc5N2YyYzcyMWUzNDhmMTdjOTk3Yzg3YjMzYzIKFwitrtDnqs2gAhCt9O_CBhiwFDgCQPEHGgJsZiIgY2EzNWQyY2RkOTA2N2ZiY2Y5Y2E2MTU1YzFlZmUxYjY; ssid_ucp_v1=1.0.0-KGQ3MzczMTBjODdmYzc5N2YyYzcyMWUzNDhmMTdjOTk3Yzg3YjMzYzIKFwitrtDnqs2gAhCt9O_CBhiwFDgCQPEHGgJsZiIgY2EzNWQyY2RkOTA2N2ZiY2Y5Y2E2MTU1YzFlZmUxYjY; csrf_session_id=4334234defb2f143f9aa5cae031a4223"
    aid = "2608"
    uuid = "7419957518539048474"
    spider = "0"
    # msToken  获取后测试 url解码
    # 解密网址1:https://www.toolhelper.cn/EncodeDecode/Url
    # 解密网址2:https://www.bejson.com/enc/urlencode/index.html#google%20vignette

    msToken = 'alTCgamFmIowM_UyCs-V-RlVWatArDfnP3OEOZW8RgtOit2hnVBDv76Q3n46AiCLzDnTzXHw47xqEmxnkJpAvm2R1QmjSBOiNFjfcMerswKzmTFUOYn0yOmACHkzaiSHTRY='
    a_bogus = 'xyMQ6c2hMsm1efVzlwDz9twmuFR0YW5agZEz7ylNjtqS'
    base_url = "https://api.juejin.cn/growth_api/v1/"

    common_params = {"aid": aid, "uuid": uuid, "spider": spider, "msToken": msToken, "a_bogus": a_bogus}
    header1 = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }

    if check_sign_in_status(base_url, header1):
        if get_free(base_url,common_params, header1):
            draw(base_url,common_params, header1)
            pass
        else:
            pass
    else:
        if not sign_in(base_url, common_params, header1):
            sign_in(base_url, common_params, header1)
        if get_free(base_url,common_params, header1):
            draw(base_url, common_params, header1)
            pass
        else:
            pass
    get_win(base_url, aid, uuid, spider, header1)
