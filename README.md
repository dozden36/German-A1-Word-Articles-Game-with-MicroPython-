# German A1 Word Articles Game with MicroPython 🇩🇪

[![MicroPython](https://img.shields.io/badge/MicroPython-Ready-2b5b84?style=flat&logo=python&logoColor=white)](https://micropython.org/)
[![Hardware](https://img.shields.io/badge/Hardware-RP2040--Zero-red?style=flat)](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html)

A DIY interactive language learning device built with an **RP2040-Zero** and a **0.96" IPS display** to practice German A1 articles (*der, die, das*). 

Written in **MicroPython**, it displays random German words on the screen and uses three dedicated push buttons with RGB LED feedback to indicate correct or wrong answers immediately.

---

## 📌 Features

- **Interactive Learning:** Practice German A1 vocabulary and articles (*Der / Die / Das*) hands-on.
- **Visual Feedback:** Instant RGB LED notifications for correct and incorrect answers.
- **Compact Hardware:** Powered by a tiny RP2040-Zero microcontroller & crisp 0.96" IPS LCD (ST7735).
- **Customizable Vocabulary:** Easily add or edit German words directly inside `main.py`.

---

## 🔌 Complete Hardware Wiring Guide

To build this project, connect your **ST7735 Display** and **3 Push Buttons** to the **RP2040-Zero** according to the tables and diagrams below.

### 🖥️ 1. Display Connections (0.96" IPS - ST7735)

| Display Pin | RP2040-Zero Pin | Description |
| :--- | :--- | :--- |
| **VCC** | `3V3` | 3.3V Power Supply |
| **GND** | `GND` | Ground |
| **SCL** | `GPIO 2` | SPI Clock |
| **SDA** | `GPIO 3` | SPI MOSI |
| **RES** | `GPIO 5` | Reset |
| **DC** | `GPIO 4` | Data / Command |
| **CS** | `GPIO 1` | Chip Select |
| **BLK** | `GPIO 6` | Backlight Control |


| **DER** | `GPIO 14`
| **DIE** | `GPIO 27`
| **DAS** | `GPIO 26`

