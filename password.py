def ask_password(q):
    c = 0
    while c != 4:
        if q == 'password':
            print('Пароль принят')
            return
        else:
            c += 1

w = input('Введите пароль:')
ask_password(w)