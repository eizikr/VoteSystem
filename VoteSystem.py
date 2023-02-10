from cipher_funcs import *
from Voter_GUI import voterGUI
from DB_Functions import initKey

HOST = socket.gethostname()  # Default loopback
PORT = 5000  # Port number

def client_program():
    #--------- Create handshake with server ---------
    client_socket = socket.socket()  # Instanse of socket
    client_socket.connect((HOST, PORT))  # Connect to the server
    #----------- End handshake with server -----------

    # ------------ Key exchange - ECDE ----------------
    client_socket.send('StartKE'.encode())  # Send message
    curve_str = client_socket.recv(1024).decode()  # Get data from server
   
    ## client keys creation
    curve = registry.get_curve(curve_str)
    clientPrivKey = secrets.randbelow(curve.field.n)
    clientPubKey = clientPrivKey * curve.g 
   
    ## send public key to server
    clientPubKey_asBytes = pickle.dumps(clientPubKey)
    client_socket.send(clientPubKey_asBytes)  # Send message
   
    ## get server pub key and create a shared key
    serverPubKey = pickle.loads(client_socket.recv(1024))
    sharedKey = clientPrivKey * serverPubKey
    # ----------- END key exchange - ECDE ----------------
    initKey(compress(sharedKey))

    voterGUI()

    client_socket.close()  # Close connection

if __name__ == '__main__':
    client_program()