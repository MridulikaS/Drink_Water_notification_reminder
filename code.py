import time
from plyer import notification

if __name__ == "__main__":
    while True:

        notification.notify(
            title = "Please drink water NOW!!",
            message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
            app_icon = "E:\icon.ico",
            timeout = 10


        )
        time.sleep(60*60)
