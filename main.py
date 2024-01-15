alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# importing and printing logo
from art import logo

print(logo)


def caesar(start_text, shift_amount, cipher_direction): 
  end_text = ""
  if cipher_direction == "decode":
    shift *= -1

  for char in start_text:
    if char in alphabet: 
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else: 
      end_text += char
  return end_text

end = False

while end == False:

  direction = input("Type 'encode' to encrypt and 'decode' to decrypt: \n")
  text = input("Type your message: \n")
  shift = int(input("Type the shift number: \n"))
  
  if shift > 26:
    shift = shift%26
  
  
  new_text = caesar(text, shift, direction)
  print(f"This is the end result: {new_text}")
  
  again = input("Do you want to go again? Type 'yes' for yes and 'no' for no. \n")

  if again == "no":
    end = True
    print("Goodbye")