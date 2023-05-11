## QX

### Policy

if use cdn:
> https://cdn.jsdelivr.net/gh/Andy963/custom_rules@main/icon/Auto.png

```
url-latency-benchmark=自动选择, server-tag-regex=.*, check-interval=1200, tolerance=50, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Auto.png
round-robin=负载均衡, server-tag-regex=.*, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Roundrobin.png
static=Apple,direct, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Apple.png
static=BiliBili,direct, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/BiliBili.png

available=Google, server-tag-regex=.*, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon//Google.png
available=Telegram, server-tag-regex=.*, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon//Telegram.png
available=Microsoft, server-tag-regex=.*, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon//Microsoft.png
static=Media,自动选择, 负载均衡,proxy,img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/YouTube.png
static=Accelerate,自动选择, 负载均衡,proxy,img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Global.png
static=CN2GIA, HD|vmess, img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Thunder.png
static=Final,自动选择,负载均衡,proxy,direct,img-url=https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/icon/Final.png
```

### filter remote

if use cdn:
> https://cdn.jsdelivr.net/gh/Andy963/custom_rules@main/qx/Unbreak.list

```

https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Unbreak.list, tag=Fix, force-policy=direct, update-interval=172800, opt-parser=true, enabled=true

https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/WeChat.list, tag=Wechat, force-policy=direct, update-interval=172800, opt-parser=false, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Apple.list, tag=Apple, force-policy=Apple, update-interval=172800, opt-parser=true, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/BiliBili.list, tag=BiliBili, force-policy=BiliBili, update-interval=172800, opt-parser=true, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/ASN.China.list, tag=Domestic, force-policy=direct, update-interval=172800, opt-parser=true, enabled=true

https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Paypal.list, tag=PayPal, force-policy=CN2GIA, update-interval=86400, opt-parser=false, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Google.list, tag=Google, force-policy=Google, update-interval=86400, opt-parser=false, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Telegram.list, tag=Telegram, force-policy=Telegram, update-interval=86400, opt-parser=false, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Microsoft.list, tag=Microsoft, force-policy=Microsoft, update-interval=86400, opt-parser=false, enabled=true
https://gh.zhougao.win/https://raw.githubusercontent.com/Andy963/custom_rules/main/qx/DuoLingo.list, tag=DuoLingo, force-policy=proxy, update-interval=86400, opt-parser=false, enabled=true

https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Streaming.list, tag=Media, force-policy=Media, update-interval=172800, opt-parser=true, enabled=true
https://gh.zhougao.win/https://github.com/Andy963/custom_rules/blob/main/qx/Global.list, tag=Accelerate, force-policy=Accelerate, update-interval=172800, opt-parser=true, enabled=true
https://gh.zhougao.win/https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge.txt, tag=广告终结者, force-policy=reject, update-interval=172800, opt-parser=true, enabled=true

```

Ref: 
- [ddgksf2013](https://github.com/ddgksf2013/ddgksf2013)