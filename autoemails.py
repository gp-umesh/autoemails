from optparse import OptionParser
import sys
import datetime
import smtplib
import time

def send(sendto,header1):
    """
    
    """
    #sendto = [
    #    'abc@gmail.com',
    #    'xyz@gmail.com',
    #    'tuv@gmail.com']
    no = [1]
    status = "true"

    gmail_username = 'sbcjacbjabc'#replace this with your gmail username
    gmail_password = 'abcywvyuqw'#replace this with your password

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(gmail_username, gmail_password)
    ## here you can add your code or call something to get information what you want to share.
    for i in range(len(sendto)):
        header = 'To:' + sendto[i] + 'From:' + gmail_username + '\n' + header1
        print header
        msg = header + 'This is python generated email sent to you. Dont reply to this email..'
        smtpserver.sendmail(gmail_username, sendto, msg)
        print 'done!'
    smtpserver.close()

def run1(opt):
    """
    this will initiate the send function to send emails
    """
    target_emails=[]
    emails=opt.target_email.split(',')
    for x in emails:
        target_emails.append(x)
    header=opt.subject
    
        
def run():
    """It is the function that calls the entire script."""
    parser = OptionParser()
    parser.add_option("-TO", "--reciept", type="string",
                      help="pass the emails comma seperated",
                      dest="target_email",
                      default="example@gmail.com")

    parser.add_option("-heading", "--subject of email", type="string",
                      help="Passes the subject",
                      dest="subject",
                      default="test email")
                      
    (options, args) = parser.parse_args()
    run1(options)


if __name__ == "__main__":
    run()
