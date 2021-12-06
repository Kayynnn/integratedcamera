import firebase_admin
from firebase_admin import credentials

cd = credentials.Certificate("ya.json")

# In the above line <path_to_generated_private_key>
# is a placeholder for the generate JSON file containing
# your private key.

firebase_admin.initialize_app(cd)

