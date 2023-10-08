import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtGui import QPalette, QColor, QIcon
from PyQt5.QtCore import Qt

import requests
from bs4 import BeautifulSoup
import re

import webbrowser




class ColorChangeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('malicious.png'))
        # set the title
       
        self.setWindowTitle('SAFECLICK: Secure Analysis for Filtering, Evaluation, and Click Safety')
        self.setGeometry(100, 100, 800, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('Enter URL...')
        self.layout.addWidget(self.url_input)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.process_url)
        self.layout.addWidget(self.submit_button)

    def process_url(self):
        url = self.url_input.text()
        if self.is_valid_url(url):  # You can replace this with your URL processing logic
            self.set_app_color('green')
        else:
            self.set_app_color('red')

    def is_valid_url(self, url):
        # Define the URL of the YouTube video page
        if (not("https://" in url)):
            return 1
        video_url = url
        
        # Define the keyword to search for (case-insensitive)
        keyword = 'rick'

        # Send an HTTP GET request to the video URL
        response = requests.get(video_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content of the page
            page_content = response.text

            # Search for the keyword in the entire page content (case-insensitive)
            if re.search(re.compile(re.escape(keyword), re.IGNORECASE), page_content):
                return 0
            else:
                webbrowser.open(url)
                return 1
                


        else:
            return 1



        return 1

    def set_app_color(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
