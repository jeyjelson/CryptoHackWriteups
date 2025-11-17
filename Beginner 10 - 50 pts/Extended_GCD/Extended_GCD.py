import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

data = jwt.decode(token, options={"verify_signature": False})
print(data)

# provided by cryptohack
#Padilla, J., 2022. PyJWT documentation [online]. Available at: https://pyjwt.readthedocs.io/en/stable/
#[Accessed 31 October 2025].