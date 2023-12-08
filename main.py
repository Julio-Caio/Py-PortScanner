#!usr/bin/env python3

from nmap import PortScanner

class ScannerException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Scanner:
    def __init__(self, host: str, param: str, port: str):
        self.host = host
        self.param = param
        self.port = port


    def chooseParam(self):
        dict_param = {
            1: '-sS',
            2: '-sT',
            3: '-sU',
            4: '-sV',
            5: '-sO',
            6: '-A',
            7: '-Pn',
            8: '-sL',
            9: '-sP'
        }
        if self.param in dict_param.keys():
            return dict_param[self.param]
        else:
            raise ScannerException("Invalid param")

    def scan_port(self, target, param, port, output_file_path):
        nm_scan = PortScanner()
        nm_scan.scan(target, port, param)

        with open(output_file_path, 'w') as output_file:
            for host in nm_scan.all_hosts():
                if 'tcp' in nm_scan[host] and port in nm_scan[host]['tcp']:
                    if nm_scan[host]['tcp'][port]['state'] == 'open':
                        output_file.write(f"Host: {host} | Port {port}: Open\n")
# ===================================================================================================

def menu():
    print(f'''
================================
    Choose an option of param:
    (1) -sS: TCP SYN scan
    (2) -sT: TCP connect scan
    (3) -sU: UDP scan
    (4) -sV: Version scan
    (5) -sO: OS detection
    (6) -A: Aggressive scan
    (7) -Pn: No ping
    (8) -sL: List scan
    (9) -sP: Ping scan
================================
    ''')
if __name__ == "__main__":
    # vlan_range = input("Type of range of IP's: ")
    vlan_range = "192.168.0.0/24"

    port = input("Type of port:\n[If you want to scan all ports, press enter]\n")

    if port == '':
        port = '-p 1-65535'
    
    param = input("Type of param: ")
    scanPortRange = Scanner(vlan_range, param, port)
    scanPortRange.scan_port(vlan_range, param, port, './output/a.txt')