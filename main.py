import string
import customtkinter as ctk
from random import choice

upper = [x for x in string.ascii_uppercase]
lower = [x for x in string.ascii_lowercase]
symbol = [x for x in string.punctuation]
numbers = [x for x in string.digits]


def generate_seed() -> str:
    seed = ""
    for i in range(25):
        seed += choice(numbers)
    return seed


def gen_seed_list() -> list[int]:
    seed = input("What is your code?: ")
    output_list = []
    for i in seed:
        output_list.append(int(i))

    return output_list


def encode(text: str, code: list[int], repeat: int = 1) -> None:
    for i in range(repeat):
        encoded_message = ""
        for e, i in enumerate(text, start=0):
            seed = code[e % (len(code))]
            if i.islower():
                encoded_message += lower[(lower.index(i) + seed) % 26]
            elif i.isupper():
                encoded_message += upper[(upper.index(i) + seed) % 26]
            elif i in symbol:
                encoded_message += symbol[(symbol.index(i) + seed) % 26]
            elif i in numbers:
                encoded_message += numbers[(numbers.index(i) + seed) % 10]
            else:
                encoded_message += i
        text = encoded_message

    with open("output.txt", mode="w") as file:
        file.write(encoded_message)


def decode(text: str, code: list[int], repeat: int = 1) -> None:
    for i in range(repeat):
        decoded_message = ""
        for e, i in enumerate(text, start=0):
            seed = code[e % (len(code))]
            if i.islower():
                decoded_message += lower[(lower.index(i) - seed) % 26]
            elif i.isupper():
                decoded_message += upper[(upper.index(i) - seed) % 26]
            elif i in symbol:
                decoded_message += symbol[(symbol.index(i) - seed) % 26]
            elif i in numbers:
                decoded_message += numbers[(numbers.index(i) - seed) % 10]
            else:
                decoded_message += i
            text = decoded_message

    with open("output.txt", mode="w") as file:
        file.write(decoded_message)


#
# with open("message.txt") as file:
#     message = file.read()
#
# encoded_text = encode(text=message, code=gen_seed_list())
# print(encoded_text)
# print("")
# print(decode(encoded_text, code=gen_seed_list()))


window = ctk.CTk()
window.title("Cipher")
window.geometry("500x600")


def get_message():
    return message_display.get("1.0", "end-1c")


def get_seed():
    if seed_value.get() == "":
        return [0]
    else:
        seed = seed_value.get().split(":")[0]
        return [int(x) for x in seed]


def get_repeat():
    if seed_value.get() == "":
        return 1
    else:
        try:
            repeat = seed_value.get()
            repeat = int(repeat.split(":")[1])
        except IndexError:
            return 1
        else:
            return repeat


message_display = ctk.CTkTextbox(window, width=500, height=500)
message_display.grid(column=1, row=0, columnspan=2)

seed_value = ctk.CTkEntry(window, width=500, height=25, placeholder_text="eg: 123456:5")
seed_value.grid(column=1, row=2, columnspan=2)

encode_button = ctk.CTkButton(window, text="encode",
                              command=lambda: (encode(text=get_message(), code=get_seed(), repeat=get_repeat())))
encode_button.grid(column=1, row=3)

decode_button = ctk.CTkButton(window, text="decode",
                              command=lambda: (decode(text=get_message(), code=get_seed(), repeat=get_repeat())))
decode_button.grid(column=2, row=3)

window.mainloop()
