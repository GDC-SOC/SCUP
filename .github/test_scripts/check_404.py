import requests
import pytest

# List of URLs to check
urls_to_test = [
    "https://gdc.smce.nasa.gov/",           # No 404
    "https://gdc.smce.nasa.gov/ballistickittens/",  # this should return a 404
]

# Checks for 404 error
def check_for_404(url):
    response = requests.get(url)
    
    # Check if the HTTP status code is exactly 404
    if response.status_code == 404:
        # Now check if the page content contains a 404 error message
        if "404" not in response.text and "not found" not in response.text.lower():
            raise AssertionError(f"Expected 404 error message in the content of {url}, but none found.")
    else:
        print(f"{url} did not return 404 (status code: {response.status_code})")

@pytest.mark.parametrize("url", urls_to_test)
def test_check_for_404(url):
    check_for_404(url)