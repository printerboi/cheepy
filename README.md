# 🐥 Cheepy

*A tiny love-letter machine built with Raspberry Pi Zero + Inky pHAT*

Cheepy is a charming client–server application designed to send digital *love letters* to your favorite person and display them in a cozy, physical way. Using a Raspberry Pi Zero paired with an Inky pHAT e-ink display, Cheepy turns heartfelt messages into a delightful, glanceable, always-there reminder of affection.

---

## 💡 What Cheepy Does

* 📬 **Send love letters** from any device through a simple client API
* 🖥️ **Display messages** beautifully on a Raspberry Pi Zero with an Inky pHAT
* 🔄 **Auto-refresh** when new letters arrive
* 💛 **Create a physical, ambient connection** between you and someone special

Cheepy is built to be minimal, cute, and emotionally expressive

---

## 🏗️ Architecture Overview

Cheepy consists of two main parts:

### **1. Server (Cheepy-Server)**

* Receives love letters via HTTP/REST (or any interface you define)
* Stores recent messages
* Notifies or provides endpoints for the client to fetch updates

### **2. Client (Cheepy-Pi)**

* Runs on a Raspberry Pi Zero
* Periodically queries the server for the latest letter
* Renders the message on the Inky pHAT display
* Handles text wrapping & display formatting

```
[Your Phone / App] → [Cheepy Server] → [Cheepy Pi Zero] → [Inky pHAT]
```

---

## 🧰 Hardware Requirements

* Raspberry Pi Zero or Zero W
* Pimoroni Inky pHAT (Black/White/Red or Black/White/Yellow)
* MicroSD card
* Wi-Fi network
* Python 3.x

---

## 🛠️ Installation

### **On the Raspberry Pi (Client)**

```bash
git clone https://github.com/yourname/cheepy-client.git
cd cheepy-client
pip3 install -r requirements.txt
```

Set your environment variables

```bash
...
```

Run the client:

```bash
...
```

---

### **On the Server**

Set your environment variables

```bash
...
```

Launch

```bash
...
```

---

## 📤 Sending a Love Letter

Once the server is running, sending a letter is as easy as:

```bash
curl -X POST https://your-cheepy-server/cheep \
     -u "user:password" \
     -H "Content-Type: application/json" \
     -d '{
           "sender": "alice",
           "receiver": "bob",
           "content": "Thinking of you 💛",
           "is_image": false
         }'

```

Or using your own UI/app, if you build one.

---

## 🎨 Display Behavior

* The Pi checks for new messages every X seconds
* When a new letter arrives, the screen updates
* E-ink means the message stays visible even when powered off

---

## 🚀 Roadmap Ideas

* Web dashboard for composing letters
* Multiple themes/fonts for the display
* Support for drawings or tiny pixel art
* Message queue/history on the client

---

## 🤝 Contributing

Pull requests, suggestions, and ❤️ are always welcome.

---
