# src/core/exchange_service.py

import requests
from typing import Union 

# URL da AwesomeAPI
EXCHANGE_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

def get_usd_to_brl_exchange_rate() -> Union[float, None]:
    """
    Busca a taxa de câmbio de USD para BRL na API externa.
    Retorna a taxa de compra (bid) como float ou None em caso de falha.
    """
    try:
        # É crucial definir um timeout para boas práticas e testes
        response = requests.get(EXCHANGE_URL, timeout=5)
        response.raise_for_status() # Levanta HTTPError para 4xx/5xx

        data = response.json()
        
        # A cotação de compra (bid) está em data['USDBRL']['bid']
        bid_price = data['USDBRL']['bid']
        
        return float(bid_price)

    except requests.exceptions.RequestException as e:
        # Este é o cenário de erro que você deve testar com Mocking no Passo 4
        print(f"Erro ao buscar a cotação: {e}")
        return None


def calculate_conversion(amount: float) -> Union[float, None]:
    """
    Calcula a conversão do valor em USD para BRL usando a taxa atual.
    """
    rate = get_usd_to_brl_exchange_rate()
    if rate is None:
        return None
    
    return amount * rate