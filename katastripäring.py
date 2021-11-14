import requests
kataster = '41201:004:0066'

r = requests.get('https://geoportaal.maaamet.ee/url/xgis-ky.php?ky='+kataster+'&out=json')
r = r.json()
print(r['Pindala'])