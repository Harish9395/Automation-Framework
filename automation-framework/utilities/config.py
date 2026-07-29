import os

def load_environment():

    app_url = os.getenv("APP_URL")

    print("Loaded APP_URL:", app_url)

    if not app_url:
        raise Exception("APP_URL environment variable is missing")

    return app_url
