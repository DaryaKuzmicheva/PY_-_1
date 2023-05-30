import csv
import os
from datetime import datetime

NOTES_FILE = 'notes.csv'

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            notes = list(reader)
    else:
        notes = []
    return notes

def save_notes(notes):
    with open(NOTES_FILE, 'w', newline='') as file:
        fieldnames = ['id', 'title', 'body', 'timestamp']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(notes)

def create_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {'id': len(notes) + 1, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print('Заметка успешно создана.')

def read_notes():
    if not notes:
        print('Нет доступных заметок.')
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/Время: {note['timestamp']}")
            print('-----------------------')

def edit_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    found_note = None
    for note in notes:
        if note['id'] == note_id:
            found_note = note
            break
    if found_note:
        new_title = input('Введите новый заголовок заметки: ')
        new_body = input('Введите новый текст заметки: ')
        found_note['title'] = new_title
        found_note['body'] = new_body
        found_note['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes(notes)
        print('Заметка успешно отредактирована.')
    else:
        print('Заметка с указанным ID не найдена.')

def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Заметка успешно удалена.')
            break
    else:
        print('Заметка с указанным ID не найдена.')

def search_notes_by_date():
    date_string = input('Введите дату в формате ГГГГ-ММ-ДД: ')
    try:
        search_date = datetime.strptime(date_string, '%Y-%m-%d').date()
        found_notes = []
        for note in notes:
            note_date = datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S').date()
            if note_date == search_date:
                found_notes.append(note)
        if not found_notes:
            print('Заметки с указанной датой не найдены.')
        else:
            for note in found_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата/Время: {note['timestamp']}")
                print('-----------------------')
    except ValueError:
        print('Некорректный формат даты.')

notes = load_notes()

while True:
    print('Меню:')
    print('1. Создать новую заметку')
    print('2. Просмотреть все заметки')
    print('3. Редактировать заметку')
    print('4. Удалить заметку')
    print('5. Поиск заметок по дате')
    print('6. Выход')

    choice = input('Выберите действие (1-6): ')

    if choice == '1':
        create_note()
    elif choice == '2':
        read_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        search_notes_by_date()
    elif choice == '6':
        break
    else:
        print('Некорректный ввод. Попробуйте еще раз.')

print('Завершение программы.')
