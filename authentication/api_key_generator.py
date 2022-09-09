
import base64
import os
import hashlib
import six
import random

# sha256 encrypt some string data

def generate_api_key():

    seed = os.urandom(256)

    # since urandom does not provide sufficient entropy hash, base64encode and salt.
    # The resulting value is now large and should be hard to predict.
    hashed_seed = hashlib.sha256(seed).hexdigest()

    base64_encoded = base64.b64encode(
        six.b(hashed_seed),
        six.b(random.choice(['rA', 'aZ', 'gQ', 'hH', 'hG', 'aR', 'DD']))).rstrip(b'==')
    base64_encoded = base64_encoded.decode()
    return base64_encoded 