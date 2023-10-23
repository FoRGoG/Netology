import requests

url = 'https://akabab.github.io/superhero-api/api'
resp = requests.get(url + '/all.json')
full_file = resp.json()
heroes_list = ['Hulk', 'Captain America', 'Thanos']
new_dict = dict()
for item in full_file:
    if item['name'] in heroes_list:
        new_dict[item['name']] = item['powerstats']['intelligence']
print('The smartest hero is', max(new_dict, key=new_dict.get))
