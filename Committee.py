import random
from CommitteeGUI import *
from cipher_funcs import *

HOST = socket.gethostname()  # Default loopback
PORT = 5000  # Port number
#Gettin al the curves types
CURVES = list(registry.EC_CURVE_REGISTRY.keys())

def server_program():
    
    #--------- Create handshake with clients ---------
    server_socket = socket.socket()  # Instance of socket
    server_socket.bind((HOST, PORT))  
    server_socket.listen(1) # Configure how many client the server can listen
    connection, address = server_socket.accept()
    print("Committee is on air!")
    print("--------------------------------------------------")
    #----------- End handshake with clients -----------

    # ------------ Key exchange - ECDE ----------------
    startKEmsg = connection.recv(1024).decode()
    if(startKEmsg != 'StartKE'):
        print('Incorrect message recived')
        exit()

    # curve_str = CURVES[0] # later random!!
    curve_str = random.choice(CURVES) # later random!!
    connection.send(curve_str.encode())  # Send Curve to the client
    
    ## get client public key
    clientPubKey = pickle.loads(connection.recv(1024))
    
    ## server keys creation
    curve = registry.get_curve(curve_str)
    serverPrivKey = secrets.randbelow(curve.field.n)
    serverPubKey = serverPrivKey * curve.g
    
    ## send public key to client
    serverPubKey_asBytes = pickle.dumps(serverPubKey)
    connection.send(serverPubKey_asBytes)  # Send message to the client
    
    ## create shared key
    sharedKey = serverPrivKey * clientPubKey
    # ----------- END key exchange - ECDE ----------------
    print("Key exchanged with polling stations system!")

    # Handle committee
    clearDB(VOTES_DB)
    initVotersToFalse()
    compressed_shared_key = compress(sharedKey)
    initKey(compressed_shared_key)
    committeeWindow(compressed_shared_key)

    # Close connection
    connection.close()
    print("--------------------------------------------------")
    print("Committee is closed!")

if __name__ == '__main__':
    server_program()