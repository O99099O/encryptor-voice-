# 🔊 Audio Bit-Frequency Encoder & Decoder

**BY POLOSS**

Encoder–Decoder berbasis audio frekuensi yang mengubah **plain text menjadi gelombang suara (WAV)** dan dapat **mengembalikannya ke teks** secara presisi menggunakan analisa frekuensi.
Dibangun tanpa error, tanpa bug, dan 100% stabil.


## ✨ Fitur

* Konversi teks → biner → audio frekuensi.
* Decode audio → biner → teks.
* Frekuensi bit **1** dan **0** dapat diatur bebas.
* Output audio `.wav` berkualitas tinggi (44.1 kHz).
* CLI sederhana, cepat, dan responsif.
* Tidak menggunakan dummy/simulasi — *full real audio processing*.

---

## 📥 Download

**Download script:**
👉 [https://github.com/O99099O/encryptor-voice-/blob/main/voice.py](https://github.com/O99099O/encryptor-voice-/blob/main/voice.py)

**Clone repository:**

```bash
git clone https://github.com/O99099O/encryptor-voice-.git
```

---

## 🛠 Instalasi

Tidak diperlukan library tambahan.

Pastikan Python 3 sudah terinstall:

```bash
python3 --version
```

---

## ▶️ Cara Menjalankan

### **1. Encode Teks → Audio**

```bash
python3 voice.py
```

Pilih:

```
1 = Encode
```

Input yang diperlukan:

* Pesan teks
* Nama file WAV output
* Frekuensi bit 1 (Hz)
* Frekuensi bit 0 (Hz)

Script akan menghasilkan file audio berisi bit frekuensi.

---

### **2. Decode Audio → Teks**

Pilih:

```
2 = Decode
```

Input:

* File WAV
* Frekuensi bit 1 (Hz)
* Frekuensi bit 0 (Hz)

Output berupa teks plaintext hasil decode.

---

## 📂 Struktur Script

* **text_to_bits** — konversi teks ke biner.
* **bits_to_audio** — menghasilkan audio dari bit.
* **audio_to_bits** — membaca gelombang & mengekstrak bit.
* **bits_to_text** — mengembalikan biner ke teks.
* **Main CLI** — antarmuka encoder/decode.

---

## 🔰 Watermark

Script memiliki watermark resmi:
**BY POLOSS**

---

## 🔗 Repository

📌 [https://github.com/O99099O/encryptor-voice-](https://github.com/O99099O/encryptor-voice-)

---
