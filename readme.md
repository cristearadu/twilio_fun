# Twilio Python Script Configuration

This repository contains a Python script that uses the Twilio API to send SMS messages. To configure the script, you need to provide your Twilio credentials and other settings in the `config.ini` file.

### Instructions:

1. **Create `config.ini` File:**
   - Copy the provided `config.ini` template.
   - Create a file named `config.ini` in the same directory as your Python script.

   ```ini
   ; config.ini

   [twilio]
   account_sid = YOUR_ACCOUNT_SID
   auth_token = YOUR_AUTH_TOKEN
   from = YOUR_TWILIO_PHONE_NUMBER

1. **Create `contacts.ini` File:**
   - Copy the provided `contacts.ini` template.
   - Create a file named `contacts.ini` in the same directory as your Python script.

   ```ini
   ; contacts.ini
   
   [contact1]
   name = Name Surname
   phone_number = +mobile_phone_number
   
   [contact2]
   name= Another Contact
   phone_number = +mobile_phone_number


