import socket

class PortScanner:
    
    def __init__(self,target,start_port,end_port):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        
    def scan(self):
        print(f"[*] Starting scan on {self.target} from port {self.start_port} to {self.end_port}")
    
        for port in range(self.start_port, self.end_port + 1):
            self.scan_port(port)

    
    def scan_port(self,port):
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            
            sock.settimeout(2)
            
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                print(f"[+] Port {port} is open")
                
            sock.close()
        except Exception as errL:
            print(f"[!] Error scanning port {port}: {errL}")
        
            
    

