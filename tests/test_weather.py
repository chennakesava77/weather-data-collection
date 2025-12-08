from unittest.mock import patch
from weather import fetch_weather_for_city

@patch('requests.get')
def test_fetch_weather_for_city(mock_get):
    class MockResp:
        def raise_for_status(self): return None
        def json(self): 
            return {"main": {"temp": 72, "humidity": 55}, "weather": [{"description": "clear sky"}]}

    mock_get.return_value = MockResp()
    data = fetch_weather_for_city('Nowhere', 'fakekey')
    assert data['temp_f'] == 72
    assert data['humidity'] == 55
    assert 'clear' in data['conditions']
