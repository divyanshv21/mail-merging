# Mail-Merging Project

This is a Python script for mail-merging that can help automate the process of sending personalized emails to a large number of recipients. The script takes a template email message, a list of recipient email addresses, and a CSV file containing the data to be merged into the email message. 

## Features

Load recipient data from external CSV files

## Installation

To run this script, you need to have Python 3 installed on your computer. You also need to install the following Python libraries:

1. pandas
2. google-auth
3. google-auth-oauthlib
4. google-auth-httplib2
5. google-api-python-client
6. You can install these libraries using pip by running the following command:

Copy code
```python
pip install pandas google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
## Configuration

Before running the script, you need to configure the following settings:

1. SENDER_EMAIL: the email address of the Gmail account that will be used to send the emails
2. SENDER_NAME: the name of the sender (optional)
6. TEMPLATE_FILE: the path to the email template file (a plain text file with placeholders for the recipient-specific data)
7. CSV_FILE: the path to the CSV file containing the recipient data (with column headers)

## Usage

To run the script, simply run the following command:
```
python mail_merge.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

This script was inspired by the mail-merge feature in Microsoft Word, and was developed for educational purposes only.
