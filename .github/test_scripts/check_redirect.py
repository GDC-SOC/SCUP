import requests

def check_http_to_https_redirection(url):
    response = requests.get(url, allow_redirects=True)
    
    if response.url.startswith("https://"):
        print(f"SUCCESS: {url} redirects to {response.url}")
    else:
        print(f"FAILURE: {url} does NOT redirect to HTTPS. Final URL: {response.url}")

# Test the NASA GDC website
check_http_to_https_redirection("http://gdc.smce.nasa.gov")