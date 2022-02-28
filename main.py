
import requests
import json



def search():
    while True:
        letter = input("\ntype: ")
        if not letter.strip():
            print("Not null")
            continue

        data_json = {"letter": letter.upper()}
        headers = {'Content-type': 'application/json'}
        url = 'http://localhost:3200/search'
        response = requests.post(url, json=data_json, headers=headers)
        res_str = response.text
        print(f"\nreturn {res_str}")



if __name__=="__main__":
    try:
        search()
    except (EOFError, KeyboardInterrupt):
        print('\nSystem exit')
