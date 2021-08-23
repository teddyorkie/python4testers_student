def encrypt_message(text):
  cipher = ''
  for char in text:
    if not char.isalpha():
      continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
      code = ord('A')
    cipher += chr(code)
  return cipher

def decrypt_message(cipher):
  text = ''
  for char in cipher:
    if not char.isalpha():
      continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
      code = ord('Z')
    text += chr(code)
  return text