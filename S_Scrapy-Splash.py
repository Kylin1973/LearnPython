#!/usr/bin/python
# -*- coding: utf-8 -*-
#python 2.7.10
#copyRight by kylin
import requests



class MySpider(CrawlSpider):
    
    name = 'innda'
    
    def start_requests(self):
        yield SplashRequest(url, dont_process_response=True, args={'wait': 0.5}, meta={'real_url': url})
    
    rules = (
             Rule(LinkExtractor(allow=('node_\d+\.htm',)), process_request='splash_request', follow=True),
             Rule(LinkExtractor(allow=('content_\d+\.htm',)), callback="one_parse")
             )
        
     def splash_request(self, request):
         """
         :param request: Request对象（是一个字典；怎么取值就不说了吧！！）
         :return: SplashRequest的请求
         """
         # dont_process_response=True 参数表示不更改响应对象类型（默认为：HTMLResponse；更改后为：SplashTextResponse）
         # args={'wait': 0.5} 表示传递等待参数0.5（Splash会渲染0.5s的时间）
         # meta 传递请求的当前请求的URL
         return SplashRequest(url=request.url, dont_process_response=True, args={'wait': 0.5}, meta={'real_url': request.url})

    def _requests_to_follow(self, response):
        """重写的函数哈！这个函数是Rule的一个方法
        :param response: 这货是啥看名字都知道了吧（这货也是个字典，然后你懂的ｄ(･∀･*)♪ﾟ）
        :return: 追踪的Request
        """
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        # 将Response的URL更改为我们传递下来的URL
        # 需要注意哈！ 不能直接直接改！只能通过Response.replace这个魔术方法来改！（当然你改无所谓啦！反正会用报错来报复你 (`皿´) ）并且！！！
        # 敲黑板！！！！划重点！！！！！注意了！！！ 这货只能赋给一个新的对象（你说变量也行，怎么说都行！(*ﾟ∀ﾟ)=3）
        newresponse = response.replace(url=response.meta.get('real_url'))
        for n, rule in enumerate(self._rules):
            # 我要长一点不然有人看不见------------------------------------newresponse 看见没！别忘了改！！！
            links = [lnk for lnk in rule.link_extractor.extract_links(newresponse)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                yield rule.process_request(r)

def one_parse(self, response):
    print(response.url)


