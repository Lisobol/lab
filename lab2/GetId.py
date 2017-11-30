import base_client
import requests
import Main
class getid(base_client.BaseClient):
    def _get_data(self, method, http_method,):
        response = requests.get('https://api.vk.com/method/' + method, params={'user_ids': Main.id , 'fields': 'bdate', })
        return self.response_handler(response)
    def response_handler(self, response):
        try:
            userid = response.json()['response'][0]['uid']
            print('ID: ',userid)
            return userid
        except:
            print('Wrong ID!')
            exit(0)
        return response