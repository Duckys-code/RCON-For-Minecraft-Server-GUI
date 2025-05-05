📦 How to Install: Minecraft RCON GUI (aka the "We-Made-It-Easy" Edition)

    Download the .exe
    It's just one file, don't worry, no extra nonsense. Just click the Download Link.

    Run the .exe
    No, really. That's it. Just double-click it. Your computer won’t explode, I promise.

    Connect to Your Server
    Open the app, throw in your server’s IP, RCON password, and hit Connect. (No need to memorize a ton of stuff. It's a GUI, not a science exam.)

    Hit STOP or RESTART
    Wanna turn off your server? Hit STOP.
    Wanna make it go on a rollercoaster ride? Hit RESTART.
    Simple, right?

    Check the Stats
    Player count? Check.
    Your server’s RAM and CPU usage? Check.
    You'll have more stats than you can shake a Minecraft stick at.

    Send Commands (Optional)
    Want to spam the server with commands? Just type it in and hit Send. Yes, it’s that easy.

🛠️ Troubleshooting:

    Q: I can’t run the .exe!
    A: Check your antivirus. It’s probably trying to protect you from all that power.

    Q: How do I exit the app?
    A: The red X in the corner works. (You can also just press Alt + F4, but we like to keep it casual.)

Enjoy managing your Minecraft server without dealing with a million windows or lines of code. Just download, click, and play!


💀 How to Install (If You Want to Die Edition)

So… you want to run the Python version instead of just using the .exe like a normal person? Bold move. Here's how to do it anyway:
🐍 Step 1: Install Python (if you don’t already have it)

Go here and download Python:
👉 https://www.python.org/downloads/
Make sure to check the box that says “Add Python to PATH” during installation, or things will break, and so will your spirit.
📁 Step 2: Get the Files

    Download or clone this repo:

    git clone https://github.com/Duckys-code/RCON-For-Minecraft-Server-GUI.git

📦 Step 3: Install Dependencies

Open a terminal (or CMD) in the project folder and run:

pip install mcrcon psutil

Or if you're using a requirements.txt file:

pip install -r requirements.txt

With this requirements.txt:

mcrcon
psutil

▶️ Step 4: Run the App

python main.py

Or if you're really feeling lucky:

py main.py

🧪 Want to Make It an .exe?

So you want pain. Cool. Here’s how to turn your Python script into a shiny .exe:
Step 1: Install auto-py-to-exe

pip install auto-py-to-exe

Then launch it:

auto-py-to-exe

Step 2: Use the GUI

A wild window appears! Here's what to do:

    Pick your Python file (e.g., main.py).

    Select "One File".

    Check "Window Based" so no CMD window pops up.

    Click "Convert .py to .exe".

    After some loading magic, it’ll spit out your .exe in the dist folder.

✅ Done!

Run your .exe and enjoy the GUI life.
No terminals, no drama—just click and go.

If anything explodes, it's probably your fault. But hey, that’s the risk you take when using the "If You Want to Die" install route.
