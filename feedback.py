import os
import subprocess
import time


subfolder = "feedback_files"

os.makedirs(subfolder, exist_ok=True)


def get_input(prompt):
    return input(prompt)


def open_in_editor(filename):
    editor = os.getenv('EDITOR')
    subprocess.run([editor, filename])


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)


student_names = get_input("Enter the names of the students, seperated by commas: ").split(",")
print(student_names)

for student in student_names:
    student = student.strip()
    print(f"Entering feedback for {student}")

    understand_level = get_input("Enter understanding level (1: basic, 2: good, 3: very good, 4: excellent)")

    understand_descriptions = {"1": "a basic understanding", "2": "a good understanding", "3": "a very good understanding", "4": "an excellent understanding"}

    feedback = f"General comments\n{student} demonstrated {understand_descriptions[understand_level]} of python and general programming concepts.\n\n"
    feedback += f"Learener punctuality and engagement\n"
    feedback += f"Recommendations for further learning"

    filename = os.path.join(subfolder, f"{student}_feedback.txt")
    with open(filename, "w") as file:
        file.write(feedback)
        print(f"Feedback for {student}  written to file {filename}")

    print(f"Opening {filename} in the default editor to make any final adjustments...")
    countdown(3)
    open_in_editor(filename)

    print(f"Feedback for {student} has been edited and saved in file {filename}")