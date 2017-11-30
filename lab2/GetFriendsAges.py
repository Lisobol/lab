import base_client
import requests
import matplotlib.pyplot as plt
import Main
from datetime import datetime
class getfr(base_client.BaseClient):
    def _get_data(self, method, http_method,):
        response = requests.get('https://api.vk.com/method/' + method, params={'user_id': Main.userid, 'fields': 'bdate', })
        return self.response_handler(response)
    def response_handler(self, response):
        try:
            count=0
            ages=[]
            for i in range(150):
                try:
                    bd = response.json()['response'][i]['bdate']
                    count += 1
                    ageindays=datetime.today()-datetime.strptime(bd, '%d.%m.%Y')
                    age= int(ageindays.days/365.25)
                    ages.append(age)
                except:
                    pass
            print('Ages: ',ages)
            print('Number of friends:',count)
            plt.hist(ages,100)
            plt.show()
        except:
            print('Something went wrong')
            exit(0)