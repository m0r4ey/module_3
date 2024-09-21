# Способы вызова функции.

def send_email (message, recipient, sender = "university.help@gmail.com"):
    domens = [".com", ".ru", ".net"]
    recipient_domen = False
    sender_domen = False
    for i in range(len(domens)):
        if domens[i] in recipient:
            if "@" in recipient:
                recipient_domen = True
        if domens[i] in sender:
            if "@" in sender:
                sender_domen = True
    if recipient_domen == sender_domen == True:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
            return
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            return
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            return
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        if recipient_domen == False:
            print(f"Ошибка была допущена: {recipient}")
        if sender_domen == False:
            print(f"Ошибка была допущена: {sender}")
        return


send_email("Hello, bro!", "mymail_good@mail.net")
print()
send_email("Hello, bro!", "mymail_goodmail.net")
print()
send_email("Hello, bro!", "mymail_good@mail.ne")
print()
send_email("Hello, bro!", "university.help@gmail.com")
print()
send_email("Hello, bro!", "mymail_good@mail.net", sender = "university.help@mail.ru")

