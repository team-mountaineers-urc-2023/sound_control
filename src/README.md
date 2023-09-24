# Installation

`pip install py-espeak-ng`
`sudo pip3 install py-espeak-ng`

Run the above with sudo if you want to use this is a systemd service

Copy the executables to /usr/bin

Copy the systemd service files to /etc/systemd/system/


# Make pulseaudio run in system mode
This is necessary for reasons I'm too lazy to explain right now.

```
useradd -d /var/run/pulse -s /usr/bin/nologin -G audio pulse

groupadd pulse-access

usermod -aG pulse-access root
```
Then copy the `pulseaudio.service` file to `/etc/systemd/system`

```
systemctl --global mask pulseaudio.socket
sudo systemctl enable --now pulseaudio
```
