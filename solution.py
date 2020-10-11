from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = "MAIL FROM:ANG@anghw\r\n"
    clientSocket.send(mailFrom.encode())
    recievedata = clientSocket.recv(1024)
    recievedata = recievedata.decode()
    if recievedata[:3] != '250':
        print('250 reply not received from server.')
    else:
        print("After MAIL FROM command: "+recievedata)  
    # Fill in end
    # Send RCPT TO command and print server response.
    # Fill in start
    print("Send RCPT TO command and print server response.")
    rcptTo = "RCPT TO:veurias@anghw\r\n"
    clientSocket.send(rcptTo.encode())
    recievedata = clientSocket.recv(1024)
    recievedata = recievedata.decode()
    if recievedata[:3] != '250':
        print('250 reply not received from server.')
        return 
    else:
        print("After RCPT TO command: %s"%(recievedata))
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    #data = "DATA\r\n"
    print("Send RCPT TO command and print server response.")
    clientSocket.send('DATA\r\n'.encode())
    recievedata = clientSocket.recv(1024)
    recievedata = recievedata.decode()    
    if recievedata[:3] != '354':
        print('250 reply not received from server.')
        return 

    else:
        print("After DATA command: %s"%(recievedata))
    # Fill in end
   
    # Send message data.
    # Fill in start
    print("Send message data.")
    subject = "Subject: This Is A Test Email \r\n\r\n" 
    clientSocket.send(subject.encode())
    clientSocket.send(msg.encode())
    # Fill in end
    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recievedata = clientSocket.recv(1024) #amount of data to be sent
    print(recievedata) #print the message
    if recievedata[:3] != '250': #if the message does not print properly
        print('250 reply not received from server.') #print out
        return 

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recievedata = clientSocket.recv(1024)
    print(recievedata[:1] )
    print("After Quit command: %s"%(recievedata))
    #print(recievedata.decode())
    clientSocket.close()    
    # Fill in end
if __name__ == '__main__':
    #smtp_client(1025, '127.0.0.1')
    smtp_client(25, '127.0.0.1')
    