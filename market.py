
import requests
import json

def UserInfo(token):
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}"
    }
    response = requests.get('https://api.lzt.market/me', headers=headers).json()
    balance = response['user']['balance']
    return balance

def GetAccounts(token,url):
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers).json()
    items = response['items']
    data_items = []
    item_games = []
    for item in items:
        if str(url).find('steam') != None:
            item_bought_games = item['account_full_games']['list']
            titles = [game_info['title'] for game_info in item_bought_games.values()]
                
            item_dict = {
                'item_title' : item['title'],
                'item_url' : f'lolz.market/{item['item_id']}',
                'item_fast_buy' : f'https://api.lzt.market/{item['item_id']}/fast-buy',
                'item_price' : item['price'],
                'item_games' : titles
                }
        else:
            item_dict = {
                'item_title' : item['title'],
                'item_url' : f'lolz.market/{item['item_id']}',
                'item_fast_buy' : f'https://api.lzt.market/{item['item_id']}/fast-buy',
                'item_price' : item['price'],
                }
        data_items.append(item_dict)
    return(data_items)


        
