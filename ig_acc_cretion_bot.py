import requests
import random
import time
import sys
import os
from cfonts import render

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
bold = '\033[1m'
end = '\033[0m'

def clearScreen():
    os.system('clear')

def printBanner():
    banner = render("ESE", colors=["white", "yellow"], align="center")
    print(banner)

def animateText(text, color='white'):
    color_code = globals().get(color, white)
    for char in text:
        print(f"{color_code}{char}{end}", end='', flush=True)
        time.sleep(0.03)
    print()

def getPasswordInput():
    animateText("🔐 𝗘𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗱𝗲𝘀𝗶𝗿𝗲𝗱 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱: ", "cyan")
    password = input(f"{cyan}▸▸▸ {end}").strip()
    if not password:
        animateText("❌ 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗲𝗺𝗽𝘁𝘆!", "red")
        sys.exit()
    return password

def encryptPassword(password):
    return f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{password}'

def sendTelegram(username, password, fullname, userid, sessionid, telegram_token, telegram_chat_id):
    if not telegram_token or not telegram_chat_id:
        return
    
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    message = f"""
𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗖𝗥𝗘𝗔𝗧𝗜𝗢𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ▸▸▸ {username}
𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ▸▸▸ {password}
𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲 ▸▸▸ {fullname}
𝗨𝘀𝗲𝗿 𝗜𝗗 ▸▸▸ {userid}
𝗡𝗢𝗡𝗖𝗘 𝗧𝗢𝗞𝗘𝗡 ▸▸▸ {sessionid}
𝗡𝗼𝘁𝗲 ▸▸▸ Please Do Not Share These Details
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    params = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    try:
        response = requests.get(url, params=params, timeout=10)
    except:
        pass

def getEmailInput():
    email = input(f"{cyan}𝗣𝗹𝗲𝗮𝘀𝗲 𝗲𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗲𝗺𝗮𝗶𝗹 𝗮𝗱𝗱𝗿𝗲𝘀𝘀 {yellow}➠ {end}").strip()
    if not email:
        animateText("❌ 𝗘𝗺𝗮𝗶𝗹 𝗰𝗮𝗻𝗻𝗼𝘁 𝗯𝗲 𝗲𝗺𝗽𝘁𝘆!", "red")
        sys.exit()
    return email

def getTelegramCredentials():
    animateText("🤖 𝗗𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘀𝗲𝘁𝘂𝗽 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗻𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻𝘀? (𝘆/𝗻): ", "cyan")
    choice = input(f"{cyan}▸▸▸ {end}").lower().strip()
    if choice == 'y':
        animateText("🔑 𝗘𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗕𝗼𝘁 𝗧𝗼𝗸𝗲𝗻: ", "blue")
        token = input(f"{blue}▸▸▸ {end}").strip()
        animateText("💬 𝗘𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗖𝗵𝗮𝘁 𝗜𝗗: ", "blue")
        chat_id = input(f"{blue}▸▸▸ {end}").strip()
        return token, chat_id
    return '', ''

def createAccount(email, password, telegram_token, telegram_chat_id, fullname="TEAM7X"):
    encryptedPassword = encryptPassword(password)
    cookiesData = {
        'csrftoken': 'nu94r8FbL9bCmhtUkJuCPK',
        'mid': 'aQLm1gABAAE842f-IkSwe_vjC30a',
        'datr': '1eYCaXxZangEyVhuLFgYLFCM',
        'ig_did': '997BCE58-8A0A-44B9-97D3-868C981F2DB0',
        'ig_nrcb': '1',
        'dpr': '3.558248996734619',
        'wd': '774x1471',
    }
    headersData = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-csrftoken': 'nu94r8FbL9bCmhtUkJuCPK',
        'x-ig-app-id': '936619743392459',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'
    }
    animateText("🚀 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗮𝗰𝗰𝗼𝘂𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗰𝗲𝘀𝘀...", "purple")
    dataPayload = {
        'enc_password': encryptedPassword,
        'email': email,
        'failed_birthday_year_count': '{}',
        'first_name': fullname,
        'username': '',
        'client_id': 'aQLm1gABAAE842f-IkSwe_vjC30a',
        'seamless_login_enabled': '1',
        'opt_into_one_tap': 'false',
        'use_new_suggested_user_name': 'true',
        'jazoest': '21906',
    }
    try:
        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
            cookies=cookiesData,
            headers=headersData,
            data=dataPayload
        )
        usernameSuggested = None
        if '"message": "This field is required."' in response.text:
            jsonData = response.json()
            usernameSuggested = jsonData.get("username_suggestions", [None])[0]
        if usernameSuggested:
            dataPayload['username'] = usernameSuggested
            responseTwo = requests.post(
                'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
                cookies=cookiesData,
                headers=headersData,
                data=dataPayload
            )
            if '"dryrun_passed":true' in responseTwo.text:
                animateText("✅ 𝗦𝘁𝗲𝗽 𝟭 ▸▸▸ 𝗗𝗿𝘆𝗿𝘂𝗻 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹", "green")
            else:
                animateText("❌ 𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗮 𝗳𝗲𝘄 𝗺𝗶𝗻𝘂𝘁𝗲𝘀 𝗯𝗲𝗳𝗼𝗿𝗲 𝗿𝗲𝘁𝗿𝘆𝗶𝗻𝗴", "red")
                return False
    except Exception as e:
        animateText(f"⚠️  𝗘𝗿𝗿𝗼𝗿 𝗶𝗻 𝘀𝘁𝗲𝗽 𝟭: {str(e)}", "yellow")
        return False

    dobData = {
        'day': '15',
        'month': '4',
        'year': '2006',
        'jazoest': '21906',
    }
    response = requests.post(
        'https://www.instagram.com/api/v1/web/consent/check_age_eligibility/',
        cookies=cookiesData,
        headers=headersData,
        data=dobData,
    )
    if '"eligible_to_register":true' in response.text:
        animateText("✅ 𝗦𝘁𝗲𝗽 𝟮 ▸▸▸ 𝗔𝗴𝗲 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹", "green")
    else:
        animateText("❌ 𝗔𝗴𝗲 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗳𝗮𝗶𝗹𝗲𝗱", "red")
        return False

    emailData = {
        'device_id': 'aQLm1gABAAE842f-IkSwe_vjC30a',
        'email': email,
        'jazoest': '21906',
    }
    response = requests.post(
        'https://www.instagram.com/api/v1/accounts/send_verify_email/',
        cookies=cookiesData,
        headers=headersData,
        data=emailData,
    )
    if '"email_sent":true' in response.text:
        animateText("📨 𝗩𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗲𝗺𝗮𝗶𝗹 𝘀𝗲𝗻𝘁! 𝗖𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝗶𝗻𝗯𝗼𝘅", "cyan")
        otpCode = input(f"{yellow}🔢 𝗘𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗢𝗧𝗣 𝗰𝗼𝗱𝗲 ▸▸▸ {end}").strip()
    else:
        animateText("❌ 𝗘𝗺𝗮𝗶𝗹 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗳𝗮𝗶𝗹𝗲𝗱", "red")
        return False

    if not otpCode:
        animateText("❌ 𝗡𝗼 𝗢𝗧𝗣 𝗽𝗿𝗼𝘃𝗶𝗱𝗲𝗱", "red")
        return False

    otpData = {
        'code': otpCode,
        'device_id': 'aQLm1gABAAE842f-IkSwe_vjC30a',
        'email': email,
        'jazoest': '21906',
    }
    response = requests.post(
        'https://www.instagram.com/api/v1/accounts/check_confirmation_code/',
        cookies=cookiesData,
        headers=headersData,
        data=otpData,
    )
    if '"signup_code"' in response.text:
        jsonData = response.json()
        signupCode = jsonData.get("signup_code", "")
        animateText("✅ 𝗦𝘁𝗲𝗽 𝟯 ▸▸▸ 𝗢𝗧𝗣 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹", "green")
    else:
        animateText("❌ 𝗢𝗧𝗣 𝘃𝗲𝗿𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗳𝗮𝗶𝗹𝗲𝗱", "red")
        return False

    finalData = {
        'enc_password': encryptedPassword,
        'day': '15',
        'email': email,
        'failed_birthday_year_count': '{}',
        'first_name': fullname,
        'month': '4',
        'username': usernameSuggested,
        'year': '2006',
        'client_id': 'aQLm1gABAAE842f-IkSwe_vjC30a',
        'seamless_login_enabled': '1',
        'tos_version': 'row',
        'force_sign_up_code': signupCode,
        'extra_session_id': 'qtfawi:xs4duo:iku1ev',
        'jazoest': '21906',
    }
    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
        cookies=cookiesData,
        headers=headersData,
        data=finalData,
    )
    if '"account_created":true' in response.text:
        animateText("🎉 𝗦𝘁𝗲𝗽 𝟰 ▸▸▸ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹!", "green")
        jsonData = response.json()
        userId = jsonData.get("user_id", "")
        sessionId = jsonData.get("nonce", "")
        if telegram_token and telegram_chat_id:
            sendTelegram(usernameSuggested, password, fullname, userId, sessionId, telegram_token, telegram_chat_id)
        print(f"""
{green}{bold}
✨ 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗖𝗥𝗘𝗔𝗧𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📛 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 ▸▸▸ {usernameSuggested}
🔐 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 ▸▸▸ {password}
👤 𝗙𝘂𝗹𝗹 𝗡𝗮𝗺𝗲 ▸▸▸ {fullname}
🆔 𝗨𝘀𝗲𝗿 𝗜𝗗 ▸▸▸ {userId}
🔒 𝗡𝗢𝗡𝗖𝗘 𝗧𝗢𝗞𝗘𝗡 ▸▸▸ {sessionId}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{end}
""")
        return True
    elif '"code": "email_code_incorrect"' in response.text:
        animateText("❌ 𝗜𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗢𝗧𝗣 𝗰𝗼𝗱𝗲", "red")
        newOtp = input(f"{yellow}🔢 𝗘𝗻𝘁𝗲𝗿 𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗢𝗧𝗣 𝗰𝗼𝗱𝗲 ▸▸▸ {end}").strip()
        finalData['force_sign_up_code'] = newOtp
        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/',
            cookies=cookiesData,
            headers=headersData,
            data=finalData,
        )
        if '"account_created":true' in response.text:
            animateText("🎉 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹 𝗮𝗳𝘁𝗲𝗿 𝗢𝗧𝗣 𝗿𝗲𝘁𝗿𝘆!", "green")
            jsonData = response.json()
            userId = jsonData.get("user_id", "")
            sessionId = jsonData.get("nonce", "")
            if telegram_token and telegram_chat_id:
                sendTelegram(usernameSuggested, password, fullname, userId, sessionId, telegram_token, telegram_chat_id)
            return True
        else:
            animateText("❌ 𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗳𝗮𝗶𝗹𝗲𝗱 𝗮𝗳𝘁𝗲𝗿 𝗿𝗲𝘁𝗿𝘆", "red")
            return False
    else:
        animateText("⚠️  𝗔𝗰𝗰𝗼𝘂𝗻𝘁 𝗰𝗿𝗲𝗮𝘁𝗶𝗼𝗻 𝗲𝗻𝗰𝗼𝘂𝗻𝘁𝗲𝗿𝗲𝗱 𝗮𝗻 𝗶𝘀𝘀𝘂𝗲", "yellow")
        return False

def askForAnother():
    print()
    animateText("🔄 𝗪𝗼𝘂𝗹𝗱 𝘆𝗼𝘂 𝗹𝗶𝗸𝗲 𝘁𝗼 𝗰𝗿𝗲𝗮𝘁𝗲 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗮𝗰𝗰𝗼𝘂𝗻𝘁? (𝘆/𝗻): ", "cyan")
    choice = input(f"{cyan}▸▸▸ {end}").lower().strip()
    return choice == 'y'

def run():
    clearScreen()
    printBanner()
    while True:
        email = getEmailInput()
        password = getPasswordInput()
        telegram_token, telegram_chat_id = getTelegramCredentials()
        animateText("🔄 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗿𝗲𝗾𝘂𝗲𝘀𝘁...", "purple")
        time.sleep(2)
        success = createAccount(email, password, telegram_token, telegram_chat_id)
        if success:
            animateText("✅ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀 𝗰𝗼𝗺𝗽𝗹𝗲𝘁𝗲𝗱 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆!", "green")
        else:
            animateText("❌ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀 𝗳𝗮𝗶𝗹𝗲𝗱. 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻.", "red")
        if not askForAnother():
            animateText("👋 𝗧𝗵𝗮𝗻𝗸 𝘆𝗼𝘂 𝗳𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝗼𝘂𝗿 𝘀𝗲𝗿𝘃𝗶𝗰𝗲!", "cyan")
            break
        clearScreen()
        printBanner()

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\n{red}❌ 𝗣𝗿𝗼𝗰𝗲𝘀𝘀 𝗶𝗻𝘁𝗲𝗿𝗿𝘂𝗽𝘁𝗲𝗱 𝗯𝘆 𝘂𝘀𝗲𝗿{end}")
    except Exception as e:
        print(f"\n{red}❌ 𝗔𝗻 𝗲𝗿𝗿𝗼𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗱: {str(e)}{end}")