import subprocess, shlex
class Scan:
    def __init__(self, tipo):
        self.scanner = tipo
    def scan(self, ip, puertos='0-65535'):
        caracteresmalos = ";&$<>{}[]'`"
        for i in ip:
            if i in caracteresmalos:
                print "Bad IP"
                return
        for i in puertos:
            if i in caracteresmalos:
                print "Bad Ports"
                return
        self.ip=ip
        self.puertos=puertos
        if self.scanner=="Nmap":
            p = self.__scanNmap()
            return p
    def __scanNmap(self):
        if self.puertos=="default":
            comando = 'nmap -sV {0}'.format(self.ip)
            p = subprocess.check_output(shlex.split(comando))
            return p
        else:
            comando = 'nmap -sV -p {0} {1}'.format(self.puertos, self.ip)
            p = subprocess.check_output(shlex.split(comando))
            return p