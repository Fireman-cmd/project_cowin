import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_cowin.settings')
django.setup()

from base_app.models import District

#make API calls to all the states and save data from them for the session in vaccines.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

for i in range(1,37):
    url = f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/{i}' #this will have all the districts with district_code and name
    response = requests.get(url=url,headers= headers)
    # print(response.status_code)
    dis = response.json()
    dis = dis["districts"]

    for d in dis:
        new_district = District(name=d['district_name'],district_id=d['district_id'])
        new_district.save()
    