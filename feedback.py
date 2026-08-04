raw_feedback = " THE SPEAKER WAS GREAT but THE ROOM WAS COLD "
cleaned = raw_feedback.strip().lower()
cleaned = cleaned.replace("speaker", "presenter")
cleaned = " ".join(cleaned.split())
final_feedback = cleaned.title()
print(f"Cleaned Feedback: {final_feedback}")


feedback_list = [
    "The Presenter Was Great But The Room Was Cold",
    "I Learned A Lot From This Workshop",
    "The Session Was Too Long But Very Informative"
]

with open("feedback.txt", "w") as file:
    for item in feedback_list:
        file.write(item + "\n")

print("--- Initial Feedback ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())

new_feedback = "Great Presentation And Excellent Materials"
with open("feedback.txt", "a") as file:
    file.write(new_feedback + "\n")

print("\n--- Updated Feedback ---")
with open("feedback.txt", "r") as file:
    for line in file:
        print(line.strip())


try:
    with open("feedback.txt", "r") as file:
        print("--- Reading Feedback File ---")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found. Please create feedback.txt first.")
except PermissionError:
    print("Permission denied. Close the file and try again.")
finally:
    print("Operation completed.")


total_feedback = 0
great_count = 0

with open("feedback.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    total_feedback += 1
    if "great" in line.lower():
        great_count += 1

with open("summary.txt", "w") as file:
    file.write("=== Workshop Feedback Summary ===\n")
    file.write(f"Total Feedback: {total_feedback}\n")
    file.write(f"Mentions of 'Great': {great_count}\n")

print("=== Workshop Feedback Summary ===")
print(f"Total Feedback: {total_feedback}")
print(f"Mentions of 'Great': {great_count}")
