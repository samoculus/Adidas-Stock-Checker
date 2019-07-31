import json
import requests

print('Adidas Stock Checker$$\nBy S')
print('--------------------------------')

def data():
    condition = True
    while condition == True:
        region = input('Enter your region (US/UK/CA): ')
        pid = input('Enter PID: ')
        region = region.strip().upper()
        pid = pid.strip().upper()

        if region == ('US'):
            link = ('https://www.adidas.com/api/products/{}/availability?sitePath=US'.format(pid))
            condition = False

        elif region == ('UK'):
            link = ('https://www.adidas.co.uk/api/products/{}/availability'.format(pid))
            condition = False

        elif region == ('CA'):
            link = ('https://www.adidas.ca/api/products/{}/availability?sitePath=en'.format(pid))
            condition = False

        else:
            choice = input('Bad input. Press Q exit or any key to try again...$$ ')
            choice = choice.strip().upper()
            if choice == 'Q':
                exit()

    return link, pid

def getStock():
    link, pid = data()
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    page = requests.get(link, headers=headers)
    try:
        page_data = json.loads((page.text))['variation_list']
    except:
        print('Stock not loaded. Here\'s the data found...')
        print(json.loads((page.text)))
        exit()
    
    print('''
###################
|                 |                               
|  PID {}     |
|                 |
###################'''.format(pid))

    for x in range(len(page_data)):
        size = (page_data[x]['size'])
        stock_status = (page_data[x]['availability_status'])
        stock = (page_data[x]['availability'])
        print('Size: [{}] Status: [{}] Stock: [{}]'.format(size, stock_status, stock))

getStock()