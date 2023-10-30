
import random



def generate_random_number():
    return random.randint(1, 10)



def get_player_name():
    name = input("Введите ваше имя: ")
    return name



def print_greeting(name):
    print("Привет, " + name + "! Добро пожаловать в игру не на жизнь, а на смерть!!!!")
    print("Вы очутились в тёмной комнате и видите перед собой Страшное существо")
    print("Вы решаете позвать его")
    print("Тут он резко оборачивается и предлагает игру, в случае победы которой, он вас отпустит")
    print("Он решает задать вам три вопроса")

def play_game():
    player_name = get_player_name()
    print_greeting(player_name)


    questions = [
        "Как зовут самого лучшего преподавателя?)",
        "Сколько пар у нас с ней в неделю?",
        "Сколько бы пар вы хотели с ней?"
    ]


    answers = {
        "Как зовут самого лучшего преподавателя?)": "Татьяна Артамонова",
        "Сколько пар у нас с ней в неделю?": "одна, а хотелось бы больше)",
        "Сколько бы пар вы хотели с ней?": "десять"
    }


    correct_answers = set()

    for question in questions:
        print(question)
        user_answer = input("Введите ответ: ")


        if user_answer.lower() == answers[question].lower():
            print("Правильный ответ, да вы гений!")
            correct_answers.add(question)
        else:
            print("Неправильный ответ, учи уроки, неуч!")

    print("Вы ответили правильно на следующие вопросы:")
    for answer in correct_answers:
        print("- " + answer)



play_game()
