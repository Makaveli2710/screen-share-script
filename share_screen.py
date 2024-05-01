import vidstream
from vidstream import ScreenShareClient, StreamingServer
import threading

while True :
    print('''
            SCREEN SHARING SCRIPT
          -------------------------
            PRIVATE. SAFE. QUIET.
        ''')
    print("**lil hint : to quit the stream just press Q ;)**\n")
    print('''
          If you want to use the script and share your screen, choose the first choice and enter the receiver's IP Adress, and port.
          If you want to use the script and receive a screen, choose the second one and enter the sender's IP Adress, and the port.
          PS : you must be on the same port, so if you don't know it just enter 9999 !  
        ''' )
    print("1- Share screen.")
    print("2- Receive a screen.")
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        sender_ip = input("Enter your ip: ")
        sender_port = int(input("Enter your port: "))
        
        sender = ScreenShareClient(sender_ip, sender_port)
        t=threading.Thread(target=sender.start_stream)
        
        t.start()
        
        while input != 'quit':
            continue
        sender.stop_stream()
        
    if choice == 2:
        receiver_ip = input("Enter your ip: ")
        receiver_port = int(input("Enter your port: "))
        
        receiver = StreamingServer(receiver_ip, receiver_port)
        
        t_r = threading.Thread(target=receiver.start_server)
        
        t_r.start()
        
        while input != 'quit':
            continue
        receiver.stop_server()
        
    else :
        print("Wrong choice pal ! :)")
        break
