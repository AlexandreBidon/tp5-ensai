import requests
import logging
import traceback
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

class SearchEndpoint():
    """
    SearchEndpoint
    ---
    Endpoint
    This class defines the methods used for the search and config endpoints
    """

    def __init__(self):
        pass

    def search_id(self, query):
        try:
            requete = requests.get(
                "https://world.openfoodfacts.org/api/v0/product/{query}.json".format(query=query))
            logging.info(
                "Searched on : https://world.openfoodfacts.org/api/v0/product/{query}.json".format(query=query))
        except Exception as e:
            logging.error(traceback.format_exc())
            # Logs the error appropriately.
            raise HTTPException(
                status_code=444, detail='An exception occurred with a Search Source: {}'.format(e))
        return requete.json()

    def is_vegan_id(self, query):
        try:
            requete = requests.get(
                "https://world.openfoodfacts.org/api/v0/product/{query}.json".format(query=query))
            logging.info(
                "Searched on : https://world.openfoodfacts.org/api/v0/product/{query}.json".format(query=query))
        except Exception as e:
            logging.error(traceback.format_exc())
            # Logs the error appropriately.
            raise HTTPException(
                status_code=444, detail='An exception occurred with a Search Source: {}'.format(e))
        for ingredient in requete.json()["product"]["ingredients"]:
            logging.info(ingredient)
            if "vegan" in ingredient:
                if ingredient["vegan"] != "yes":
                    return False
        return True

