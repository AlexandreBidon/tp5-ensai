import requests
import logging
import traceback
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException


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