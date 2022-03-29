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
        self.__search_engine = SearchEngine()
