import requests


session = requests.Session()
response = session.get(r'http://www.jctd.net/cyjc/cyrjdkweb/cysx/rjdkweb/default.aspx?vdir=34&vdxmc=%e5%85%a8%e5%9b%bd%e5%88%9b%e4%b8%9a%e5%86%b3%e7%ad%96%e5%a4%a7%e8%b5%9b--%e4%ba%ba%e6%9c%ba%e5%af%b9%e6%8a%97%e5%ae%9e%e8%ae%ad&vrjslogin=True')


payload2 = {
    'stuid':220750227,
    'mima':12345,
    '__VIEWSTATEGENERATOR':'A3C0820E',
    '__VIEWSTATE':'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',
    'login':'登录',
    '__EVENTVALIDATION':'/wEdAAQzAciB/QDW6zkymZaSNIWsHZ4wi8ny7Ddjn7Rp4o1bKeH0Iu/9fZc467JXyMTUE04rU8x5SglfzmEU2KqYFKCXUPtFZlhnqU6SzCMo4bcRBiEMcQ00d/JzNIc16qX0s38=',

}

response2 = session.post(url="http://www.jctd.net/cyjc/cyrjdkweb/cysx/rjdkweb/default.aspx", data=payload2)

print(response2.text)