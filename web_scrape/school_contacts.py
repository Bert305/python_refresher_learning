from bs4 import BeautifulSoup
import requests
import csv

url = 'https://facultyaffairs.miami.edu/resources/school-college-contacts/department-chairs/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all rows in the table
rows = soup.find_all('tr')

# Prepare CSV file
with open('department_chairs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Department', 'Chair Name', 'Email'])  # CSV headers

    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 3:
            department = cells[0].get_text(strip=True)
            chair_name = cells[1].get_text(strip=True)
            email = cells[2].get_text(strip=True)
            writer.writerow([department, chair_name, email])
            print(department, chair_name, email)
            
            
            
            
# The above code scrapes the department chair information from the University of Miami's website and saves it to a CSV file.

# want to output the data into a CSV file
# The CSV file will have three columns: Department, Chair Name, and Email.





    