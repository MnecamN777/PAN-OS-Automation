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
                         'Zdravo, \n \n' 
                        'Adresa je blokirana. \n \n' )
    mailItem.To = 'nemanja.milojkovic@pulsec.com; milos.todorovic@pulsec.com'
    mailItem.CC = 'nemanja.vasilic@pulsec.com'
    #mailItem.To = 'network@pulsec.com; socanalysts@pul-soc.com'
    #mailItem.CC = 'sanja.rakic@pulsec.com; nebojsa.jovovic@pul-soc.com'
    #mailItem._oleobj_.Invoke(*(64209, 0, 8, 0, outlookNS.Accounts.Item('nemanja.milojkovic@pulsec.com')))
    logging.info(f"Mail sent to SOC at {datetime.now()}")

    mailItem.Display()
    #mailItem.Save()
    #mailItem.Send()
    #sending_email()