import smtplib as sm
from email.message import EmailMessage as em

def email_structure(subject, body, to):
    msg = em()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "electricitytracker@gmail.com"

    user = "electricitytracker@gmail.com"
    password = "kqkz wrwj ygdb utwp"  # Consider using an app password

    try:
        server = sm.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent to {to}")  # Log success
        return "Email sent successfully."  # Return success message
    except sm.SMTPException as e:
        print(f"SMTP Error: {e}")  # Print SMTP-related errors
        return f"SMTP Error: {e}"  # Return SMTP error message
    except Exception as e:
        print(f"Error: {e}")  # Print other errors
        return f"Error: {e}"  # Return general error message
