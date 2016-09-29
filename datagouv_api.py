from urllib.request import urlopen
import json

class GetData:

    def __init__(self, ID):
        self.url = ''.join(['http://www.data.gouv.fr/api/1/datasets/', ID, '/full/'])
        self.dataset_url = None
        self.dataset = None

        self.get_dataset_url()
        self.get_dataset()


    def get_dataset_url(self):
        response = urlopen(self.url)
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        self.dataset_url = json_obj['community_resources'][0]['url']


    def get_dataset(self):
        response = urlopen(self.dataset_url)
        string = response.read().decode('utf-8')

        self.dataset = json.loads(string)




def main():
    print(GetData('53699934a3a729239d2051a1').dataset_url)
    print(GetData('53699934a3a729239d2051a1').dataset)

if __name__ == '__main__':
    main()