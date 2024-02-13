import requests
import time


checking = True

def main():
    website_url = input_website_url()
    while checking:
        check_website_status(website_url)
        time.sleep(60)
        #again = input("Do you want to check another website? (y/n): ").lower()
        if not checking:
            break
    print("Goodbye!")

def check_website_status(url):

    global checking 
    try:
        response = requests.get(url)
        # Check if the status code is in the 2xx range
        if response.status_code // 100 == 2:
            print(f"The website {url} is up and running.")
        else:
            print(f"The website {url} is down. Status code: {response.status_code}")
            checking = False
    except requests.ConnectionError:
        print(f"Failed to connect to {url}. The website may be down.")
        checking = False
        

def input_website_url():
    website_url = input("Enter the website URL: https://www.")
    return ("https://www."+website_url)

if __name__ == "__main__":
    main()