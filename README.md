# 📸 Instagram Unfollowers Checker
A modern Flask-based web application that analyzes Instagram export files and identifies users who don't follow you back.
The application processes Instagram's exported HTML files locally, ensuring privacy while providing fast and accurate follower analysis.

## ✨ Features
* Upload Instagram Followers and Following HTML files
* Identify users who do not follow you back
* Modern analytics dashboard
* Alphabetically sorted results
* Search usernames instantly
* Open Instagram profiles directly
* Export results as TXT
* Export results as CSV
* File validation and error handling
* Automatic cleanup of temporary files
* Responsive modern user interface

## 🛠 Tech Stack
### Backend
* Python
* Flask
* BeautifulSoup4

### Frontend
* HTML5
* CSS3
* JavaScript

### Data Processing
* Set Operations
* File Handling
* HTML Parsing

## 📂 Project Structure

Instagram-Unfollowers-Checker/
│
├── app.py
├── instagram_parser.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/

## 🚀 Installation

### Clone Repository
git clone https://github.com/omkara24/Instagram-Unfollowers-Checker.git

### Move Into Project Directory
cd Instagram-Unfollowers-Checker

### Install Dependencies
pip install -r requirements.txt
### Run Application
python app.py

### Open Browser
http://127.0.0.1:5000

## 📖 How To Use
### Step 1
Download your Instagram account data.

### Step 2

Locate the exported files:
* Followers HTML file
* Following HTML file

### Step 3
Open the application.

### Step 4
Upload both files.

### Step 5
Click:
Analyze Account

### Step 6
View:
* Total Followers
* Total Following
* Users Who Don't Follow You Back

### Step 7
Export results as:
* TXT
* CSV

## 🔒 Privacy
All processing happens locally on your machine.
Uploaded files are automatically removed after analysis.
Temporary export files are automatically deleted after download.
No user data is stored permanently.

## 📊 Core Logic
The application uses Python sets for efficient comparison.
non_followers = following - followers
This approach provides fast and scalable performance even for large Instagram accounts.

## 🎯 Future Improvements
* Mutual Followers Analysis
* Followers You Don't Follow Back
* Dark/Light Theme Toggle
* Drag & Drop Upload Support
* Profile Statistics Dashboard
* Deployment Support

## 📜 License
This project is available for educational and personal use.