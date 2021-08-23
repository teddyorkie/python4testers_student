# IBAN Validator
def validator_IBAN(iban):
  iban = iban.replace(' ', '')
  if not iban.isalnum():
    print("You have entered invalid characters.")
    return False
  elif len(iban) < 15:
    print("IBAN entered is too short.")
    return False
  elif len(iban) > 31:
    print("IBAN entered is too long.")
    return False
  else:
    iban = (iban[4:] + iban[0:4]).upper()

  iban2 = ''
  for ch in iban:
    if ch.isdigit():
      iban2 += ch
    else:
      iban2 += str(10 + ord(ch) - ord('A'))

  if int(iban2) % 97 == 1:
    return True
  else:
    return False
