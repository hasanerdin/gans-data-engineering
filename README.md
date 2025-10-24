# 🛴 Gans Data Engineering Project

## 💼 Case Study: Gans — E-Scooter Data Pipeline

Welcome to the **Gans Data Engineering Project**, a case study designed to simulate a real-world data engineering challenge.  
**Gans** is a growing e-scooter sharing startup aiming to optimize scooter distribution in major cities worldwide.  

This repository contains the complete **ETL (Extract, Transform, Load)** pipeline for collecting, cleaning, and storing data from multiple external sources — such as APIs and web scraping — and automating the process through **Google Cloud Functions**.

---

## 🚀 Project Overview

The project’s main goal is to help **Gans** anticipate scooter movements and optimize placement across different cities.  
To do that, we collect and merge data from multiple external sources that influence scooter usage, such as:

- 🌦 **Weather conditions** (via OpenWeather API)  
- 🛫 **Airport and flight activity** (influence of tourist arrivals)  
- 🏙 **City demographics** (population, density, etc.)  

All of this data is processed using **Python** and **pandas**, and stored in a **MySQL database hosted on Google Cloud**.

---

## 🧩 Architecture
```text
+-------------------+
|  External Sources |
|-------------------|
| Wikipedia (cities)|
| OpenWeather API   |
| Flight APIs       |
+--------+----------+
         |
         v
+-------------------+
|  Data Collection  |
| (requests, BS4)   |
+--------+----------+
         |
         v
+-------------------+
|   Data Cleaning   |
| (pandas, utils)   |
+--------+----------+
         |
         v
+-------------------+
|  Cloud Storage    |
|  (MySQL on GCP)   |
+--------+----------+
         |
         v
+-------------------+
|  Automation Layer |
| (Cloud Functions) |
+-------------------+
```
---

## 🌍 Why the Cloud?

Migrating the database to the **cloud** allows:

- 🌍 Global accessibility — everyone in the company can access the data securely.  
- ⚙️ Automation — data collection and updates can be scheduled via **Cloud Scheduler**.  
- 📈 Scalability — the system grows as data volume increases.  
- 🔐 Security — managed authentication and storage.  

While debugging Cloud Functions directly can be difficult, we developed and tested each function **locally first** using **Flask** to simulate API requests before deploying to Google Cloud.

---

## 🧰 Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| Language | Python 3 |
| Data Extraction | `requests`, `BeautifulSoup`, `OpenWeather API` |
| Data Processing | `pandas`, `json` |
| Database | `MySQL (Google Cloud SQL)` |
| Cloud & Automation | `Google Cloud Functions`, `Cloud Scheduler` |
| Local Debugging | `Flask` |
| Utilities | Custom helper scripts (`utils.py`) |

---

## 🗂️ Repository Structure
```
📁 Gans-Data-Engineering
│
├── cities.py          # Extracts city-level data (name, country, etc.)
├── airport.py         # Collects airport-related data
├── weather.py         # Fetches weather forecasts via OpenWeather API
├── flight.py          # Retrieves flight data for selected cities
├── population.py      # Gets population and demographic data
├── request.py         # Manages and validates API requests
├── utils.py           # Helper functions for cleaning and transforming data
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```
---

## ⚙️ Setup & Installation

### 1️⃣ Clone this repository
```bash
git clone https://github.com/hasanerdin/gans-data-engineering.git
cd gans-data-engineering
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set up your environment variables
Go to utils.py and write your informations.
```bash
RAPID_API_KEY = "your_api_key"
WEATHER_API_KEY = "your_api_key"
schema = "your_db_schema_name"
host = "your_gcp_ip_address"
password = "your_gcp_password"
```

### 4️⃣ Run locally
```python
python cities.py
python population.py
python airport.py
python request.py
```

### 5️⃣ Deploy to Google Cloud
Make sure your main.py contains a properly defined entry point:
@functions_framework.http
def main(request):
    # your ETL logic here
    return 'Data successfully added.'

---

## 🧩 Key Learnings
- The difference between web scraping and API-based data collection
- How to build a structured ETL pipeline
- Using Python and pandas to interact with a MySQL Cloud database
- Deploying and automating scripts with Google Cloud Functions
- Debugging best practices using Flask before deployment
- Understanding that there are always multiple ways to achieve a task — and choosing the most efficient and reliable one

