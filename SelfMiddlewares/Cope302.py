'''
当访问量过大，会302重定位到check.html
定义302处理行为：
1. 检查重定向Location为http://captcha.weibo.com/static/waf/check.html*
2. 直接返回request，将request加入新的队列
'''

class Cope302:
    def process_response(self,request, response, spider):
        # print(response)
        # print(response.headers.get('Location'))
        if (response.status==302) and response.headers.get('Location') and ( 'http://captcha.weibo.com/static/waf/check.html'in response.headers.get('Location').decode('utf-8')):
            print("拒绝重定向到 http://captcha.weibo.com/static/waf/check.html，队列重新加入url: ",request.url)
            retryreq=request.copy()
            retryreq.dont_filter = True
            return retryreq
        return response
