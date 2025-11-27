from pyscript import display, document

Dance_Club = {
    'name': 'Dance Club',
    'description': 'A club for students who like dancing.',
    'meeting_time': 'Monday & Thursday 3-5 PM',
    'location': 'Dance Room',
    'moderator': 'Mr. Marutani',
    'members': 25
}

COCC_Club = {
    'name': 'COCC Club',
    'description': 'A leadership training club.',
    'meeting_time': 'Thursday 3-5 PM',
    'location': 'Quadrangle',
    'moderator': 'Ms. Mobilla',
    'members': 25
}

Glee_Club = {
    'name': 'Glee Club',
    'description': 'A club for students who enjoy singing.',
    'meeting_time': 'Monday & Friday 3-5 PM',
    'location': 'Music Room',
    'moderator': 'Ms. Loyola',
    'members': 25
}

clubs = {
    'Dance Club': Dance_Club,
    'COCC Club': COCC_Club,
    'Glee Club': Glee_Club
}

def show_club(event=None):
    club_name = document.getElementById('club_select').value
    info = clubs[club_name]

    document.getElementById('output').innerHTML = ""

    display(f"Name: {info['name']}", target='output')
    display(f"Description: {info['description']}", target='output')
    display(f"Meeting Time: {info['meeting_time']}", target='output')
    display(f"Location: {info['location']}", target='output')
    display(f"Moderator: {info['moderator']}", target='output')
    display(f"Members: {info['members']}", target='output')
