# Instagram Bot

This Python script automates several tasks on Instagram, including logging in, accepting message and friend requests, and replying to messages using the Groq API.

## Prerequisites

1. Python 3.7+
2. Chrome Browser
3. ChromeDriver
4. Required Python packages:
    - `selenium`
    - `undetected-chromedriver`
    - `webdriver_manager`
    - `pickle`
    - `time`
    - `groq`

## Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-repository/instagram-bot.git
    cd instagram-bot
    ```

2. **Install Dependencies**

    ```sh
    pip install selenium undetected-chromedriver webdriver_manager groq
    ```

## Usage

1. **Configure the Script**

    - Replace `"samplegmail.com"` and `"Password"` with your Instagram login credentials.
    - Replace `"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"` with your Groq API key.

2. **Run the Script**

    ```sh
    python instagram_bot.py
    ```

## Functions

### insta_login()

Logs into Instagram using either stored cookies or manually via username and password. If cookies are available, it uses them to log in directly; otherwise, it performs a manual login and saves the cookies for future use.

### accept_request(bot)

Accepts all message requests on Instagram. It navigates to the message request page and clicks on the "Accept" button for each request.

### accept_frnd_request(bot)

Accepts all friend requests on Instagram. It navigates to the notifications page and clicks on the "Accept" button for each request.

### reply_to_messages(bot)

Replies to unread messages on Instagram using the Groq API. It fetches the unread messages, generates a reply using Groq, and sends the reply.

## Detailed Steps

1. **Login**

    The script first attempts to
