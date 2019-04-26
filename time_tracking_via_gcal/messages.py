DESCR_ON_CAL_NAMING_PRINCIPLE = (
    "In order to make the bot recognize your cal events "
    "you have to identify your events names by tags. "
    "It is easier to show this on examples:\n\n"
    "'cg','dev' - 'some descr [{only}CG{or}cg][{only}dev]'. "
    "Report builds the pivot table with index 'cg', then 'dev'\n\n"
    "'','' - 'some descr [{any}][{any}]'. "
    "Report builds the pivot table with index '{any}', then '{any}'\n\n"
    "and so on"
)

INTRO_MSG = (
    "This bot helps you create customized reports "
    "by tracking your google calendar events.\n\n"
    "Available commands are:\n"
    "`/start` - start the bot\n"
    "`/settings` - see/update your report settings\n"
    "`/help` - get help\n\n"
    "By clicking on the buttons (i.e. this week, "
    "previous week etc.) in the main menu (available "
    "only after finsihing the authentication process,\n"
    "you will receive a corresponding report as "
    "a text message and csv file.\n\n"
    + DESCR_ON_CAL_NAMING_PRINCIPLE
)
HELP_MSG = (
    "You can either submit a support ticket"
    " (github registration required). "
    "Or you can ask in the support channel.\n\n"
    "Just in case reminding you the intro:\n\n"
)
ALREADY_REGISTRED_USER_MSG = (
    "User with this id is already registered"
)
CURRENT_STATE_MSG = r"Your current state is {state}"
ENTER_CAL_ID_MSG = "Now, enter your calendar id"
SMTH_WENT_WRONG_MSG = "Something went wrong"
THIS_IS_BAD_FILE_MSG = (
    "Looks like this is not a"
    " correct json file... Try one more time..."
)
SEND_JSON_MSG = (
    "OK. Now, send me the json file, "
    "which you generated from google api"
)
YOU_CAN_USE_BOT_MSG = (
    "Great. Now you can use the"
    " bot, just update your report settings."
)
PROBLEM_WITH_CAL_AUTH_MSG = (
    "It looks like you have no access to your calendar."
    " Forwarding you to revalidate your credentials"
    + "\n\n"
    + ENTER_CAL_ID_MSG
)

SETTINGS_REGEX = (
    r"(\d+|(?:\d+\.\d+)) ([A-Z]{3}) *((?:.*, ?)*.*)"
)
SETTINGS_GET_MSG = (
    "Your settings are:\n\n{settings}\n\n"
)

SETTING_FMT_MSG = (
    "Enter new settings in the format like\n"
    "{hour_rate} {currency} {tag1},{tag2}...{tagX}\n"
    "number of tags could be from 0 to any number."
    "then any value will be accepted inside []\nExamples:\n"
    "40.0 EUR GT,dev,sprint2-1-0\n"
    "40.0 EUR ,,sprint2-1-0\n"
    "1000 RUB\n"
    "1000 RUB ,"
)
SETTINGS_WRONG_FMT_MSG = "Wrong format"
SETTINGS_UPD_SUCCESS_MSG = (
    "Settings updated successfully"
)
