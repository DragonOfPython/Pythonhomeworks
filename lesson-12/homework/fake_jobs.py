import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Function to scrape job listings from the website
def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    job_listings = []
    for job in soup.find_all('div', class_='job'):
        title = job.h2.text.strip()
        company = job.h3.text.strip()
        location = job.find('p', class_='location').text.strip()
        description = job.find('p', class_='description').text.strip()
        link = job.find('a')['href']
        
        job_listings.append({'title': title, 'company': company, 'location': location, 'description': description, 'link': link})
    
    return job_listings

# Function to create the SQLite database and jobs table
def create_database():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        link TEXT,
        PRIMARY KEY(title, company, location)
    )''')
    
    conn.commit()
    conn.close()

# Function to insert job listings into the database
def insert_job_listings(job_listings):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    
    for job in job_listings:
        c.execute('INSERT OR REPLACE INTO jobs (title, company, location, description, link) VALUES (?, ?, ?, ?, ?)',
                  (job['title'], job['company'], job['location'], job['description'], job['link']))
    
    conn.commit()
    conn.close()

# Scrape job listings and insert into the database
job_listings = scrape_job_listings('https://realpython.github.io/fake-jobs')
create_database()
insert_job_listings(job_listings)

# Function to export filtered results to a CSV file
def export_to_csv(location=None, company=None):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    
    query = 'SELECT * FROM jobs'
    if location:
        query += f" WHERE location = '{location}'"
    if company:
        if 'WHERE' in query:
            query += f" AND company = '{company}'"
        else:
            query += f" WHERE company = '{company}'"
    
    c.execute(query)
    results = c.fetchall()
    
    with open('filtered_jobs.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'Company', 'Location', 'Description', 'Link'])
        csv_writer.writerows(results)
    
    conn.close()

# Export filtered results to a CSV file
export_to_csv(location='AP')
export_to_csv(company='Garcia PLC')