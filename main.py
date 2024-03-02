import argparse
import json


def create_note(note_dict):
    with open('notes.json', 'w') as f:
        json.dump(note_dict, f)


def read_notes():
    with open('notes.json', 'r') as f:
        notes = json.load(f)
    for note in notes:
        print(note)


def edit_note(note_dict):
    with open('notes.json', 'w') as f:
        json.dump(note_dict, f)


def delete_note(note_dict):
    with open('notes.json', 'w') as f:
        json.dump(note_dict, f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', help='Создать новую заметку', action='store_true')
    parser.add_argument('-r', '--read', help='Прочитать все заметки', action='store_true')
    parser.add_argument('-e', '--edit', help='Редактировать существующую заметку', action='store_true')
    parser.add_argument('-d', '--delete', help='Удалить существующую заметку', action='store_true')
    args = parser.parse_args()

    if args.create:
        create_note(
            {'id': 'новая_заметка', 'title': 'Новая заметка', 'body': 'Это новая заметка', 'created_at': '2022-01-01'})
    elif args.read:
        read_notes()
    elif args.edit:
        edit_note(
            {'id': 'существующая_заметка', 'title': 'Редактированная заметка', 'body': 'Это отредактированная заметка',
             'created_at': '2022-01-01'})
    elif args.delete:
        delete_note({'id': 'удаленная_заметка', 'title': 'Удаленная заметка', 'body': 'Эта заметка была удалена',
                     'created_at': '2022-01-01'})


if __name__ == '__main__':
    main()
