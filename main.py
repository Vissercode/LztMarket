import time
import market
import config



def Main():
    cfg = config.load()
    token = cfg['market_token']
    urls = cfg['url']
    delay = cfg['delay']
    print(f'Актуальный баланс: {market.UserInfo(token)} у.е.')
    for url in urls:
        accounts = market.GetAccounts(token,url)
        for account in accounts:
            try:
                print(f'''====НАЙДЕНО ОБЪЯВЛЕНИЕ====\nНазвание объявления:{account['item_title']}\nСсылка на объявление:{account['item_url']}\nЦена: {account['item_price']} у.е.\nИгры:{account['item_games']}\nССЫЛКА ДЛЯ БЫСТРОЙ ПОКУПКИ: {account['item_fast_buy']}\n''')
            except:
                    print(f'''====НАЙДЕНО ОБЪЯВЛЕНИЕ====\n
                    Название объявления:{account['item_title']}\n
                    Ссылка на объявление:{account['item_url']}\n
                    Цена: {account['item_price']} у.е.\n
                    ССЫЛКА ДЛЯ БЫСТРОЙ ПОКУПКИ:{account['item_fast_buy']}\n=======''')
        time.sleep(int(delay))
    
Main()