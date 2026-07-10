exam_dict = {}
submissions = {}


def add_submission(submissions_, language_):
    if language_ not in submissions_:
        submissions_[language_] = 1
    else:
        submissions_[language_] += 1


while True:
    data = input()

    if data == "exam finished":
        break

    if "banned" in data:
        username = data.split("-")[0]

        if username in exam_dict:
            exam_dict.pop(username)

        continue

    username, language, points = data.split("-")
    points = int(points)

    add_submission(submissions, language)

    if username not in exam_dict:
        exam_dict[username] = {language: points}

    elif language not in exam_dict[username]:
        exam_dict[username][language] = points

    else:
        if points > exam_dict[username][language]:
            exam_dict[username][language] = points


print("Results:")

for user, languages in exam_dict.items():
    best_result = max(languages.values())
    print(f"{user} | {best_result}")

print("Submissions:")

for language, count in submissions.items():
    print(f"{language} - {count}")