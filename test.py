import requests
requete = requests.get(
    "https://world.openfoodfacts.org/api/v0/product/3256540001305.json")
print(requete.status_code)
print(requete.json())
