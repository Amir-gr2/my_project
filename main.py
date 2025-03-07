# ДЛЯ НАЧАЛА РАБОТЫ С ПРОГРАММОЙ СОЗДАТЬ В ОДНОЙ ПАПКЕ С main.py ТЕКСТОВЫЙ ФАЙЛ my_file.txt

# считываем информацию
with open("my_file.txt", "r", encoding="utf-8") as f:
    data = []
    for d in f:
        data.append(d.rstrip("\n"))
# работаем с пользователем
while True:
    print("--add - добавить(дата событие участник)")
    print("пример: 09-05-1945 День Победы СССР")
    print("--search - найти")
    print("--break - выход из программы")
    print("--stats - статистика")
    x = input()
    if x == "--break":
        break
    elif x == "--stats":
        print(f"кол-во событий: {len(data)}")
        d_cnt = {}
        for ev in data:
            year = ev[6:10]
            if year in d_cnt:
                d_cnt[year] += 1
            else:
                d_cnt[year] = 1
        for years, quan in d_cnt.items():
            print(f"в {years}: {quan} событий")
        continue
    a, b = x.split(" ", 1)
    if a == "--add":
        if data == []:
            data = [b]
        else:
            for v in range(len(data)):
                if data[v] in b:
                    data[v] = b
                else:
                    data.append(b)
    elif a == "--search":
        for v in data:
            if b in v:
                print(v)
# сохраняем данные
with open("my_file.txt", "w", encoding="utf-8") as f:
    for d in data:
        f.write(d + "\n")
