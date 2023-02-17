import os

app_settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "files"),
    "static_url_prefix": '/files/',
}
