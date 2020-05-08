# Power Off
Allow yourself to focus on powering down while your mobile device powers down on automatically. With this app, you
can give your device a set amount of time until it shuts down allowing you to listen to music, meditate, or read without
worrying about falling asleep and having your phone wasting battery all night (or all day).

### Requirements
Assuming you have a virtual environment for this project:
0. `pip install -r requirements.txt`
1. `brew install pkg-config`
2. `brew install glib`
3. Download `dbus-python` source code: <http://dbus.freedesktop.org/releases/dbus-python/>
4. `cd ~/Downloads/dbus-python-1.2.16`
5. `PYTHON=python3.X ./configure --prefix=/tmp/dbus-python`
6. `make`
7. `make install`
8. `cp -r /usr/local/lib/python3.7/site-packages/dbus ~/<path-to-project>/venv/lib/python3.7/site-packages`
9. `cp -r /usr/local/lib/python3.7/site-packages/_dbus_*.so ~/<path-to-project>/ven/lib/python3.7/site-packages`
10. `pip install buildozer`
11. `pip install https://github.com/kivy/buildozer/archive/master.zip`