# Mail-Merging Project

This is a Python script for mail-merging that can help automate the process of sending personalized emails to a large number of recipients. The script takes a template email message, a list of recipient email addresses, and a CSV file containing the data to be merged into the email message. The script then generates a separate personalized email message for each recipient, and sends them via SMTP (Simple Mail Transfer Protocol) using the Gmail account of the sender.

## Features

Personalize email messages with recipient-specific data such as name, company, and job title
Load email template and recipient data from external CSV files
Send personalized emails via Gmail SMTP
Automatically handle common SMTP errors such as authentication failure and connection timeout

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
3. CLIENT_SECRET_FILE: the path to the client secret file for the Gmail API (downloaded from the Google Cloud Console)
4. API_NAME: the name of the Gmail API (usually "gmail")
5. API_VERSION: the version of the Gmail API (usually "v1")
6. TEMPLATE_FILE: the path to the email template file (a plain text file with placeholders for the recipient-specific data)
7. CSV_FILE: the path to the CSV file containing the recipient data (with column headers)
8. You also need to enable the Gmail API and grant access to your Gmail account by following the instructions in the Google Cloud Console.

## Usage

To run the script, simply run the following command:
```
python mail_merge.py
```

The script will prompt you to enter your Gmail account password (for authentication). It will then load the email template and recipient data from the external files, generate personalized email messages for each recipient, and send them via Gmail SMTP.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

This script was inspired by the mail-merge feature in Microsoft Word, and was developed for educational purposes only.
