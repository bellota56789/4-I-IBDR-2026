from cryptography.fernet import Fernet
import base64

class Constants:
    host = "Z0FBQUFBQnBsaE9oeG9DbnVIb2Q1cnFyemwxWnp3N0tkM1kyRnpQRTNQV1VSYjY3VlV2RkxBbmRLVUE4OHNKV1FwYy1MMS1YYWJoTGg3V1IyM2pzQ0FMVm9WUnE4blhRY2phbFhzTW5hWXBrVmlNVHZ2VzNVWmg0S3A0YjhxWGdiMWtaMzg4X2o2LW4="
    port = "Z0FBQUFBQnBsaFB6amhWbmRfdWZodUFuTTNYcWFySzJlWmdiUWxjNkFsWWZrR1N4Q2R2TmNRejNSNkVpbmxqRnZPN3dvTHlSVEFjRlFNVjNpUXpPVHRDaTZjemgwUmRaeXc9PQ=="
    database = "Z0FBQUFBQnBsaE5ZWk41MVNhYzl0ZTVKeVJYRkRMak81TlAzWnluMWFINjBJMmxuSHJxSm1wUnZRYjVFa1FpdEVsQ1J1Yy1mTHdqZTRESE5rNEZrTjlfRGRfRXJlYXVtTmc9PQ=="
    user = "Z0FBQUFBQnBsaFFNVXNBTjc0c0FxbFlxOW1Pdkc0TGhBdWxvR09OeFFabnNKcXN1VHkweVQ0QjhRTmUzd21JQmpYYjhQdDVhYWN2bnIyRURINzVKQ1NMcGRMMkhOaUgya2c9PQ=="
    password  = "Z0FBQUFBQnBsaFFsZWE3WXVMaHVyMFplZDVLdzJISHFQUWI5enU3YlBUSWZzSy1aZm9tcDNYWF9vUU44Z2NFejBXOE5VQ1F3NDFVU2ctZFFDRm9QNGZ2eFRUT29fNU5oLU9DbDRKUkVZei1hVzhIVGJRbGxfOWs9"
    

    def generate_and_save_key(self, key_filename="secret.key"):
        """Generates a key and saves it to a file."""
        key = Fernet.generate_key()
        with open(key_filename, "wb") as key_file:
            key_file.write(key)
        print(f"New key generated and saved to {key_filename}")

    def load_key(self, key_filename="secret.key"):
        """Loads the key from the current directory's file."""
        return open(key_filename, "rb").read()
    
    
    def encrypt(self, string):
        # You only need to run this once to create the key file
        #self.generate_and_save_key() 
        # Load the key from the file
        key = self.load_key()
        f = Fernet(key)
        # Strings must be encoded to bytes before encryption
        encoded_string = string.encode()
        # Encrypt the bytes
        encrypted_bytes = f.encrypt(encoded_string)
        # The result is bytes, often stored or transmitted as a base64 encoded string
        return base64.urlsafe_b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, string):
        key = self.load_key()
        f = Fernet(key)
        encoded_string = string.encode()
        decrypted_bytes = f.decrypt(base64.urlsafe_b64decode(encoded_string).decode('utf-8'))
        return decrypted_bytes.decode()
    
    
"""
const = Constants()
print(f"Original: {const.decrypt(Constants.user)}")
print(f"Encrypted : {const.encrypt(const.decrypt(Constants.user))}")
"""
