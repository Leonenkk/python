import random
import os
import file_operations
from faker import Faker


FAKE = Faker("ru_RU")
SKILL_LIST = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар",
              "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
LETTER_MAPPING = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def get_runic_skills(letter_replacement, ability_list):
    runic_skills = []
    for skill in ability_list:
        runic_skill = skill
        for key, value in letter_replacement.items():
            runic_skill = runic_skill.replace(key, value)
        runic_skills.append(runic_skill)
    return runic_skills


def generate_random_context(runic_skill):
    sample_skill_list = random.sample(runic_skill, 3)
    return {
        "first_name": FAKE.first_name(),
        "last_name": FAKE.last_name(),
        "job": FAKE.job(),
        "town": FAKE.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": sample_skill_list[0],
        "skill_2": sample_skill_list[1],
        "skill_3": sample_skill_list[2]
    }


def main():
    runic_skills = get_runic_skills(LETTER_MAPPING, SKILL_LIST)
    os.makedirs("photo_svg", exist_ok=True)
    for num in range(1, 11):
        context = generate_random_context(runic_skills)
        output_path = os.path.join("photo_svg", f"output_photo{num}.svg")
        file_operations.render_template("charsheet.svg", output_path, context)


if __name__ == '__main__':
    main()
