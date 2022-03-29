from fastapi import FastAPI
from tp5.webservice.endpoints.search_endpoint import SearchEndpoint


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()
        self.searchendpoint = SearchEndpoint()

        @self.app.get("/")
        async def root():
            return {"message": "Hello World"}

        @self.app.get("/search_id={query}")
        async def search_str(query: str):
            return (self.searchendpoint.search_id(query))

        @self.app.get("/is_vegan_id={query}")
        async def is_vegan_str(query: str):
            return (self.searchendpoint.is_vegan_id(query))
