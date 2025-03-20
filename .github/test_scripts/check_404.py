import requests

# List of URLs to check
urls_to_test = [
    "https://gdc.smce.nasa.gov/",           # No 404
    "https://gdc.smce.nasa.gov/ballistickittens/",  # this should return a 404
]

# Function to check for 404 errors
def check_for_404(url):
    try:
        response = requests.get(url)
        
        # Check if the status code is 404
        if response.status_code == 404:
            # Now check if the page content contains a 404 error message
            if "404" not in response.text and "not found" not in response.text.lower():
                print(f"Warning: Expected 404 error message in the content of {url}, but none found.")
            else:
                print(f"Success: {url} correctly returned a 404 error with appropriate message.")
        else:
            print(f"{url} did not return 404 (status code: {response.status_code})")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred when trying to access {url}: {e}")

# Check each URL
for url in urls_to_test:
    check_for_404(url)