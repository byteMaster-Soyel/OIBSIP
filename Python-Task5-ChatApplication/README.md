# 💬 Chat Application

A real-time Chat Application developed using **Python**, **Socket Programming**, and **Threading**. The application follows a **client-server architecture** that allows multiple clients to connect to a server and exchange messages in real time.

The application provides a simple **Tkinter GUI** for sending and receiving messages, while Python sockets handle the network communication between the clients and the server.

---

## 📌 Features

* 💬 Real-Time Messaging
* 👥 Two-User Communication
* 🖥️ Client-Server Architecture
* ⏰ Timestamped Messages
* 👤 Username Support
* 🔄 Bidirectional Communication
* 🔌 Graceful Disconnection Handling
* 🌐 Localhost Support
* 🧵 Thread-Based Communication
* 🪟 Tkinter Graphical User Interface
* 📡 TCP Socket Communication
* 🚪 Quit/Disconnect Support
* ⚠️ Connection Error Handling
* 🛡️ Basic Connection Management

---

## 🛠️ Technologies Used

* Python 3
* Socket
* Threading
* Tkinter
* Argparse
* Sys
* OS

---

## 📂 Project Structure

```text
Python-Task5-ChatApplication/
│
├── server.py
├── client.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
    ├── server.png
    ├── client.png
    └── chat.png
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/byteMaster-Soyel/OIBSIP.git
```

### 2. Go to the project folder

```bash
cd OIBSIP/Python-Task5-ChatApplication
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Start the server

Open a terminal and run:

```bash
python server.py 127.0.0.1
```

The server should display:

```text
Listening at ('127.0.0.1', 1060)
```

### 5. Start the client

Open another terminal and run:

```bash
python client.py 127.0.0.1
```

Enter your username when prompted.

To connect another user, open another terminal and run:

```bash
python client.py 127.0.0.1
```

Enter a different username.

---

## 💬 Chat Usage

After connecting to the server, users can communicate with each other in real time.

Example:

```text
Your name: Soyel

Welcome, Soyel! Getting ready to send and receive messages...

Soyel: Hello!
Alice: Hi Soyel!
Soyel: How are you?
Alice: I am fine.
```

Messages are transferred through the server using TCP socket communication.

---

## 🖥️ Server

The `server.py` file is responsible for:

* Listening for incoming client connections
* Accepting client connections
* Creating a separate thread for each client
* Receiving messages from clients
* Broadcasting messages to other connected clients
* Managing active connections
* Handling client disconnections
* Closing all connections when the server is stopped

Start the server using:

```bash
python server.py 127.0.0.1
```

### Stop the Server

Type:

```text
q
```

in the server terminal to close the server and disconnect the connected clients.

---

## 👤 Client

The `client.py` file is responsible for:

* Connecting to the chat server
* Taking the user's username
* Sending messages
* Receiving messages
* Displaying messages in the Tkinter GUI
* Managing sending and receiving threads
* Handling disconnections
* Allowing users to leave the chat

Start the client using:

```bash
python client.py 127.0.0.1
```

---

## 🧵 Threading

The application uses Python's **threading** module to allow sending and receiving messages simultaneously.

The client uses separate threads for:

* 📤 Sending messages
* 📥 Receiving messages

The server also creates a separate thread for each connected client.

This allows communication to continue without blocking other users.

---

## 🌐 Socket Communication

The application uses TCP sockets with:

```python
socket.AF_INET
socket.SOCK_STREAM
```

The default server port is:

```text
1060
```

The default local server address is:

```text
127.0.0.1
```

The communication flow is:

```text
Client 1
   │
   │ Message
   ▼
Server
   │
   │ Broadcast
   ▼
Client 2
```

---

## 📸 Screenshots

### 🖥️ Server

Add your server screenshot here:

![Server](screenshots/server.png)

### 💬 Chat Window

Add your chat application screenshot here:

![Chat Window](screenshots/chat.png)

### 👥 Multiple Clients

Add your multiple-client screenshot here:

![Multiple Clients](screenshots/client.png)

---

## ⚙️ Requirements

Make sure **Python 3** is installed on your computer.

The project mainly uses Python's built-in modules:

```text
socket
threading
argparse
tkinter
sys
os
```

No external Python package is required for the current implementation.

You can install the project requirements using:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Notes

* 🌐 The current application is designed to run on `localhost`.
* 🖥️ The server must be running before starting the client.
* 🔢 The default TCP port is `1060`.
* 👥 Multiple clients can connect to the server.
* 🧵 Threading is used for simultaneous communication.
* 🪟 Tkinter is used for the client GUI.
* 🔌 Closing a client connection is handled by the server.
* ⚠️ The application does not provide end-to-end encryption.
* 🔐 Messages are transmitted through the server and are not encrypted by the application.
* 💾 The current version does not permanently store chat messages.
* 🗄️ No database is used in the current implementation.
* 🌍 For communication between different computers, the server's network IP address and appropriate firewall/network configuration would be required.

---

## 🔒 Security Transparency

This project is intended for learning and demonstrates basic socket-based communication.

Messages are sent using TCP sockets between the client and server. The current implementation does **not** provide:

* End-to-end encryption
* Password authentication
* User registration
* Database-backed message history
* TLS/SSL encryption

Therefore, this application should **not be considered suitable for sending sensitive or confidential information**.

---

## 🎯 Internship Task

This project was developed as part of the **Python Programming Internship** at **Oasis Infobyte**.

**Task:** Chat Application

**Task Number:** Task 5

---


## ⭐ Acknowledgement

I would like to thank **Oasis Infobyte** for providing this internship opportunity and allowing me to develop practical Python programming projects.

This project helped me gain practical experience with:

* Python Socket Programming
* Client-Server Architecture
* Multithreading
* TCP Communication
* Tkinter GUI Development
* Real-Time Message Exchange
* Network Connection Handling

---

## 📜 License

This project is created for educational and internship purposes.

---

## 👨‍💻 Author

**SK Soyel**

Python Programming Intern – Oasis Infobyte
