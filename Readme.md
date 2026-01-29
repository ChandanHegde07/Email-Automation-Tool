# Email Automation Tool 

## Overview

The **Email Automation Tool** is a Python-based solution for automating the process of sending customized bulk emails. It reads recipient data from a CSV file and sends personalized emails using Gmail's SMTP server.

This tool is ideal for automating outreach, reminders, notifications, and other communication tasks for businesses, event organizers, or teams.

## Features

* **Bulk Email Sending**: Send emails to multiple recipients listed in a CSV file.
* **Personalized Messages**: Use Python string formatting to personalize emails with recipient names.
* **Simple Configuration**: Easy-to-modify configuration variables in the main script.
* **Scheduling Support**: Built-in support for scheduling emails using the `schedule` library (optional).
* **Error Handling**: Graceful error handling with informative console output.

## Technologies Used

- **Python 3.x**
- **smtplib** (built-in SMTP library)
- **email.mime** (built-in email composition)
- **pandas** (for reading CSV data)
- **schedule** (for optional email scheduling)

## Project Structure

```
.
├── send_email.py      # Main script for sending emails
├── contacts.csv       # CSV file containing recipient names and emails
├── message.txt        # Email body template with placeholder support
├── .gitignore         # Git ignore rules
└── Readme.md          # This documentation file
```

## Setup and Installation

### Prerequisites

- Python 3.x installed on your system
- A Gmail account with App Password enabled (required for security)

### Installation Steps

1. **Clone the repository** to your local machine:
   ```bash
   git clone <repository-url>
   cd "Email Automation Tool"
   ```

2. **Install the required dependencies**:
   ```bash
   pip install pandas schedule
   ```

3. **Configure your email settings** in [`send_email.py`](send_email.py:9):
   - Open `send_email.py` and update the following variables:
     ```python
     SENDER_EMAIL = "youremail@gmail.com"
     PASSWORD = "your_app_password"   # Use App Password from Google Account
     SUBJECT = "Your Email Subject"
     ```

4. **Prepare your contacts list** in [`contacts.csv`](contacts.csv:1):
   - The CSV file should have two columns: `Name` and `Email`
   - Example:
     ```csv
     Name,Email
     Alice,alice@example.com
     Bob,bob@example.com
     ```

5. **Customize your message** in [`message.txt`](message.txt:1):
   - Edit the message content
   - Use `{name}` placeholder to include the recipient's name
   - Example:
     ```
     Hello {name},

     This is a personalized message for you.

     Best regards,
     Your Team
     ```

## Usage

### Basic Usage

Run the script to send emails to all contacts:

```bash
python send_email.py
```

The script will:
1. Read all contacts from `contacts.csv`
2. Send a personalized email to each recipient
3. Print success/failure messages to the console

### Scheduling Emails (Optional)

The script includes commented-out code for scheduling. To enable scheduled sending:

1. Uncomment the scheduling code in [`send_email.py`](send_email.py:46):
   ```python
   schedule.every().day.at("09:00").do(send_bulk_emails)

   while True:
       schedule.run_pending()
       time.sleep(60)
   ```

2. Run the script - it will wait and send emails at the scheduled time

## Configuration Reference

### Environment Variables (Recommended for Security)

Instead of hardcoding credentials, consider using environment variables:

```python
import os

SENDER_EMAIL = os.environ.get("EMAIL_USER")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
```

Then set them before running:
```bash
export EMAIL_USER="youremail@gmail.com"
export EMAIL_PASSWORD="your_app_password"
python send_email.py
```

### Gmail App Password Setup

1. Go to your Google Account settings
2. Navigate to Security → 2-Step Verification → App passwords
3. Generate a new app password for "Mail"
4. Use this password in the `PASSWORD` variable (not your regular Gmail password)

## API Documentation

### Functions

#### `send_email(name, receiver_email)`

Sends a single email to a recipient.

**Parameters:**
- `name` (str): Recipient's name for personalization
- `receiver_email` (str): Recipient's email address

**Returns:**
- None

**Side Effects:**
- Sends an email via Gmail SMTP
- Prints success or error message to console

#### `send_bulk_emails()`

Reads the contacts CSV and sends emails to all recipients.

**Parameters:**
- None

**Returns:**
- None

**Side Effects:**
- Calls `send_email()` for each contact in `contacts.csv`

## Important Notes

**Security Warning**: Never commit your actual email credentials to version control. Use environment variables or a separate configuration file that is listed in `.gitignore`.

**Gmail Limitations**: Gmail has sending limits (typically 100-150 emails per day for regular accounts). For larger volumes, consider using a service like SendGrid or AWS SES.

**App Password Required**: Regular Gmail passwords won't work. You must use an App Password when 2-Step Verification is enabled.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Authentication error | Ensure you're using an App Password, not your regular Gmail password |
| "Less secure app access" error | Enable 2-Step Verification and use App Passwords |
| CSV not found | Ensure `contacts.csv` is in the same directory as the script |
| Emails not sending | Check your internet connection and Gmail SMTP settings |

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source. Feel free to use and modify as needed.

## Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy Emailing!**
