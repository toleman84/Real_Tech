#!/usr/bin/env python3

import asyncio
from get_props import making_data_json
from obtener_numero_selenium import obtener_numero_selenium

async def main():
    await making_data_json()
    # json con los datos de cada propiedad (url, user_id)
    # si el json tiene número asociado al user_id, no obtener número
    await obtener_numero_selenium()

asyncio.run(main())
