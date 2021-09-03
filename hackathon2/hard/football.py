import requests
import json

def get_total_goals(team, year):
    c = 0
    for t in range(1,3):
        r = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?team{t}={team}&year={str(year)}&page=1').json()
        total = r['total_pages']
        per_page = r['per_page']

        for j in range(1, total + 1):
            r = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?team{t}={team}&year={str(year)}&page={str(j)}').json()
            try:
                for i in range(0, per_page):
                    c += int(r['data'][i][f'team{t}goals'])
            except:
                # print("Exception at: ", r)
                pass
    return c

print(get_total_goals('Barcelona', 2011))