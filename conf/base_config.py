import os

# For authorization on http://ok.ru
LOGIN = os.environ.get("LOGIN", "")
PASSWORD = os.environ.get("PASSWORD", "")

# Config for seismograph.ext.selenium
SELENIUM_EX = {
    "USE_REMOTE": True,
    "MAXIMIZE_WINDOW": True,
    "DEFAULT_BROWSER": os.environ.get("BROWSER", "firefox"),
    "PROJECT_URL": "https://ok.ru/",

    "REMOTE": {
        "command_executor": "http://127.0.0.1:4444/wd/hub"
    }
}
