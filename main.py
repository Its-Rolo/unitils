#!/usr/bin/env python3

import configparser
from datetime import datetime, time
import argparse

classes = []
class_rooms = []
times = {
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
}

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M").time()

def load_config():
    config = configparser.ConfigParser()
    config.read('config.conf')
    for section in config.sections():
        class_name = config[section]['name']
        classes.append(class_name)

        class_room = config[section].get('room', 'N/A')
        class_rooms.append(class_room)

        for key in config[section]:
            if key not in ['name', 'room']:
                day, time_type = key.split('_', 1)
                if time_type == 'start_time':
                    start_time = parse_time(config[section][key])
                    end_time_key = f"{day}_end_time"
                    end_time = parse_time(config[section].get(end_time_key, '00:00'))
                    times[day.lower()].append((class_name, start_time, end_time))

def find_next_class(current_time):
    current_day = datetime.now().strftime("%A").lower()
    current_time = parse_time(current_time)
    next_class = None
    for cls in times[current_day]:
        if cls[1] > current_time:
            if next_class is None or cls[1] < next_class[1]:
                next_class = cls
    return next_class

def display_all_classes():
    for day, classes in times.items():
        print(f"{day.capitalize()}:")
        sorted_classes = sorted(classes, key=lambda cls: cls[1])
        for cls in sorted_classes:
            start_time_str = cls[1].strftime("%-I:%M %p")
            end_time_str = cls[2].strftime("%-I:%M %p")
            print(f"  {cls[0]}: {start_time_str} - {end_time_str}")
        print()

def main():
    parser = argparse.ArgumentParser(description="University Utils")
    parser.add_argument('--nextclass', action='store_true', help="Show the next class")
    args = parser.parse_args()

    load_config()

    if args.nextclass:
        current_time = datetime.now().strftime("%H:%M")
        next_class = find_next_class(current_time)
        if next_class:
            start_time_str = next_class[1].strftime("%-I:%M %p")
            print(f"Next class is {next_class[0]} at {start_time_str}")
        else:
            print("\033[1m              No more classes today!\033[0m")
            print_ascii_art("./ascii/noClassesLeft.txt")
    else:
        print("Classes:", classes)
        print("Class Rooms:", class_rooms)
        print("Times:", times)
        display_all_classes()

def print_ascii_art(file_path):
    with open(file_path, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    main()


"""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠾⠛⠛⠉⠉⠉⠉⠉⠛⠻⠶⣤⣀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣯⠉⠙⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠟⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠋⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⡀⠀⠀⠈⠙⠷⣦⣤⣄⣠⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣄⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠈⠉⠻⣦⡀⠀
⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢠⡾⠂⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡿⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀
⠀⠀⠀⢀⣴⠟⠁⠀⣀⣤⠶⠞⠛⠻⠶⣤⡀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⢤⣶⢻⡟⣶⢠⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃
⠀⠀⢠⡟⠁⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠈⢿⣌⣛⡋⠀⠀⠀⠸⢧⡴⠛⠓⠞⠁⠀⠀⠀⠈⠛⠛⢈⣥⠟⠁⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⠏⠀
⠀⠀⣾⠁⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡽⠟⠀⠀⠀⠀⠀⢀⣤⣤⣴⣤⣄⣀⣤⣤⠶⠞⠛⠁⠀⠀⠀⠀⠀⠉⠛⠶⢦⣤⣤⣤⣤⣤⡶⠾⠋⠁⠀⠀
⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⣀⣀⣀⣀⣤⣤⣴⡟⠁⠘⣧⠀⠙⠻⠋⠛⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠿⢋⣩⣽⠿⣯⣽⡇⠸⠋⠀⠀⣸⡟⠷⣤⡀⠀⠀⠈⠻⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠶⠶⠶⠚⠛⠋⠉⠀⣰⡟⠉⢀⡀⠀⣿⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⣰⠟⠉⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⣿⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠘⠷⣤⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣧⣀⣀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⢈⣻⢦⣄⣀⣀⠀⢠⣴⣶⠞⠛⠉⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠁⠀⠈⠛⢷⣤⣤⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⠱⠊⡱⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠒⠒⠒⠒⠤⢄⣑⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠝⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⢄⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⢰⣢⠐⡄⠀⠉⠑⠒⠒⠒⣄
⠀⠀⠀⣀⠴⠋⠀⠀⠀⡎⠀⠘⠿⠀⠀⢠⣀⢄⡢⠉⣔⣲⢸⠀⠀⠀⠀⠀⠀⢘
⡠⠒⠉⠀⠀⠀⠀⠀⡰⢅⠫⠭⠝⠀⠀⠀⠀⠀⠀⢀⣀⣤⡋⠙⠢⢄⣀⣀⡠⠊
⢇⠀⠀⠀⠀⠀⢀⠜⠁⠀⠉⡕⠒⠒⠒⠒⠒⠛⠉⠹⡄⣀⠘⡄⠀⠀⠀⠀⠀⠀
⠀⠑⠂⠤⠔⠒⠁⠀⠀⡎⠱⡃⠀⠀⡄⠀⠄⠀⠀⠠⠟⠉⡷⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠤⠤⠴⣄⡸⠤⣄⠴⠤⠴⠄⠼⠀⠀⠀⠀⠀⠀⠀⠀
"""