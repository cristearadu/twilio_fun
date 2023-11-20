import sys
from typing import List, Tuple
from twilio.rest import Client
from configparser import ConfigParser


def send_sms(client: Client, to: str, from_: str, body: str) -> None:
    message = client.messages.create(body=body, to=to, from_=from_)
    print(f"Message sent to {to}. SID: {message.sid}")


def get_twilio_config() -> Tuple[str, str, str]:
    twilio_config = ConfigParser()
    twilio_config.read("config.ini")

    account_sid = twilio_config.get("twilio", "account_sid")
    auth_token = twilio_config.get("twilio", "auth_token")
    from_number = twilio_config.get("twilio", "from")

    return account_sid, auth_token, from_number


def get_contacts() -> List[dict]:
    contacts_config = ConfigParser()
    contacts_config.read('contacts.ini')

    contacts = []
    for contact_section in contacts_config.sections():
        name = contacts_config.get(contact_section, 'name').lower()
        phone_number = contacts_config.get(contact_section, 'phone_number')
        contacts.append({'name': name, 'phone_number': phone_number})

    return contacts


def get_phone_number_by_name(name: str) -> str:
    contacts_list = get_contacts()

    for contact in contacts_list:
        if contact["name"] == name:
            return contact["phone_number"]
    raise ValueError(f"Contact with name '{name}' not found in contacts.ini")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py 'contact_name' 'message'")
        sys.exit(1)

    account_sid, auth_token, from_number = get_twilio_config()

    client = Client(account_sid, auth_token)

    contact_name = sys.argv[1].lower()
    message_body = sys.argv[2]

    to_number = get_phone_number_by_name(contact_name)

    send_sms(client, to=to_number, from_=from_number, body=message_body)
