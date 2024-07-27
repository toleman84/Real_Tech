#!/usr/bin/python3

import requests
import json

"""for requests library: http://tiny.cc/x7niyz"""

def get_prop():
    print("re-Generating a new List [Real Tech]:")
    url = "https://api.mercadolibre.com/sites/MLU/search"
    params = {
        "category": "MLU1459",
        "limit": 10,
        "offset": 0,
        "children_categories": [
        {
            "id": "MLA1472",
            "name": "Departamentos"
        }],
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        """On error, prints the error code and returns an empty list."""
        print("Error: {}".format(response.status_code))
        return []

def making_json():
    propertys = get_prop()
    filtered_props = []
    if propertys:
        
        for prop in propertys:
            if prop['price'] > 50000 and prop['price'] < 100000:
                filtered_props.append({
                    "id": prop['id'],
                    "title": prop['title'],
                    "price": prop['price'],
                    "currency": prop['currency_id'],
                    "address": prop.get('address', {})
                })
                # print("id: {}".format(prop['id']))
                # print("título: {}".format(prop['title']))
                # print("precio: {} {}".format(prop['currency_id'], prop['price']))
                # print("link: {}".format(prop['permalink']))
                # print("--")
        # Guardar los resultados filtrados en un archivo JSON
        with open('filtered_properties.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_props, f, ensure_ascii=False, indent=4)
        print("json of list granted. a Real Tech software")
    else:
        print("No propertys ...")
    print("end script ...")


if __name__ == "__main__":
    making_json()
