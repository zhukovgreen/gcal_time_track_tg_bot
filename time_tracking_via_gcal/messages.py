INTRO_MSG = (
    "This bot helps you create customized reports "
    "by tracking you google calendar events.\n\n"
    "Available commands are:\n"
    "`\start` - start the bot\n"
    "`\settings` - see/update your report settings\n"
)
ALREADY_REGISTRED_USER_MSG = (
    "User with this id is already registered"
)
GCAL_BUILD_NOTIF_MSG = r"Google calendar was built for the user {user_id}"
CURRENT_STATE_MSG = r"Your current state is {state}"
ENTER_CAL_ID_MSG = "Now, enter your calendar id"
SMTH_WENT_WRONG_MSG = "Something went wrong"
SEND_JSON_MSG = (
    "OK. Now, send me the json file, "
    "which you generated from google api"
)
YOU_CAN_USE_BOT_MSG = "Great. Now you can use the bot"

SETTINGS_REGEX = (
    r"(\d+|(?:\d+\.\d+)) ([A-Z]{3}) *((?:.*, ?)*.*)"
)
SETTINGS_GET_MSG = "Your settings are:\n\n{settings}"

SETTING_FMT_MSG = (
    "Enter new settings in the format like\n"
    "{hour_rate} {currency} '{tag1}','{tag2}'...'{tagX}'\n"
    "number of tags could be from 0 to any number."
    "then any value will be accepted inside []\nExamples:\n"
    "40.0 EUR GT,dev,sprint2-1-0\n"
    "40.0 EUR ,,sprint2-1-0\n"
    "1000 RUB"
)
SETTINGS_WRONG_FMT_MSG = "Wrong format"
SETTINGS_UPD_SUCCESS_MSG = (
    "Settings updated successfully"
)
