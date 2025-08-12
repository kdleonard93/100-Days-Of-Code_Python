from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time
from dataclasses import dataclass
from typing import List, Callable, Any

@dataclass
class ClassInfo:
    name: str
    day: str
    time: str
    status: str

    @property
    def display_text(self) -> str:
        return f"{self.name} on {self.day} at {self.time}"

class GymBookingBot:
    def __init__(self, email: str, password: str, url: str):
        self.account_email = email
        self.account_password = password
        self.gym_url = url
        self.driver = self._setup_driver()
        self.wait = WebDriverWait(self.driver, 5)
        self.stats = {
            'already_booked': 0,
            'new_bookings': 0,
            'waitlisted': 0,
            'verified': 0
        }
    
    def _setup_driver(self) -> webdriver.Chrome:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.gym_url)
        return driver
    
    def retry(self, func: Callable, retries: int = 7, description: str = None) -> Any:
        for i in range(retries):
            print(f"Trying {description}. Attempt: {i + 1}")
            try:
                return func()
            except TimeoutException:
                if i == retries - 1:
                    raise
                time.sleep(1)
    
    def login(self) -> None:
        login_btn = self.wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()
        
        email_input = self.wait.until(ec.presence_of_element_located((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(self.account_email)
        
        password_input = self.driver.find_element(By.ID, "password-input")
        password_input.clear()
        password_input.send_keys(self.account_password)
        
        submit_btn = self.driver.find_element(By.ID, "submit-button")
        submit_btn.click()
        
        self.wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    
    def book_class(self, booking_button) -> None:
        booking_button.click()
        self.wait.until(lambda d: booking_button.text in ["Booked", "Waitlisted"])
    
    def get_target_classes(self) -> List[ClassInfo]:
        class_cards = self.driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
        target_classes = []
        
        for card in class_cards:
            day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
            day_title = day_group.find_element(By.TAG_NAME, "h2").text
            
            if "Tue" in day_title or "Thu" in day_title:
                time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
                if "6:00 PM" in time_text:
                    class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                    button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
                    
                    target_classes.append(ClassInfo(
                        name=class_name,
                        day=day_title,
                        time=time_text,
                        status=button.text
                    ))
        
        return target_classes
    
    def process_classes(self) -> None:
        target_classes = self.get_target_classes()
        
        for class_info in target_classes:
            card = self.driver.find_element(By.XPATH, f"//h3[text()='{class_info.name}']/ancestor::div[contains(@id, 'class-card-')]")
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            
            if class_info.status == "Booked":
                print(f"✓ Already booked: {class_info.display_text}")
                self.stats['already_booked'] += 1
            elif class_info.status == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info.display_text}")
                self.stats['already_booked'] += 1
            elif class_info.status == "Book Class":
                self.retry(lambda: self.book_class(button), description=f"Booking {class_info.name}")
                print(f"✓ Successfully booked: {class_info.display_text}")
                self.stats['new_bookings'] += 1
                time.sleep(0.3)
            elif class_info.status == "Join Waitlist":
                self.retry(lambda: self.book_class(button), description=f"Waitlisting {class_info.name}")
                print(f"✓ Joined waitlist for: {class_info.display_text}")
                self.stats['waitlisted'] += 1
                time.sleep(0.3)
    
    def verify_bookings(self) -> None:
        def navigate_to_bookings():
            my_bookings_link = self.wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
            my_bookings_link.click()
            self.wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
            cards = self.driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
            if not cards:
                raise TimeoutException("No booking cards found - page may not have loaded")
            return cards
        
        print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
        all_cards = self.retry(navigate_to_bookings, description="Get my bookings")
        
        for card in all_cards:
            try:
                when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
                when_text = when_paragraph.text
                
                if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
                    class_name = card.find_element(By.TAG_NAME, "h3").text
                    print(f"  ✓ Verified: {class_name}")
                    self.stats['verified'] += 1
            except NoSuchElementException:
                pass
    
    def run(self) -> None:
        try:
            self.retry(self.login, description="login")
            self.process_classes()
            
            total_expected = sum([self.stats['already_booked'], self.stats['new_bookings'], self.stats['waitlisted']])
            print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_expected} ---")
            
            self.verify_bookings()
            
            print(f"\n--- VERIFICATION RESULT ---")
            print(f"Expected: {total_expected} bookings")
            print(f"Found: {self.stats['verified']} bookings")
            
            if total_expected == self.stats['verified']:
                print("✅ SUCCESS: All bookings verified!")
            else:
                print(f"❌ MISMATCH: Missing {total_expected - self.stats['verified']} bookings")
        
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")
        finally:
            print("\n--- PROCESSING COMPLETE ---")

if __name__ == "__main__":
    ACCOUNT_EMAIL = "angela@test.com"
    ACCOUNT_PASSWORD = "superSecretTestPassword"
    GYM_URL = "https://appbrewery.github.io/gym/"
    
    bot = GymBookingBot(ACCOUNT_EMAIL, ACCOUNT_PASSWORD, GYM_URL)
    bot.run()