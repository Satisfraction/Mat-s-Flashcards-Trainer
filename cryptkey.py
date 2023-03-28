from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save key to a file
with open('key.txt', 'wb') as f:
    f.write(key)