from pyscript import display, document
import matplotlib.pyplot as plt
import logging

logging.getLogger('matplotlib').setLevel(logging.ERROR)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
absences = [1, 2, 3, 4, 5]

def sign_in(e):
    selected_day = document.getElementById("class_day").value
    new_value = document.getElementById("absence_input").value
    
    try:
        day_index = [d.lower() for d in days].index(selected_day.lower())
        absences[day_index] = float(new_value)
    except:
        pass

    plt.clf()
    plt.plot(days, absences)
    plt.title('Days of the Week')

    display(plt, target="output", append=False)

