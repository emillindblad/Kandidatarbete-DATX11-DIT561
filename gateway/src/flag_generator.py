import hashlib

def generate_flag(id1, id2):
    secret_password = "SuperSecretPassword"
    # Combine the IDs and the secret password
    combined_string = f"{id1}_{id2}_{secret_password}"

    # Hash the combined string using SHA-256
    hasher = hashlib.sha256()
    hasher.update(combined_string.encode('utf-8'))
    hashed_string = hasher.hexdigest()

    # Truncate the hashed string to get the flag length of 24 characters
    truncated_hashed_string = hashed_string[:16]  # 16 characters to account for the 'flag{}' format (24 - 8)

    # Create the flag in the required format
    flag = f"flag{{{truncated_hashed_string}}}"

    return flag

# Example usage:
# id1 = "user123"
# id2 = "user456"

# generated_flag = generate_flag(id1, id2, secret_password)
# print(generated_flag)
