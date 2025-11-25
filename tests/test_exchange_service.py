# tests/test_exchange_service.py

import unittest.mock as mock
import requests
from src.core.exchange_service import get_usd_to_brl_exchange_rate, calculate_conversion, EXCHANGE_URL 

# Mock da Resposta da AwesomeAPI com a taxa 5.1550
MOCK_RESPONSE_DATA = {
    "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "bid": "5.1550", 
    }
}

# --- Testes para get_usd_to_brl_exchange_rate (Mocking da Requisição Externa) ---

@mock.patch('src.core.exchange_service.requests.get')
def test_get_exchange_rate_success(mock_get: mock.Mock):
    """Testa se a cotação é extraída corretamente de uma resposta HTTP 200 simulada."""
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = MOCK_RESPONSE_DATA
    mock_response.raise_for_status.return_value = None 
    mock_get.return_value = mock_response 
    
    rate = get_usd_to_brl_exchange_rate()
    
    # Verifica se a chamada foi feita para o URL correto
    mock_get.assert_called_once_with(EXCHANGE_URL, timeout=5)
    assert rate == 5.1550
    assert isinstance(rate, float)


@mock.patch('src.core.exchange_service.requests.get')
def test_get_exchange_rate_network_failure(mock_get: mock.Mock):
    """Testa se a função lida corretamente com falhas de rede (exceptions)."""
    # Simula um erro de conexão (o cenário que deve ser coberto)
    mock_get.side_effect = requests.exceptions.RequestException("Simulated Network Error")
    
    rate = get_usd_to_brl_exchange_rate()
    
    assert rate is None

# --- Testes para calculate_conversion (Mocking da Função Interna) ---

@mock.patch('src.core.exchange_service.get_usd_to_brl_exchange_rate')
def test_calculate_conversion_success(mock_get_rate: mock.Mock):
    """Testa o cálculo usando uma taxa de câmbio mockada."""
    # Simula que a taxa de câmbio foi obtida com sucesso
    mock_get_rate.return_value = 5.1550
    amount = 100.00
    expected_result = 515.50
    
    result = calculate_conversion(amount)
    
    assert result == expected_result
    mock_get_rate.assert_called_once()


@mock.patch('src.core.exchange_service.get_usd_to_brl_exchange_rate')
def test_calculate_conversion_rate_failure(mock_get_rate: mock.Mock):
    """Testa se retorna None quando a função de buscar a taxa falha (cobertura de erro)."""
    # Simula que a taxa de câmbio não pôde ser obtida (retornou None)
    mock_get_rate.return_value = None
    
    result = calculate_conversion(50.00)
    
    assert result is None
    mock_get_rate.assert_called_once()