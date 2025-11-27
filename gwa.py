from pyscript import display, document

def compute_gwa(e):
    document.getElementById('output').innerHTML = ""

    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value

    subjects = ["science", "math", "english", "filipino", "ict", "pe"]
    units = (1, 5, 5, 5, 1, 3)

    science= float(document.getElementById('pe').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

    grades = ["science", "math", "english", "filipino", "ict", "pe"]

    total_weight = 0
    weighted_sum = 0

    weighted_sum += science* units[0]
    weighted_sum += math * units[1]
    weighted_sum += english * units[2]
    weighted_sum += filipino * units[3]
    weighted_sum += ict * units[4]
    weighted_sum += pe * units[5]

    total_weight = sum(units)
    gwa = weighted_sum / total_weight

    display(f"Student: {fname} {lname}", target="output")
    display(f"General Weighted Average: {gwa:.2f}", target="output")