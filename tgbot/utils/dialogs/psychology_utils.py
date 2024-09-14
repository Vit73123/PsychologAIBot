from tgbot.config import Config
from tgbot.utils.dialogs.text_utils import *
from tgbot.utils.services import (get_prompt,
                                  get_prompt_info)

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def create_prompt(user_data: dict, config: Config, i18n: TranslatorRunner, prompt_info: dict = None) -> str:
    if not prompt_info:
        prompt_info = get_prompt_info('psychology', config)

    prompt_gpt = get_prompt(prompt_info, config)
    prompt_text = create_prompt_text(user_data, i18n)

    return ' '.join([prompt_gpt, prompt_text])


def create_prompt_text(user_data: dict, i18n: TranslatorRunner) -> str:
    if user_data['name']:
        name_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.name(), user_data['name']])
    else:
        name_string = i18n.gpt.pmt.psycholog.person.name.anoninm()

    if user_data['age']:
        age_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.age(), create_age_f_string(age=user_data['age'], i18n=i18n)])
    else:
        age_string = i18n.gpt.pmt.psycholog.person.age.anonim()

    if user_data['gender']:
        gender_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.gender(), create_gender_string(gender=user_data['gender'], i18n=i18n)])
    else:
        gender_string = i18n.gpt.pmt.psycholog.person.gender.anonim()

    if user_data['status_text']:
        status_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.status(), user_data['status_text']])
    else:
        status_string = ''

    if user_data['grade']:
        grade_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.grade(), create_grade_f_string(user_data['grade'])])
    else:
        grade_string = ''

    if user_data['review'] in user_data:
        review_string = ' '.join(
            [i18n.gpt.pmt.psycholog.person.review(), user_data['review']])
    else:
        review_string = ''

    text = ', '.join([name_string, age_string, gender_string])

    if status_string:
        text = '. '.join([text, status_string])
    if grade_string:
        text = '. '.join([text, grade_string])
    if review_string:
        text = '. '.join([text, review_string])

    return text
