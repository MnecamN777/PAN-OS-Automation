# ==== Sending email to SOC after blocking the reported IP address

import win32com.client as win32 
import logging
import datetime



def sending_email():
    outlookApp = win32.Dispatch('Outlook.Application')

    outlookNS = outlookApp.GetNameSpace('MAPI')

    mailItem = outlookApp.CreateItem(0)
    mailItem.Subject = 'Blokiranje IP adrese - automation'
    mailItem.BodyFormat = 1
    mailItem.Body = (
                         'Hello, \n \n' 
                        'IP address is blocked. \n \n' )
    mailItem.To = ''
    mailItem.CC = ''
    logging.info(f"Mail sent to SOC at {datetime.now()}")

    mailItem.Display()
    mailItem.Save()
    mailItem.Send()
    #sending_email()