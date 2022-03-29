from tp5.webservice import APISetup
import uvicorn
import logging


def main():
    """
    Runs the web service
    """
    web_service = APISetup()
    uvicorn.run(web_service.app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    logging.basicConfig(filename='info.log', level=logging.INFO)
    logging.info('API start')
    main()
    logging.info('API shutdown')
