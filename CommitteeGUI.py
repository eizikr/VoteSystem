import PySimpleGUI as sg
from Voter_GUI import getCenterLayout
from DB_Functions import *
from token_generator import *

RESULTS_BUTTON = "Show results"
VERIFY_BUTTON = "Verify button"

def committeeWindow(shared_key):
    '''Open window that manages the committee system'''
    # Setup        
    layout = [
                [sg.Text("Enter token to verify "),sg.InputText(key='-TOKEN-'),sg.Button(VERIFY_BUTTON)],
                [sg.Button(RESULTS_BUTTON)]
                ]
    window = sg.Window(title="Vote", layout=getCenterLayout(layout))
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            # End program if user closes window or
            break
        
        if event == RESULTS_BUTTON:
            # Show results
            democrats,republicans,corrupted = getAllVotes()
            sg.popup_ok(f"Democrats = {democrats:.2f}%, Republicans = {republicans:.2f}%, corrapted = {corrupted:.2f}%",title="Results")
        
        elif event == VERIFY_BUTTON:
            # Verify token string
            try:
                token = values['-TOKEN-']
                if verifyToken(token, shared_key):
                    sg.popup_ok("This is a valid token!",title="Token verified")
                else:
                    sg.popup_error("Your token is invalid!", title="Invalid token")

            except jwt.exceptions.DecodeError:
                sg.popup_error("Your token is invalid!", title="Invalid token")

    window.close()