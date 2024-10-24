import requests

# Define the API URL
url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=all&country=all&ssl=all&anonymity=all"

def get_proxies():
    try:
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the proxy list as text
            proxy_list = response.text
            
            # Remove empty lines
            proxy_list = "\n".join([line for line in proxy_list.splitlines() if line.strip()])
            
            # Save the proxies to a file
            with open('proxies.txt', 'w') as file:
                file.write(proxy_list)
            print("Proxies saved to proxies.txt")
        else:
            print(f"Failed to retrieve proxies. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
get_proxies()
