
###!!@mocleW EPGTQ!!!6789
def decode_message(encoded):
    # Step 1: Extract the core part of the message
    core_part = encoded.split('@')[-1].split('!')[0].strip()
    
    # Step 2: Reverse the first word
    first_word, second_word = core_part.split()
    first_word_reversed = first_word[::-1]  # Reverse the first word
    
    # Step 3: Process the second word (no vowels to change in "EPGTQ")
    # No changes needed as there are no vowels
    second_word_processed = second_word
    
    # Step 4: Final decoded message
    decoded_message = f"{first_word_reversed} {second_word_processed}"
    return decoded_message

# Example usage
encoded_message = "###!!@mocleW EPGTQ!!!6789"
decoded = decode_message(encoded_message)
print(decoded)

