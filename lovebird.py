from twilio.rest import Client 
 
account_sid = 'AC03a4b4ec11f205dfb6a16f17acf84233' 
auth_token = 'e3ad49b6bf2547caefe354e9630050f0' 
client = Client(account_sid, auth_token) 
def sendLove():
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='Automate message-python',      
                                  to='whatsapp:+601156474458' 
                              ) 
     
    print(message.sid)
