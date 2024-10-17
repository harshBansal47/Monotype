import os
from pathlib import Path


class Config:
    BROWSER = "chrome"
    BASE_URL = "https://enterprise.monotype.com/"
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    HEADLESS = False
    PROJECT_DIR = Path(__file__).resolve().parent.parent
    DOWNLOAD_DIR = PROJECT_DIR / "download"
    if not DOWNLOAD_DIR.exists():
        DOWNLOAD_DIR.mkdir(parents=True)
    