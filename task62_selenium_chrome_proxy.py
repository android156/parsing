import time
import random
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

# Define a list of proxies
proxies = [
    'https://NDcGhG:poCK2h@185.89.41.214:8000',
    'https://xCV1m5:SR8Mcp@5.101.33.153:8000',
    # Add more proxies here
]

# Maximum retries
max_retries = len(proxies)

# URL to visit
url = 'https://2ip.ru/'


# Function to create browser with proxy and user agent
def create_browser(proxy):
    # Generate a random user agent
    ua = UserAgent()
    user_agent = ua.random
    print(f"Using User-Agent: {user_agent}")

    # Configure Selenium options
    selenium_options = webdriver.ChromeOptions()
    selenium_options.add_argument(f'user-agent={user_agent}')

    selenium_wire_options = {
        'proxy': {
            'https': proxy,
        },
        'connection_timeout': 30,
        'http2': False,  # Force HTTP/1.1
    }

    return webdriver.Chrome(options=selenium_options, seleniumwire_options=selenium_wire_options)


# Retry logic
for attempt in range(max_retries):
    if not proxies:  # Check if proxies are exhausted
        print("All proxies failed.")
        break

    try:
        # Select a random proxy for the first attempt or remaining proxies
        proxy = random.choice(proxies)
        print(f"Using proxy: {proxy}")

        # Create a browser instance with the selected proxy and user agent
        with create_browser(proxy) as browser:
            browser.get(url)

            # Wait for the element to be present
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'd_clip_button'))
            )

            # Extract the text
            span_text = element.find_element(By.TAG_NAME, 'span').text
            print(f"Extracted Text: {span_text}")
            time.sleep(5)

            # If successful, break the loop
            break

    except Exception as e:
        print(f"Attempt {attempt + 1} failed with proxy {proxy}: {e}")

        # Remove the failed proxy from the list to avoid reusing it
        if proxy in proxies:
            proxies.remove(proxy)
