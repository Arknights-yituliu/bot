#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
from datetime import datetime


now = datetime.today().strftime("%Y-%m-%d_%H-%M-%S")

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page(
        device_scale_factor=2, viewport={"width": 810, "height": 1080}
    )
    page.goto("http://localhost:8080")
    page.locator("body").screenshot(path=f"/output/{now}.png")
    browser.close()
