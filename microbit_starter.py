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
# Sound settings
short_tone = 800
long_tone = 600

while True:
    # Task 4: Shake to scroll/show the full message
    if accelerometer.was_gesture('shake'):
        if message:
            # Join list into string and scroll
            display.scroll("".join(message))
            # Optional: Clear message after showing
            # message = [] 
        else:
            display.show(Image.NO) # Show X if message is empty
        sleep(500)
        display.clear()

    # Task 2: Decode current_symbol when logo is touched
    elif pin_logo.is_touched():
        if current_symbol in morse_dict:
            letter = morse_dict[current_symbol]
            message.append(letter)
            display.show(letter) # Display the decoded letter
            music.pitch(1000, 200) # Sound for successful decoding
            sleep(500)
        else:
            display.show(Image.NO) # Invalid code
            music.pitch(200, 300) # Low sound for error
            sleep(500)
        current_symbol = '' # Reset for next letter
        display.clear()

    # Task 1 & 3: Record dots and dashes (Button A=dot, B=dash)
    elif button_a.was_pressed():
        current_symbol += '.'
        display.show('.')
        music.pitch(short_tone, 100) # Short sound
        sleep(100)
        display.clear()

    elif button_b.was_pressed():
        current_symbol += '-'
        display.show('-')
        music.pitch(short_tone, 300) # Long sound
        sleep(100)
        display.clear()

    # Visual feedback: Dim center dot to show building
    if current_symbol:
        display.set_pixel(2, 2, 5) 
    else:
        display.clear()