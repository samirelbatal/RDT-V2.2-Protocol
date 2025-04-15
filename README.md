
# RDTv2.2 – Reliable Data Transfer Protocol (Stop-and-Wait)

A Python implementation of the Reliable Data Transfer protocol RDTv2.2, simulating a communication channel with possible packet corruption or ACK corruption using a stop-and-wait approach (alternating bit protocol). The project emulates a real sender-receiver model with debugging capabilities.

## 📌 Features

- Implements RDTv2.2 protocol
- Supports packet corruption and ACK corruption simulation
- Uses alternating bit (0 or 1) sequence number
- Print-color-coded logs for clear sender/receiver actions
- Adjustable network reliability and round-trip delay
- Easily extendable to RDT3.0

---

## 📁 Project Structure

```
│
├── main.py              # Entry point to run the RDT simulation
├── sender.py            # Sender logic for RDTv2.2
├── receiver.py          # Receiver logic for RDTv2.2
├── network.py           # Simulates the unreliable network layer
└── README.md            # You are here
```

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then, open your terminal and navigate to the project directory.

### Example command:

```bash
python main.py msg=HELLO rel=0.8 delay=1 debug=1 pkt=1 ack=1
```

---

## 🔧 Parameters

| Parameter   | Type    | Description                                                                 |
|-------------|---------|-----------------------------------------------------------------------------|
| `msg`       | string  | The message to send (e.g., `HELLO`)                                         |
| `rel`       | float   | Network reliability (between `0.0` and `1.0`)                               |
| `delay`     | int     | Round-trip delay in seconds                                                 |
| `debug`     | 0 or 1  | Enable (1) or disable (0) debugging features like corruption logs           |
| `pkt`       | 0 or 1  | Enable (1) or disable (0) packet corruption (only effective if `debug=1`)   |
| `ack`       | 0 or 1  | Enable (1) or disable (0) ack corruption (only effective if `debug=1`)      |

---

## 📦 Sample Output

With `debug=1`, the sender and receiver logs look like this:

```
Sender: sending {'sequence_number': '0', 'data': 'H', 'checksum': 72}
Receiver: received {'sequence_number': '0', 'data': 'H', 'checksum': 72}
Receiver: reply with {'ack': '0', 'checksum': 48}
Sender: received {'ack': '0', 'checksum': 48}
Letter H is sent and received correctly
...
```

---

## 💡 Bonus Ideas (RDTv3.0)

You can extend this project to support **RDTv3.0** by:

- Adding **timeouts** and **retransmission** for packet loss
- Simulating **packet drop** in `network.py` (e.g., skip delivery)
- Using Python's `threading.Timer` or `time.monotonic()` for timeouts

---

## 📚 Educational Use

This project is intended for educational purposes (e.g., GUC Computer Networks course) to understand core concepts of:

- Reliable transmission
- Stop-and-wait protocol
- Handling data corruption in transmission

---

## 🧑‍💻 Authors

- Samir ElBatal (samirelbatal0@gmail.com)  
- GUC Student – Fall 2023 – Tutorial 61

---

## 📄 License

This project is for educational use only. Please do not distribute or reuse without permission.

