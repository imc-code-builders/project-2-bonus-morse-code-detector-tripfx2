from microbit import *
import music

# Dictionary to map Morse sequences to characters
morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '-----': '0'
}

current_symbol = ''
message = []

while True:
    # Task 4: Shake to scroll/show the full message
    if accelerometer.was_gesture('shake'):
        if message:
            display.scroll("".join(message))
        else:
            display.show(Image.NO) # Show X if message is empty
        sleep(500)

    # Task 2: Decode current_symbol when logo is touched
    if pin_logo.is_touched():
        if current_symbol in morse_dict:
            letter = morse_dict[current_symbol]
            message.append(letter)
            display.show(letter) # Display the decoded letter
            music.pitch(600, 200) # Sound for decoding
            sleep(500)
        else:
            display.show(Image.NO) # Invalid code
            sleep(500)
        current_symbol = '' # Reset for next letter

    # Task 1 & 3: Record dots and dashes (Button A=dot, B=dash) & Sound/Display
    elif button_a.was_pressed():
        current_symbol += '.'
        display.show('.')
        music.pitch(800, 100) # Short sound for dot
        sleep(100)
        display.clear()

    elif button_b.was_pressed():
        current_symbol += '-'
        display.show('-')
        music.pitch(800, 300) # Long sound for dash
        sleep(100)
        display.clear()
        
    # Optional: Display current partial symbol (visual feedback)
    # This helps see what you are building
    if current_symbol and not display.get_pixel(2,2):
        display.set_pixel(2,2, 5) # Dim center dot to show building