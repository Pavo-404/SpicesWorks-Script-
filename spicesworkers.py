from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver (Edge example)
driver = webdriver.Chrome()  # Or webdriver.Firefox() for Firefox
driver.get('https://on.spiceworks.com/tickets/open/1?sort=updated_at-desc')  # Replace with actual URL

# Function to check and refresh tickets
def check_and_refresh_tickets():
    try:
        # Find all elements using the specified XPath for "Accept" button
        open_ticket_elements = driver.find_elements(By.XPATH, '//*[@id="firstPanelDivticketsResizablePanels"]/div/div/table/tbody/tr/td[4]')

        if open_ticket_elements:
            for index, ticket in enumerate(open_ticket_elements):
                # Verify if the text within the element is "Accept"
                if ticket.text.strip() == 'Accept':
                    # Accept the ticket
                    ActionChains(driver).move_to_element(ticket).click().perform()
                    print(f"Accepted ticket {index + 1}")
                    
                    # Wait briefly to allow UI updates before continuing
                    time.sleep(2)
                    
                    # Restart the check after accepting a ticket
                    return
        else:
            # Find the refresh button if no open tickets are found
            refresh_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="refresh tickets"]')
            if refresh_button:
                refresh_button.click()
                print('No open tickets found. Refreshing...')
    except Exception as e:
        print(f"Error occurred: {e}")


# Run the check every 5 seconds
print('Ticket monitoring script started...')
while True:
    check_and_refresh_tickets()
    time.sleep(5)  # Check every 5 seconds
