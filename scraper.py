import requests, json, lxml
from bs4 import BeautifulSoup

#STYLE ID INPUT, seperated by _ => 4436_4679_893

def get_data(style_id):
    link = f"https://www.ae.com/us/en/p/{style_id}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        #"Cookie": "TLTUID=8F490B236BAABC2E62B70D5EE7A6BF9A; bm_sz=E725A69F21EE40BF2C35A6208011CED8~YAAQFWl8aBxXhtyLAQAAzVCT/BXbRNSWFBtIim7uADG1LtwEG9yzaItY5MN+GpFLLBbHmqeihkBFz3UQlexnMB4JmBXka4ZisEIoFn+NjqcQvMYHbKu+Qm7v9n0RJosGWkJLDik5Yk8vVj6OOasPEud+v+q8DWPnTi6RZ8OlRLNmYVqoRNte/o2RWXF/5dbIRCKRwGfS/7h5JFqYs/DEnp78H8Zt+5RTdfitw1X86movGD8FDIzWIqbiHEBauPN3JsIKcvixW1owJFtvUPBkljYZAvLNEjgGgXJrqqAhsA==~4407604~4473657; AKA_A2=A; akaalb_PROD_ALB=1700835994~op=PROD_LB_ALL_DCs:PROD_AGWA_GKE_ORIGIN|~rv=20~m=PROD_AGWA_GKE_ORIGIN:0|~os=db0ecb8ead961a2983478ea211c488b6~id=d55c7cea90d03a6cdc01939172ce8753; _cls_v=8ae754c2-3771-4d34-b638-f93e165b76d0; _cls_s=7c771c66-9b7c-4590-8fa7-7b8a8760d8d3:0; ak_bmsc=659E74BC90CA4BEE2173ABF6B3363BC0~000000000000000000000000000000~YAAQFWl8aD5XhtyLAQAA31WT/BVD3p8NYPdSss+8cRFhz8u4oeA1lm5Y1AQjWjtL1PEocfXLt+sOLo8xf20RhSwWhKlbQSMP9E/cBmydIRdAq4NXfQXFHqEJHyF3SsLC8YlzW+xhbYiEyP97UdUORN11VgVa35Gj0By2D4bJ0pWq1SUVri6In8zLpMqU20wa1UJ4NUTczT3CgluNI0bmuxhPSEN9rEQhNQom1QTrRDh2DAgOB26G091ZUAjv2wcHpDRWyvJMc+WAyjUdZ0ebiAOCHIPsmk98PSRTaHgvdLUW8oclAabG9TgWQQee4z2zAnSYgmMOWe36E/OlqODvJyai5AgByKlvdQXrM1mH5mH+T4VsOsGm1o+TpOWke+ex9S1vTYrXMiV4nkPXeJJXALMh0MY4BkfMk27bBREeN48A2wwG+/z7U7e5sZRjsBo565fvPWoGX3ITKMqNywVu+e40w/MwVBBei/6zden+3FugAHDfUL3y4ns=; brand=aeo; akaalb_PROD_ALB_API=1700751396~op=PROD_LB_API_APICG_ONLY:PROD_LB_Origin_API_01|PROD_LB_APICG_EAST5:PROD_LB_Origin_APICG_East5|~rv=27~m=PROD_LB_Origin_API_01:0|PROD_LB_Origin_APICG_East5:0|~os=db0ecb8ead961a2983478ea211c488b6~id=7909772953374df394a04ee63f106987; tkbl_cvuuid=20d5d111-c94d-4b4f-87bf-bff3f84095c3; swim_ten=e; user_profile_id=undefined; acquisition_value=; acquisition_location=https://www.ae.com/us/en; test_acquisition_value=; test_acquisition_location=https://www.ae.com/us/en; ConstructorioID_client_id=d3d42a91-0a23-4cbc-a39c-b400777f2a32; ConstructorioID_session_id=1; _scid=60600db5-3b7d-49a5-84e9-caf8e85fc89a; cjConsent=MHxOfDB8Tnww; cjUser=98560b0b-7d62-4b75-8eac-787be1102c3a; cjLiveRampLastCall=2023-11-23T14:26:37.140Z; _gcl_au=1.1.396904599.1700749597; _ga=GA1.1.284834346.1700749597; _tt_enable_cookie=1; _ttp=GCtKQ4HthhpuC_3b4y9PXVC7j32; _pin_unauth=dWlkPU5EZzRaR0l4TVRBdE56Um1aaTAwTlRaaUxUZzJNR0l0WkRGbE5XWTNaalptWldVeg; __exponea_etc__=8ba053e9-4d98-4e0d-849f-a8715145beaf; __exponea_time2__=-0.20386075973510742; _sctr=1%7C1700715600000; __idcontext=eyJjb29raWVJRCI6IjIxTGtNZWQ1MXNVSGx2YUtOQkZRcXlRMDU5NyIsImRldmljZUlEIjoiMjFMa01oZHpyVm4yeHhxZ2tLU0FlRWQ2UWQ5IiwiaXYiOiIiLCJ2IjoiIn0%3D; OptanonAlertBoxClosed=2023-11-23T14:26:40.315Z; BVBRANDID=f1a19fbf-dcce-4c13-ba15-f9819944c06a; BVBRANDSID=9c7a6667-33c9-4a70-8cef-d7e7f25f49cd; ae_i18n=en|US|USD|US|us; ae_lang=en; ConstructorioID_session={\"sessionId\":1,\"lastTime\":1700749995819}; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Nov+23+2023+09%3A33%3A16+GMT-0500+(Eastern+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0007%3A1&geolocation=US%3BRI&AwaitingReconsent=false; _scid_r=60600db5-3b7d-49a5-84e9-caf8e85fc89a; _abck=D9D2B43C56B5355959DFEE147F27EE8F~-1~YAAQFWl8aDuahtyLAQAAFsCd/ArpNYVGxN4fMT45ERmm0oM4eKgRVmVxWR6XPQv3ddMVbx0gopkzNijwgiQsDkcqwAlkTmDPR6wOXlGfUQJY1Uh2eeZeWb9opu/y7CT2ixrxpiyskjulhNB1WwwfG3GvOPSpID/iOzBtY5k5Cd19AMZZLkJoGAqh22a8OhVT7+3dgHgkMPxQnGpYUknLJsz8l5lYEvxVh/jCHcXfRi3DOEraQz1j8rL1K4/Bg37Wf0cuf39eoejoTaVyauCJ6CdqnOSr0TJopE1sPDikos61eNg5ftIy4q30Vm3ANBtbjhNwY8jTA+4wBhFVTNelkbfoRoof49WJTwt/muE6/jGQ23sJZViCzLdyOI0NTvSp9Ix8HPiUF8wOqveIq8a0q7lvgpoTPt3CvVIGnApgR7ng/i62HpPC2wE51WUvbSQ=~-1~-1~-1; _ga_XGBGNYD4S1=GS1.1.1700749597.1.1.1700750278.0.0.0; utag_main=v_id:018bfc9358aa001c7e960d4d65de05075001806d00942$_sn:1$_se:35$_ss:0$_st:1700752078782$ses_id:1700749596843%3Bexp-session$_pn:2%3Bexp-session$_prevpage:AE%3Awomen%3Abottoms%3Ajeans%3Acurvy_jeans%3Acurvy_baggy_jeans%3Aae_curvy_super_high_waisted_baggy_wide_leg_cargo_jean%3Apdp%3Bexp-1700753878784$dc_visit:1$dc_event:35%3Bexp-session$dc_region:us-east-1%3Bexp-session; bm_sv=EADA2FA75C898EB33408AD86A6DCC3A5~YAAQFWl8aEW/htyLAQAAWkSk/BUW+D8nI6kBEQcxhrP4wPfbH10Wj1BdCezZDQGFd8Vx56FN1eUmVWsRhe21h6T/GMRlJ1amjXMvSol1iN+0MqTByMgoPVHhnzpm20Ds+PinDzIxvtUdHqnuX24To8jz3wwUoGc6tUImjc2Oile5tPEi8l2VquIZc/rfVdzvSnz0jt5iVZI75JkBVQU384mNUAnjK0q65R0Bj/Yy34e+Xmr9kYRm1O5xAubz~1; RT=\"z=1&dm=ae.com&si=de5dcd34-0b09-41f5-8028-c3503a04c92b&ss=lpbae9xd&sl=2&tt=16x&rl=1&nu=1l8xf6in&cl=enf1&obo=1&ld=nv3t&r=n4tgk3i4&ul=nv3u\"",
        "Dnt": "1",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    r = requests.get(link, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, "lxml")
        data = soup.findAll("script", {"type": "fastboot/shoebox"})[3].text
        data = json.loads(data)
        return data
    
def find_sizes(data):
    sizes = []
    sizeList = data['data']['contentItem']['contents'][0]['productDetailContent'][0]['records'][0]['records']
    for i in sizeList:
        item = {
            'size':str(i['attributes']['sku_sizeDesc'][0]),
            'stock':int(str(i['attributes']['P_Online_02953_DC_STATUS_AEO_US'][0])),
        }
        sizes.append(item)
    return sizes



def main(style_id):
    data = get_data(style_id)
    sizes = find_sizes(data)
    return sizes


