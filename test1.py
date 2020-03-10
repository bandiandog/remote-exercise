# -*- coding: utf-8 -*-

import requests
import json
import xmltodict

"""
amount（） src - currency（）dest - currency（）reference - date（）the output of 2 parameters
amount（） currency（）
"""
def currency_exchange(amount=100, currency='USD', dest_currency='JPY', reference_date='2020-03-03'):
    content = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml', timeout=30).content
    ceDict = {}
    for d in xmltodict.parse(content)["gesmes:Envelope"]["Cube"]["Cube"]:
        ceDict[d['@time']] = dict([(dd["@currency"], dd["@rate"]) for dd in d['Cube']])

    a = ceDict.get(reference_date, {}).get(currency.upper())
    b = ceDict.get(reference_date, {}).get(dest_currency.upper())
    if a and b:
        amount2 = round(amount * float(a) / float(b), 4)
        print(u"dest-amount: %s, dest-currency: %s, rate: %s -> %s" % (amount2, dest_currency, a, b))
        return amount2, dest_currency
    else:
        print(u"wrong parameter\n%s" % json.dumps(ceDict, indent=4, ensure_ascii=False))

currency_exchange(dest_currency='bgn')