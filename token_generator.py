import jwt

def generateToken(payload,key):
    # Create token
    token = jwt.encode(
        payload = payload,
        key = key,
    )
    return token

def getPayload(token):
    # Get the payload from the token
    return jwt.decode(token, options={"verify_signature": False})

def verifyToken(token, key):
    # Check if this token is legal
    payload = getPayload(token)
    IV = payload['IV']
    return generateToken(payload, IV+key) == token
   