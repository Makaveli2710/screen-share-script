import vidstream
from vidstream import ScreenShareClient, StreamingServer
import threading

while True :
    print("\t\t\t\t\tWelcome to the Screen Sharing Script.\t\t\t\t\t\n")
    print("**lil hint : to quit the stream just press Q ;)**\n")
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