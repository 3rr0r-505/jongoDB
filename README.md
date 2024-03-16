<p align="center"><a href="https://github.com/3rr0r-505/jongoDB"><img alt="" src="https://github.com/3rr0r-505/jongoDB/blob/main/jongoDB.png?raw=true" width="100%" height="80%"/></a></p>
<p align="center"> 
<a href="https://www.python.org/"><img alt="" src="https://img.shields.io/badge/python-3.9%2B-brighten?logo=python&label=pyhton&color=blue"/></a>
&nbsp;
<a href="https://www.gnu.org/gnu/linux-and-gnu.en.html"><img alt="" src="https://img.shields.io/badge/OS-GNU%2FLINUX-brighten?logo=linux&label=OS&labelColor=grey&color=red"/></a>
&nbsp;
<a href="https://www.microsoft.com/en-us/windows?r=1"><img alt="" src="https://img.shields.io/badge/OS-Windows-brighten?logo=windows&label=OS&labelColor=grey&color=blue"/></a><br>
</p>

# jongoDB
jongoDB is a Python tool for performing NoSQL injection attacks on MongoDB servers running on localhost. This tool is designed to fetch data from all collections of all databases hosted on a MongoDB server and send the data to a specified recipient email address.

## Features
- **NoSQL Injection Attack**: jongoDB allows you to execute NoSQL injection attacks on MongoDB servers running locally.
- **Data Extraction**: Fetches data from all collections of all databases on the MongoDB server.
- **Email Notification**: Sends the extracted data as JSON files via email to a specified recipient.
- **Customizable**: You can customize MongoDB connection settings, email sender and recipient addresses, SMTP server settings, etc.
- **JSON Encoding**: Utilizes custom JSON encoding to handle MongoDB-specific data types such as ObjectId, Binary, and datetime.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/3rr0r-505/jongoDB.git

2. Navigate to the project directory:
   ```bash
   cd jongoDB

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt


## Usage
Before using jongoDB, ensure that you have MongoDB running on localhost. You may need to customize the MongoDB connection settings in the script if your MongoDB server is hosted differently.
### CLI Mode:
- To execute jongoDB, simply run the script:
  ```bash
  python jongoDB.py

### GUI Mode:
- To execute jongoDB as an application, double-click on the ```jongo-py.bat``` file.


By default, jongoDB will attempt to fetch data from all collections of all databases on the localhost MongoDB server. Make sure to review and understand the script before running it in any environment.

## Configuration
You can customize the behavior of jongoDB by modifying the configuration parameters in the script. These parameters include:
- MongoDB connection settings
- Email sender and recipient addresses
- SMTP server settings for sending emails
Make sure to configure these parameters according to your requirements before running the script.

## Disclaimer
This tool is provided for educational and research purposes only. Misuse of this tool may be illegal and unethical. The authors assume no liability and are not responsible for any misuse or damage caused by this tool.

