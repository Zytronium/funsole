# Funsole

A playful, interactive command-line console packed with fun commands,
colorful effects, sound effects, and easter eggs. Built for fun, experimentation,
and as a showcase of creative Python CLI programming.

---

## Screenshots

(Add screenshots or GIFs here showing the console in action!)

---

## Features

- 🎨 **Colorful Output** – Uses ANSI escape codes to make the console vibrant and lively.
- 🔊 **Sound Effects** – Plays audio cues (like alarms and scanner warnings) when `vlc` is installed.
- 🧨 **Self-Destruct Mode** – Countdown timer with dramatic effects that ends the session.
- 🚀 **Battleship Encounter** – Simulated scanner warning with suspenseful text and audio.
- 🌈 **Rainbow Printer** – Outputs a rainbow of colors in the terminal.
- 🔐 **Password Judge** – Critiques your chosen password with brutal ~~honesty~~ bias (and kicks you out if its bad enough).
- 🎵 **Rickroll Command** – Why not try it out yourself?
- 🛠 **Customizable Settings** – Toggle warnings or sound in `settings.json` or via the `settings` command.
- ⚙️ **Persistent Settings** – Your preferences are saved between sessions using JSON-based storage.
- 🥚 **Easter Eggs** – Hidden phrases and responses waiting to be discovered.

---

## Description

Funsole is not your typical command-line tool—it’s an entertainment console
disguised as a Python CLI. It blends humor, interactivity, and coding tricks
to create a unique terminal experience.

The project demonstrates:
- Using Python’s `cmd` module for building interactive shells
- Managing persistent configuration with a lightweight JSON storage engine
- Integrating audio via `python-vlc`
- ANSI color manipulation for immersive terminal effects
- A playful approach to software that prioritizes fun as much as *fun*ction

This is both a coding playground and a proof-of-concept for how creative you
can get with Python CLIs.

---

## Installation

Clone the repository
```bash
git clone https://github.com/Zytronium/funsole.git
cd funsole
```

If you want sound support:
```bash
pip install python-vlc
```
or if that doesn't work, try
```bash
pip install vlc
```

---

## Usage

Run the console:
```bash
python3 console.py
```

## Commands
| Command        | Description                                                              | Notes                                                                  |
|----------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| `help`         | Displays a list of commands.                                             | Interchangeable with `?`. Prefix a command with this to display usage. |
| `exit`, `quit` | Exits the console.                                                       | Interchangeable between `exit`, `quit`, and `EOF`.                     |
| `rickroll`     | Opens Rick Astley’s *Never Gonna Give You Up* in the browser.            | Requires an internet connection.                                       |
| `selfdestruct` | Starts a countdown (default 5 seconds) and then terminates the session.  | Plays alarm sound if enabled. Input must be a number or blank.         |
| `battleship`   | Simulates a dramatic scanner warning and enemy approach.                 | Plays "SCANNER WARNING" sound and suspense text.                       |
| `rainbow`      | Prints a rainbow of colors to the console.                               | Random chance of reverse-color effect.                                 |
| `password`     | Prompts for a password and judges it harshly.                            | Weak passwords may cause the console to exit.                          |
| `settings`     | Manage console settings (`show_warnings`, `sound`).                      | `settings` alone lists all settings.                                   |
| *easter eggs*  | Several secret commands that not listed when running the `help` command. | Not shown in help list (must be typed manually).                       |


---

## Settings

Settings are stored in `settings.json`.
Default values:
```json
{
  "show_warnings": true,
  "sound": true
}
```

Use the `settings` command in Funsole to view or update them interactively.

---

## Challenges Faced

Todo section 

The biggest challenge, if I recall correctly, was getting VLC to properly play media.
Getting settings to work was also a challenge.

---

## Development Story

Todo section

This project was inspireed by a similar school project. Instead of building an
AirBnB database manager console, I wanted to build something fun instead. Besides,
I needed somewhere to put all my fun side commands that I had implemented before
I removed them rom the final version of the AirBnB console.

---

## Future Ideas

- None - this project is complete wiht no plans to revisit. Feel free to fork and
  add your own features!

---

## About me

todo section
