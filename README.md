# Daily Driver

A minimalist daily task manager that helps you focus on what matters most. Built with PyQt5, Daily Driver emphasizes simplicity and purposeful task management.

## Features
- Set one Most Important Task (MIT) for laser focus
- Maintain a flexible "Might-Do" list for other tasks
- Clean, dark-mode interface
- Automatic date tracking
- Local storage of tasks

## Installation

### Windows Users

1. Download the latest 'DailyDriverSetup.exe' from the [Releases](https://github.com/stdelaros/daily-drive/releases) page
2. Double-click the downloaded 'DailyDriverSetup.exe'
3. If you see a security warning, click "More info" and then "Run anyway"
4. Follow the installation wizard
5. Once installed, you can:
    - Launch from the start menu
    - Launch from the Desktop shortcut (if you chose to create one during installation)
    - Launch from the installation directory

To uninstall:
1. Go to Windows settings > Apps > Apps & features
2. Find "Daily Driver" in the list
3. Click Uninstall and follow the prompts

### macOS Users
1. Download the latest 'DailyDriver.dmg' from the [Releases](https://github.com/stdelaros/daily-drive/releases) page
2. Double-click the downloaded 'DailyDriver.dmg' file
3. If you see a security warning, go to System Preferences > Security & Privacy and click "Open Anyway"
4. In the opened DMG window, drag the Daily Driver app to your Applications folder
5. Eject the DMG
6. Launch Daily Driver from your Applications folder or Spotlight (Cmd + Space)

To uninstall:
1. Open Finder
2. Go to the Applications folder
3. Find Daily Driver
4. Drag it to the trash (or right-click and select "Move to trash")

## Building from Source

If you prefer to build from source:

1. Clone the repository:
```bash
git clone https://github.com/stdelarosa/daily-drive.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```

## Troubleshooting

### Windows
- If you see "Windows protected your PC" message, click "More info" then "Run anyway"
- If you get a "Missing DLL" error, install the [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

### macOS
- If you see "'Daily Driver' cannot be opened because the developer cannot be verified", right-click (or Control-click) the app and select Open
- If you see "'Daily Driver' is damaged and can't be opened", try downloading the DMG file again
- If Gatekeeper blocks the app, go to System Preferences > Security & Privacy > General and click "Open Anyway"