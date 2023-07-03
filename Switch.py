import PySimpleGUI as sg
import json
import os
import re

stream = os.popen('git config --list')
try:
    output = stream.read()
    email_match = re.search(r'user.email=(.*)', output)
    name_match = re.search(r'user.name=(.*)', output)
except:
    sg.popup("Error","No existing git credentials.")

if email_match:
    global_email = email_match.group(1)

if name_match:
    global_name = name_match.group(1)

# Getting the accounts
def get_account_buttons():
    buttons = []
    try:
        with open('accountsConfig.json', 'r') as file:
            # Load the JSON data
            accounts = json.load(file)
                # Print the accounts
        for account in accounts:
            accountName = account['account']
            if global_email == account['email']:
                buttons.append(sg.Button(accountName, key=f'-ACCOUNT_{accountName}', size=(20, 4), button_color=('white', 'red')))
            else:
                buttons.append(sg.Button(accountName, key=f'-ACCOUNT_{accountName}', size=(20, 4), button_color=('white', 'green')))
        return buttons
    except:
        return buttons

    # Define the layout for the GUI
layout1 = [
    [sg.Text('Current Username:', font=('Helvetica', 14)), sg.Text(global_name, key='-CURRENT_NAME-', font=('Helvetica', 12))],
    [sg.Text('Current Email:', font=('Helvetica', 14)), sg.Text(global_email, key='-CURRENT_EMAIL-', font=('Helvetica', 12))],
    [sg.Button('Add Account', key='-ADD_ACCOUNT-', size=(10, 1)), sg.Button('Remove Account', key='-REMOVE_ACCOUNT-', size=(14, 1))],
    get_account_buttons()
]

# Create the window
window = sg.Window('Git Account Switcher', layout1, size=(550,200))

# Event loop to process events and get user input
while True:
    event, values = window.read()
    

    # Exit the application if the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Handle account button clicks
    if event.startswith('-ACCOUNT_'):
        target_account = event.split('_')[1]

        # Get the username and email from the accountsConfig using the target account identifier
        with open('accountsConfig.json', 'r') as file:
            # Load the JSON data
            accounts = json.load(file)
        for account in accounts:
            if account['account'] == target_account:

                global_email = account['email']
                global_name = account['username']
                break

        # Setting the global config settings
        stream = os.popen(f'git config --global user.name "{global_name}"')
        stream = os.popen(f'git config --global user.email {global_email}')

        layout3 = [
            [sg.Text('Current Username:', font=('Helvetica', 14)), sg.Text(global_name, key='-CURRENT_NAME-', font=('Helvetica', 12))],
            [sg.Text('Current Email:', font=('Helvetica', 14)), sg.Text(global_email, key='-CURRENT_EMAIL-', font=('Helvetica', 12))],
            [sg.Button('Add Account', key='-ADD_ACCOUNT-', size=(10, 1)), sg.Button('Remove Account', key='-REMOVE_ACCOUNT-', size=(14, 1))],
            get_account_buttons()
        ]

        window.close()
        window = sg.Window('Git Account Switcher', layout3, size=(550,200))


    # Handle add account button click
    elif event == '-ADD_ACCOUNT-':
        try:
            with open('accountsConfig.json', 'r') as file:
                accounts = json.load(file)
        except FileNotFoundError:
            # Create a new file and initialize it with an empty list
            accounts = []
            with open('accountsConfig.json', 'w') as file:
                json.dump(accounts, file)

        if len(accounts) > 2:
            sg.popup("Account Limit Reached", "You have reached the limit of accounts that can be added at once.")
        else:   
            layout2 = [
                [sg.Text('Account Type:', size=(12, 1)), sg.Input(key='-ACCOUNT_TYPE-', size=(20, 1))],
                [sg.Text('Email:', size=(12, 1)), sg.Input(key='-EMAIL-', size=(20, 1))],
                [sg.Text('Username:', size=(12, 1)), sg.Input(key='-USERNAME-', size=(20, 1))],
                [sg.Button('Add', key='-WRITE_ACCOUNT-', size=(10, 1))]
            ]
            
            window.close()
            window = sg.Window('Git Account Switcher', layout2, size=(300,125))

    elif event == '-WRITE_ACCOUNT-':
        account_type = values['-ACCOUNT_TYPE-']
        email = values['-EMAIL-']
        username = values['-USERNAME-']

        with open('accountsConfig.json', 'r') as file:
            accounts = json.load(file)

        new_account = {
            "account": account_type,
            "username": username,
            "email": email
        }

        accounts.append(new_account)

        with open('accountsConfig.json', 'w') as file:
            json.dump(accounts, file, indent=4)

        layout3 = [
            [sg.Text('Current Username:', font=('Helvetica', 14)), sg.Text(global_name, key='-CURRENT_NAME-', font=('Helvetica', 12))],
            [sg.Text('Current Email:', font=('Helvetica', 14)), sg.Text(global_email, key='-CURRENT_EMAIL-', font=('Helvetica', 12))],
            [sg.Button('Add Account', key='-ADD_ACCOUNT-', size=(10, 1)), sg.Button('Remove Account', key='-REMOVE_ACCOUNT-', size=(14, 1))],
            get_account_buttons()
        ]

        window.close()
        window = sg.Window('Git Account Switcher', layout3, size=(550,200))

    elif event == '-REMOVE_ACCOUNT-':
        with open('accountsConfig.json', 'r') as file:
            # Load the JSON data
            accounts = json.load(file)
        for account in accounts:
            if account['email'] == global_email:
                accounts.remove(account)
                break

        with open('accountsConfig.json', 'w') as file:
            json.dump(accounts, file, indent=4)
        
        global_email = ""
        global_name = ""

        layout4 = [
            [sg.Text('Current Username:', font=('Helvetica', 14)), sg.Text(global_name, key='-CURRENT_NAME-', font=('Helvetica', 12))],
            [sg.Text('Current Email:', font=('Helvetica', 14)), sg.Text(global_email, key='-CURRENT_EMAIL-', font=('Helvetica', 12))],
            [sg.Button('Add Account', key='-ADD_ACCOUNT-', size=(10, 1)), sg.Button('Remove Account', key='-REMOVE_ACCOUNT-', size=(14, 1))],
            get_account_buttons()
        ]

        window.close()
        window = sg.Window('Git Account Switcher', layout4, size=(550,200))

# Close the window
window.close()