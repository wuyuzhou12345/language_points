import threading
class ProjectThread(threading.Thread):
    '''test'''
    def __init__(self,project_name,test_url,uat_url,prod_url):
        self.project_name = project_name
        self.test_url = test_url
        self.uat_url = uat_url
        self.prod_url = prod_url


    def run(self):
        '''
        :return: execute
        '''
        self.test_result = self.execute_case(self.test_url)
        self.uat_result = self.execute_case(self.uat_url)
        self.pro_result = self.execute_case(self.pro_url)
        print('project_name:{}结束执行'.format(self.project_name))


    def exexute_case(self,url):
        print(url)

    def get_result(self):
        # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        return self.test_result,self.uat_result,self.pro_result

if __name__ == '__main__':
    thread_list = []
    projects = [
        {"project_name":"test_project1",
         "test_url":"http://www.baidu.com/test_project1/test_url",
         "uat_url":"http://www.baidu.com/test_project1/uat_url",
         "prod_url":"http://www.baidu.com/test_project1/prod_url"
         },
        {"project_name": "test_project2",
         "test_url": "http://www.baidu.com/test_project2/test_url",
         "uat_url": "http://www.baidu.com/test_project2/uat_url",
         "prod_url": "http://www.baidu.com/test_project2/prod_url"
         },
        {"project_name": "test_project3",
         "test_url": "http://www.baidu.com/test_project3/test_url",
         "uat_url": "http://www.baidu.com/test_project3/uat_url",
         "prod_url": "http://www.baidu.com/test_project3/prod_url"
         },
    ]
    for project in projects:
        p = ProjectThread(project['project_name'],project['test_url'],project['uat_url'],project['prod_url'])
        thread_list.append(p)
        p.start()

    for t in thread_list:
        t.join() #一定要join，不然主线程比子线程跑的快，会拿不到结果  join方法：阻塞线程直到该线程执行完毕
        for p in projects:
            if p.get('project_name') == t.project_name:
                p['test_result'] = t.test_result
                p['uat_result'] = t.uat_result
                p['prod_result'] = t.pro_result