from os import path, scandir, mkdir, system, name
from shutil import move

def main():
    source_input = input('Source? ')
    if not path.exists(source_input) or not path.isdir(source_input):
        print('Not a real source, exiting...')
        exit()

    target_input = input('Target? ')
    if path.exists(target_input) and not path.isdir(target_input):
        print('Target is not a folder, exiting...')
        exit()
    if not path.exists(target_input):
        print('Target doesn\'t exists')
        choice = input('Should I create it? (Y/N) ')
        if choice == 'y' or choice == 'Y':
            mkdir(target_input)
        else:
            exit()

    source = path.abspath(source_input)
    target = path.abspath(target_input)

    cards = [card for card in scandir(source) if card.is_dir()]
    for card in cards:
        print(f'Working on {card.name}')
        videos = [video for video in scandir(card.path) if video.is_dir()]
        for video in videos:
            print(f'Current video: {video.name}')
            folder_name = path.split(video.path)[1]
            new_folder_path = path.join(target, folder_name)
            if not path.exists(new_folder_path):
                mkdir(new_folder_path)
            parts = [part for part in scandir(video.path) if part.is_file()]
            for part in parts:
                print(f'Current file: {part.name}')
                source_path = part.path
                target_path = path.join(new_folder_path, part.name)
                move(source_path, target_path)

    print('DONE')

while True:
    main()
    choice = input('Again? (y/N) ')
    if choice == 'y' or choice == 'Y':
        command = 'cls' if name == 'nt' else 'clear'
        system(command)
    else:
        break
