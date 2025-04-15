import pytest
from bat_functions import *
import time

#Exercise 1: Basic Tests and Parametrization

def test_calculate_bat_power():
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(1) == 42
    assert calculate_bat_power(10) == 420
    assert calculate_bat_power(100) == 4200

@pytest.mark.parametrize("distance, expected", [
    (0, 100),
    (5, 50),
    (10, 0),
    (12, 0)
])

def test_signal_strength(distance, expected):
    assert signal_strength(distance) == expected

#Exercise 2: Using Fixtures

@pytest.fixture
def bat_vehicles():
    return ["Batmobile", "Batwing", "Batcycle"]

def test_get_bat_vehicle_known(bat_vehicles):
    batmobile = get_bat_vehicle("Batmobile")
    assert batmobile == {"speed": 200, "armor": 80}

    batwing = get_bat_vehicle("Batwing")
    assert batwing == {"speed": 300, "armor": 60}

    batcycle = get_bat_vehicle("Batcycle")
    assert batcycle == {"speed": 150, "armor": 50}

def test_get_bat_vehicle_unknown():
    with pytest.raises(ValueError) as info:
        get_bat_vehicle("Batboat")
    assert "Unknown vehicle: Batboat" in str(info.value)

#Exercise 3: Mocking External Dependencies

def test_fetch_joker_info(mocker):
    mock_sleep = mocker.patch("time.sleep")

    mock_return = {"mischief_level": 100, "location": "unknown"}
    mocker.patch('bat_functions.fetch_joker_info', return_value = mock_return)
    
    result = fetch_joker_info()

    assert result == mock_return
    mock_sleep.assert_called_once_with(1)