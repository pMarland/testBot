import requests
import datetime


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
            print(len(get_result))
        else:
            print(len(get_result))
            print('1')
            last_update = get_result[len(get_result)]
            #print(last_update)

        return last_update


greet_bot = BotHandler('614387338:AAH2lQP6WVaQvfdsOy65ZEZOv5qJ2O4JrGM')
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():

    new_offset = None
    today = now.day
    hour = now.hour
    greeded_people: list = []

    while True:
        print('go')
        greet_bot.get_updates(new_offset)
        print(new_offset)
        last_update = greet_bot.get_last_update()
        #print(last_update)
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
       # print(greeded_people)
        #print(last_chat_id)
        # print(now.hour)
        # print(hour)

        if last_chat_id not in greeded_people and last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            #today += 1
            greeded_people.append(last_chat_id)

        elif last_chat_id not in greeded_people and last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            #today += 1
            greeded_people.append(last_chat_id)

        elif last_chat_id not in greeded_people and last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            #today += 1
            greeded_people.append(last_chat_id)

        elif last_chat_id not in greeded_people and last_chat_text.lower() in greetings and today == now.day and (23 <= hour or 6 > hour):
            greet_bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))
            #today += 1
            greeded_people.append(last_chat_id)

        else:
            print('test hi')
            
        if now.hour == 6 and now.minute == 0:
            greeded_people.clear()

        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
