import requests
import json


# class comDeluxeDatascienceMetadatamanagerApiconsumer:
class Apiconsumer:
    _protocol = 'http'
    _host = 'localhost'
    _port = 8089
    API_KEY = ''

    def _getUrl(self):
        '''
        Returns the full API URL
        :return: string
        '''
        return "{0}://{1}:{2}".format(self._protocol, self._host, self._port)

    def authenticate(self, username='', password=''):
        '''
        Sets the API token in the self.API_KEY
        :param username: Username
        :param password: Password
        :return: boolean
        '''
        r = requests.post(url=self._getUrl() + '/api/Users/login', data={'username': username, 'password': password})
        rr = r.json()
        try:
            self.API_KEY = rr['id']
            return True
        except:
            return False

    def getOrigins(self):
        '''
        Returns the list of origins
        :param query:
        :return:
        '''
        r = requests.get(url=self._getUrl() +
                             '/api/origins',
                         headers={'Content-Type': 'application/json', 'Authorization': self.API_KEY})
        try:
            return r.json()
        except:
            return False

    def getDatabases(self, origins_idh=''):
        '''
        Returns the list of origins
        :param query:
        :return:
        '''
        q = json.dumps({"where": {"origins_idh": origins_idh}})
        r = requests.get(url=self._getUrl() +
                             '/api/databases/',
                         params={"filter": q},
                         headers={'Content-Type': 'application/json', 'Authorization': self.API_KEY})
        try:
            return r.json()
        except:
            return False

    def getSchemas(self, databases_idh=''):
        '''
        Returns the list of origins
        :param query:
        :return:
        '''
        q = json.dumps({"where": {"databases_idh": databases_idh}})
        r = requests.get(url=self._getUrl() +
                             '/api/schemas/',
                         params={"filter": q},
                         headers={'Content-Type': 'application/json', 'Authorization': self.API_KEY})
        try:
            return r.json()
        except:
            return False

    def getTables(self, schemas_idh=''):
        '''
        Returns the list of tables
        :param query:
        :return:
        '''
        q = json.dumps({"where": {"schemas_idh": schemas_idh}})
        r = requests.get(url=self._getUrl() +
                             '/api/tables/',
                         params={"filter": q},
                         headers={'Content-Type': 'application/json', 'Authorization': self.API_KEY})
        try:
            return r.json()
        except:
            return False

    def getFields(self, tables_idh=''):
        '''
        Returns the list of fields
        :param query:
        :return:
        '''
        q = json.dumps({"where": {"tables_idh": tables_idh}})
        r = requests.get(url=self._getUrl() +
                             '/api/fields/',
                         params={"filter": q},
                         headers={'Content-Type': 'application/json', 'Authorization': self.API_KEY})
        try:
            return r.json()
        except:
            return False
