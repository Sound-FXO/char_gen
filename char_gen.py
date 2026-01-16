import os
import file_operations
from faker import Faker
import random


fake = Faker("ru_RU")
dir_name = "dirforsheets"
os.makedirs(dir_name, exist_ok=True)
skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]
letters_mapping = {
    "а": "а͠",
    "б": "б̋",
    "в": "в͒͠",
    "г": "г͒͠",
    "д": "д̋",
    "е": "е͠",
    "ё": "ё͒͠",
    "ж": "ж͒",
    "з": "з̋̋͠",
    "и": "и",
    "й": "й͒͠",
    "к": "к̋̋",
    "л": "л̋͠",
    "м": "м͒͠",
    "н": "н͒",
    "о": "о̋",
    "п": "п̋͠",
    "р": "р̋͠",
    "с": "с͒",
    "т": "т͒",
    "у": "у͒͠",
    "ф": "ф̋̋͠",
    "х": "х͒͠",
    "ц": "ц̋",
    "ч": "ч̋͠",
    "ш": "ш͒͠",
    "щ": "щ̋",
    "ъ": "ъ̋͠",
    "ы": "ы̋͠",
    "ь": "ь̋",
    "э": "э͒͠͠",
    "ю": "ю̋͠",
    "я": "я̋",
    "А": "А͠",
    "Б": "Б̋",
    "В": "В͒͠",
    "Г": "Г͒͠",
    "Д": "Д̋",
    "Е": "Е",
    "Ё": "Ё͒͠",
    "Ж": "Ж͒",
    "З": "З̋̋͠",
    "И": "И",
    "Й": "Й͒͠",
    "К": "К̋̋",
    "Л": "Л̋͠",
    "М": "М͒͠",
    "Н": "Н͒",
    "О": "О̋",
    "П": "П̋͠",
    "Р": "Р̋͠",
    "С": "С͒",
    "Т": "Т͒",
    "У": "У͒͠",
    "Ф": "Ф̋̋͠",
    "Х": "Х͒͠",
    "Ц": "Ц̋",
    "Ч": "Ч̋͠",
    "Ш": "Ш͒͠",
    "Щ": "Щ̋",
    "Ъ": "Ъ̋͠",
    "Ы": "Ы̋͠",
    "Ь": "Ь̋",
    "Э": "Э͒͠͠",
    "Ю": "Ю̋͠",
    "Я": "Я̋",
    " ": " ",
}
number = 0


def create_a_charsheet():
    global number
    number += 1
    runic_skills = []

    for skill in skills:
        runic_skill = ""
        for letter in skill:
            runic_letter = letter.replace(letter, letters_mapping[letter])
            runic_skill += runic_letter
        runic_skills.append(runic_skill)

    chosen_skills = random.sample(runic_skills, 3)

    runic_skill_1, runic_skill_2, runic_skill_3 = (
        chosen_skills[0],
        chosen_skills[1],
        chosen_skills[2],
    )

    str_points = random.randint(3, 18)
    agil_points = random.randint(3, 18)
    endur_points = random.randint(3, 18)
    int_point = random.randint(3, 18)
    luck_points = random.randint(3, 18)

    context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": str_points,
        "agility": agil_points,
        "endurance": endur_points,
        "intelligence": int_point,
        "luck": luck_points,
        "skill_1": runic_skill_1,
        "skill_2": runic_skill_2,
        "skill_3": runic_skill_3,
    }

    file_operations.render_template(
        "charsheet.svg",
        "dirforsheets/editedcharsheet{}.svg".format(str(number)),
        context,
    )


def main():
    for i in range(10):
        create_a_charsheet()


if __name__ == "__main__":
    main()
