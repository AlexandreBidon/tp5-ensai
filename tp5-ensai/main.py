from fastapi import FastAPI


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/")
        async def root():
            return {"message": "Hello World"}

        @self.app.get("/search={query}")
        async def search_str(query: str):
            return {"message": query}
