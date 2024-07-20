import time
import pickle
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from groq import Groq


def insta_login():
    # driver = webdriver.Chrome(service=chrome_service(ChromeDriverManager().install()))
    driver = uc.Chrome()
    try:
        driver.get("https://www.instagram.com")
        cookie = pickle.load(open("cookie.pkl", "rb"))

        for cookies in cookie:

            cookies["domain"] = ".instagram.com"
            try:
                driver.add_cookie(cookies)
            except Exception as e:
                print(e)
        driver.get("https://www.instagram.com")
        print("logged in using cookie")
    except Exception as e:
        driver.get("https://www.instagram.com/")

        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

        email_input.send_keys("samplegmail.com")
        time.sleep(3)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("Password")
        time.sleep(3)

        login_btn = driver.find_element(By.CSS_SELECTOR, "button._acan[type='submit']")
        login_btn.click()
        print("logging in manaully")
        time.sleep(8)
        # try:
        #     notnow_btn = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        #     if notnow_btn:
        #         notnow_btn.click()
        # except:
        #     print("helo")

        cookie = driver.get_cookies()
        pickle.dump(cookie, open("cookie.pkl", "wb"))
    try:
        notnow_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        if notnow_btn:
            notnow_btn.click()
    except:
        print("there is no not now button pop up")
    return driver


def accept_request(bot):
    bot.get("https://www.instagram.com/direct/requests/")
    try:
        notnow_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        if notnow_btn:
            notnow_btn.click()
    except:
        print("there is no not now button pop up")
    time.sleep(6)
    requests = WebDriverWait(bot, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.xwib8y2[role="button"]')))
    requests.pop()

    if requests != []:
        requests[0].click()
        accept_btn = WebDriverWait(bot, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="Accept"]')))
        accept_btn.click()
        print("message requests accepted")
        accept_request(bot)


def accept_frnd_request(bot):
    bot.get("https://www.instagram.com/notifications")

    try:
        time.sleep(5)
        accept_request_btn = bot.find_element(By.CSS_SELECTOR, 'div.xzloghq')
        accept_request_btn.click()
        accept_frnd_request(bot)
    except Exception as e:
        print("all friend requests have been accepted")


def reply_to_messages(bot):
    bot.refresh()
    bot.get("https://www.instagram.com/direct/inbox")
    print("Currently looking for messages to reply")
    time.sleep(6)
    try:
        notnow_btn = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        if notnow_btn:
            notnow_btn.click()
    except:
        print("there is no not now button pop up")
    try:
        unread_messages = bot.find_element(By.CSS_SELECTOR, ".x1emribx")
        unread_messages.click()

        texts = WebDriverWait(bot, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.xyk4ms5, .x18lvrbx')))

        # texts.reverse()
        chat = ""
        for text in texts:
            class_list = (text.get_attribute("class")).split(" ")
            if "xyk4ms5" in class_list:
                chat += f"You:{text.text}\n"
            else:
                chat += f"Guy:{text.text}\n"
        print("chat has been retrived")
        print(chat)
        client = Groq(api_key="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")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a casual girl using instagram and never tell that you are an AI,don't act like an AI and give reply to this converstation simply in simple sentence not like (girl:)"
                },
                {
                    "role": "user",
                    "content": chat,
                }
            ],
            model="llama3-8b-8192",
        )
        print("reply has been generated")
        ai_reply = chat_completion.choices[0].message.content
        input_box = bot.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        input_box.send_keys(ai_reply, Keys.ENTER)
        time.sleep(5)
        reply_to_messages(bot)
    except Exception as e:
        print(e)
        print("no unread messages")



