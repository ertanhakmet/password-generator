import random
import tkinter as tk
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
specialCharacters = string.punctuation


# functions
# generate password
def generate():
    passwordLength = int(passwordLengthSpinbox.get())
    characterSet = []

    if lowerCaseLettersCheckboxVar.get():
        characterSet.append(lowercase)
    if upperCaseLettersCheckboxVar.get():
        characterSet.append(uppercase)
    if numbersCheckboxVar.get():
        characterSet.append(numbers)
    if specialCharactersCheckboxVar.get():
        characterSet.append(specialCharacters)

    if not characterSet:
        newPasswordEntry.delete(0, "end")
        newPasswordEntry.insert(0, "Select at least 1 set")
        return

    password = ""
    for _ in range(passwordLength):
        selectedCharacterSet = random.choice(characterSet)
        randomCharacter = random.choice(selectedCharacterSet)
        password += randomCharacter

    newPasswordEntry.delete(0, "end")
    newPasswordEntry.insert(0, password)


# copy to clipboard
def copy():
    newPassword = newPasswordEntry.get()
    if newPassword:
        window.clipboard_clear()
        window.clipboard_append(newPassword)
        window.update()
        newPasswordEntry.delete(0, "end")


# window application
window = tk.Tk()
window.title("Password Generator")

# password length
passwordLengthLabel = tk.Label(window, text="Password length:")
passwordLengthLabel.grid(row=0, column=0, padx=12, pady=5, sticky=tk.W)

# password length spinbox
passwordLengthSpinbox = tk.Spinbox(window, from_=4, to=24)
passwordLengthSpinbox.grid(row=0, column=1, padx=12, pady=5)

# Checkbox
# lowercase letters
lowerCaseLettersCheckboxVar = tk.BooleanVar()
lowerCaseLettersCheckbox = tk.Checkbutton(window, text="Lowercase Letters", variable=lowerCaseLettersCheckboxVar)
lowerCaseLettersCheckbox.grid(row=1, column=0, padx=12, pady=1, sticky=tk.W)
# uppercase letters
upperCaseLettersCheckboxVar = tk.BooleanVar()
upperCaseLettersCheckbox = tk.Checkbutton(window, text="Uppercase Letters", variable=upperCaseLettersCheckboxVar)
upperCaseLettersCheckbox.grid(row=2, column=0, padx=12, pady=1, sticky=tk.W)
# numbers letters
numbersCheckboxVar = tk.BooleanVar()
numbersCheckbox = tk.Checkbutton(window, text="Numbers", variable=numbersCheckboxVar)
numbersCheckbox.grid(row=3, column=0, padx=12, pady=1, sticky=tk.W)
# special characters
specialCharactersCheckboxVar = tk.BooleanVar()
specialCharactersCheckbox = tk.Checkbutton(window, text="Special Characters", variable=specialCharactersCheckboxVar)
specialCharactersCheckbox.grid(row=4, column=0, padx=12, pady=1, sticky=tk.W)

# generate button
generateButton = tk.Button(window, text="Generate Password", command=generate)
generateButton.grid(row=5, column=0, columnspan=2, pady=5)

# New Password Label
newPasswordLabel = tk.Label(window, text="New Generated Password:")
newPasswordLabel.grid(row=6, column=0, padx=12, pady=5)

# password length spinbox
newPasswordEntry = tk.Entry(window)
newPasswordEntry.grid(row=6, column=1, pady=5)

# Copy to clipboard button
copyButton = tk.Button(window, text="Copy", command=copy)
copyButton.grid(row=7, column=0, columnspan=2, pady=10)

# mainloop
window.mainloop()
