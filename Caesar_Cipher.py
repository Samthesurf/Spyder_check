from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Don't change the code above 👆


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(cipher_direction, plaintext, shift_amount):
    text = ""
    for char in plaintext:
        letter_in_list = True
        if char not in alphabet:
            text += char
            letter_in_list = False
        else:
            letter_in_list  # The goal here was too use my mistake from when I was prime checking, I saw Angela's answer and was frustrated
            # but this exercise of accounting for spaces and symbols helped me realize and recall my mistakes to solve it.
            position = alphabet.index(char)
            # in case the number is too large
            actual_shift = shift_amount % len(alphabet)
            if direction == 'encode' and letter_in_list:
                new_position = position + actual_shift
                # if the position is more than the elements in the alphabet list
                if new_position > (len(alphabet)-1):
                    new_position -= len(alphabet)
            elif direction == 'decode' and letter_in_list:
                new_position = position - actual_shift
                if new_position < 0:
                    new_position += len(alphabet)
            new_letter = alphabet[new_position]

            text += new_letter
    print(f"The {direction}d text is {text}")
choice = True
while choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plaintext=text, shift_amount=shift, cipher_direction=direction)
    result = input( 'Type "yes" if you want to continue playing, "no" to stop.\n')
    if result == "no":
        choice = False
        print('Goodbye')
    



