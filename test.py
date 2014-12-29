
import socket
from stun import get_nat_type
import stun

UDP_IP = '127.0.0.1'
UDP_PORT = 5005

# sock.sendto ("PUNCH", ('',))
socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                            
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                         
#s.bind((source_ip, source_port))                                                                
nat_type, nat = get_nat_type(s, '0.0.0.0', 54320,
None, 3478)                      
external_ip = nat['ExternalIP']                                                             
external_port = nat['ExternalPort']                                                         
print nat_type,' ', external_ip,' ', external_port
s.setblocking(1)
while True:
    data, addr = s.recvfrom(1024);
    print "receviced message:" , data



