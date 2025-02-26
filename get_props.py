#!/usr/bin/env python3

import requests
import json

"""for requests library: http://tiny.cc/x7niyz"""

def get_data_prop(category="MLU1459", prop_id="MLA1472", prop_name="Departamentos"):
    print("re-Generating a new List [Real Tech]:")
    url = "https://api.mercadolibre.com/sites/MLU/search"
    params = {
        "category": category,
        "limit": 10,
        "offset": 0,
        "user_type": "normal",
        "children_categories": [
            {
                "id": prop_id,
                "name": prop_name
            }
        ],
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        """On error, prints the error code and returns an empty list."""
        print("Error: {}".format(response.status_code))
        return []


def making_data_json():
    propertys = get_data_prop()
    filtered_props = []

    if propertys:
        for prop in propertys:
            if prop['price'] > 50000 and prop['price'] < 10000000:
                filtered_props.append({
                    "id": prop['id'],
                    "title": prop['title'],
                    "price": prop['price'],
                    "currency": prop['currency_id'],
                    "address": prop.get('address', {}),
                    # agregar usuario para luego filtrar números telefónicos del mismo
                    "user_id": prop.get('seller', {}).get('id', 'N/A'),
                    "numero": 0,
                    "link": prop.get('permalink', 'N/A')
                })
                # print("id: {}".format(prop['id']))
                # print("título: {}".format(prop['title']))
                # print("precio: {} {}".format(prop['currency_id'], prop['price']))
                # print("link: {}".format(prop['permalink']))
                # print("--")
        # Guardar los resultados filtrados en un archivo JSON
        with open('url_user_3.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_props, f, ensure_ascii=False, indent=4)
        print("json of list granted. a Real Tech software")
    else:
        print("No propertys ...")
    print("end script ...")
    return filtered_props


if __name__ == "__main__":
    making_data_json()
