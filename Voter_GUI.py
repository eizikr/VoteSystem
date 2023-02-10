import PySimpleGUI as sg
from DB_Functions import *

SUBMIT_ID_BUTTON ="submit id"
POLLING_STATIONS_AMOUNT = 14

def getCenterLayout(layout):
    return [
        [sg.Column(layout,element_justification = "center")]
    ]

def end_window(token):
    # Close window
    # Setup
    layout = [
                [sg.Text("Thank you for voting! your token is:")],
                [sg.Text(token)],
            ]
    window = sg.Window(title="Vote", layout=getCenterLayout(layout))
    while True:
        event, values = window.read()
        # End program if user closes window or
        if event == sg.WIN_CLOSED:
            break
            
    window.close()
    voterGUI()

def vote_window(idIndex):
    # Setup
    layout_vote = [
                [sg.Text("vote")],
                [sg.Text("choose polling station "),sg.Combo([i for i in range(1,POLLING_STATIONS_AMOUNT)],key='station')],
                [sg.Button(PARTY1),sg.Button(PARTY2)]
                ]

    window = sg.Window(title="Vote", layout=getCenterLayout(layout_vote))
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        if event == sg.WIN_CLOSED:
            break
        if event == PARTY1 or event == PARTY2:
            station = values["station"]
            if type(station) is str:
                sg.popup_error("Please choose polling station", title="An error Occurred")
            else:
                votes_sheet,votes_book = getSheet(VOTES_DB)
                token = writeVoter(event,station,generateIV(),votes_book)
                window.close()
                updateVotersDB(idIndex)
                end_window(token)
                

    window.close()


def voterGUI():
    # Setup
    layout_idInput = [[sg.Text("Wellcome to USA vote system")],
            [sg.Text('Enter id'), sg.InputText(key='-ID-')],
            [sg.Button(SUBMIT_ID_BUTTON)]]

    # Create the window
    window = sg.Window(title="Voting system", layout=getCenterLayout(layout_idInput))
    sheet,book = getSheet(VOTERS_DB)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # Presses the OK button
        if event == sg.WIN_CLOSED:
            break
        if event == SUBMIT_ID_BUTTON:
            try:
                id = int(values['-ID-'])
                # Check id
                value = vote(sheet,id)
                if type(value) is str: #value == error string
                    sg.popup_error(value, title="An error Occurred")
                else:
                    window.close()
                    vote_window(value) #value == index
            except ValueError as err:
                sg.popup_error("id must be numbers only", title="An error Occurred")      

    window.close()
