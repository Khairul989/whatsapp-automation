from twilio.rest import Client 
 
client = Client(account_sid, auth_token) 
def sendLove():
    message = client.messages.create( 
                                  from_='whatsapp:+',  
                                  body='Assalamualaikum saya fyp, nak tanya fyp dah buat ke?',      
                                  to='whatsapp:+601156474458' 
                              ) 
     
    print(message.sid)
