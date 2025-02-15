#!/usr/bin/env python3

import asyncio
from get_props import making_data_json
from if_no_numbers import if_no_numbers
from obtener_numero_selenium import obtener_numero_selenium

async def main():
    await making_data_json()
    # json con los datos de cada propiedad (url, user_id): "url_user.json"
    # si tiene número asociado al user_id, no obtener número: "user_id_num.json"
    await if_no_numbers()

asyncio.run(main())
