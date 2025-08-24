import requests

def get_harvest_clients(bearer_token, account_id):
    """
    Retorna a lista de clientes do Harvest em JSON
    """
    url = "https://api.harvestapp.com/v2/clients"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Harvest-Account-ID": account_id,
        "User-Agent": "PythonHarvestClient/1.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    bearer_token = input("Digite o Bearer token: ")
    account_id = input("Digite o Harvest Account ID: ")

    clientes = get_harvest_clients(bearer_token, account_id)
    if clientes:
        print(clientes)
