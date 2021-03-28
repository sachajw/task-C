import pytest
import sys
import requests

def test_get_locations_for_us_90210_check_content_type_equals_json():
    expected_response='[14, 17, 23, 27, 37, 66, 95]'
    response = requests.get("http://localhost:5000")
    print (response.content)
    assert response.content.decode('utf-8') == expected_response
