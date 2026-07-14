import requests
class ApiClient:
    def __init__(self, base_url): self.base_url=base_url.rstrip('/')
    def post(self,path,data): return requests.post(self.base_url+path,json=data,timeout=20).json()
    def get(self,path,params=None): return requests.get(self.base_url+path,params=params,timeout=20).json()
