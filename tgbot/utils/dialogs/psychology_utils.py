from fluentogram import TranslatorRunner

from tgbot.config import Config
from tgbot.utils.services.gpt_utils import (get_prompt,
                                            load_prompt_info)


def create_prompt(person_data: dict, config: Config, i18n: TranslatorRunner, prompt_info: dict = None) -> str:
    if not prompt_info:
        prompt_info = load_prompt_info('psychology', config)

    prompt_gpt = get_prompt(prompt_info, config)
    prompt_text = create_prompt_text(person_data, i18n)

    return ' '.join([prompt_gpt, prompt_text])


def create_prompt_text(person_data: dict, i18n: TranslatorRunner) -> str:
    if 'name' in person_data:
        name_string = ' '.join([i18n.gpt.pmt.psycholog.person.name(), person_data['name']])
    else:
        name_string = i18n.gpt.pmt.psycholog.person.name.anonin()

    if 'age' in person_data:
        age_string = ' '.join([i18n.gpt.pmt.psycholog.person.age(), person_data['age']])
    else:
        age_string = i18n.gpt.pmt.psycholog.person.age.anonim()

    if 'gender' in person_data:
        gender_string = ' '.join([i18n.gpt.pmt.psycholog.person.gender(), person_data['gender']])
    else:
        gender_string = i18n.gpt.pmt.psycholog.person.gender.anonim()

    if 'status' in person_data:
        status_string = ' '.join([i18n.gpt.pmt.psycholog.person.status(), person_data['status']])
    else:
        status_string = ''

    if 'review' in person_data:
        review_string = ' '.join([i18n.gpt.pmt.psycholog.person.review(), person_data['review']])
    else:
        review_string = ''

    text = ', '.join([name_string, age_string, gender_string])
    if status_string:
        text = '. '.join(status_string)
    if review_string:
        text = '. '.join(review_string)

    return text
