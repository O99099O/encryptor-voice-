#!/usr/bin/env python3
# ==================== BY POLOSS ====================
# Encoder & Decoder Audio Bit-Frequency
# 100% CLEAN – NO ERROR – NO BUG – NO WARNING

import wave
import struct
import math
import sys

# ============= KONVERSI TEXT → BINARY ===============
def text_to_bits(txt):
    return ''.join(format(ord(c), '08b') for c in txt)

# ============= AUDIO BUILDER (BIT → TONE) ===============
def bits_to_audio(bits, outfile, hz1, hz0):
    sample_rate = 44100
    duration = 0.1
    audio = []

    for bit in bits:
        freq = hz1 if bit == '1' else hz0
        for n in range(int(sample_rate * duration)):
            sample = int(32767 * math.sin(2 * math.pi * freq * (n / sample_rate)))
            audio.append(sample)

    with wave.open(outfile, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        for s in audio:
            f.writeframes(struct.pack('<h', s))

# ============= AUDIO → BIT (TONE READER) ===============
def audio_to_bits(infile, hz1, hz0):
    with wave.open(infile, 'rb') as f:
        frame_rate = f.getframerate()
        frames = f.readframes(f.getnframes())

    samples = struct.iter_unpack('<h', frames)
    samples = [s[0] for s in samples]

    chunk = int(frame_rate * 0.1)
    bits = ''

    for i in range(0, len(samples), chunk):
        part = samples[i:i+chunk]
        if len(part) < chunk:
            break

        # FFT kecil manual (dominant freq)
        peak = 0
        peak_val = 0
        for freq in (hz1, hz0):
            acc = 0
            for n in range(len(part)):
                acc += part[n] * math.sin(2 * math.pi * freq * (n / frame_rate))
            if acc > peak_val:
                peak_val = acc
                peak = freq

        bits += '1' if peak == hz1 else '0'
    return bits

# ============= BINARY → TEXT ===============
def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

# ==================== MAIN ====================
print("1 = Encode")
print("2 = Decode")
mode = input("Pilih mode: ")

if mode == '1':
    msg = input("Tulis pesan yang mau di-encode: ")
    input("Tekan CTRL + A untuk lanjut...")
    out = input("Nama output WAV (contoh: hasil.wav): ")

    hz1 = int(input("Frekuensi untuk bit 1 (Hz): "))
    hz0 = int(input("Frekuensi untuk bit 0 (Hz): "))

    bits = text_to_bits(msg)
    bits_to_audio(bits, out, hz1, hz0)
    print("Selesai encode!")

elif mode == '2':
    infile = input("Masukkan file WAV: ")

    hz1 = int(input("Frekuensi bit 1 (Hz): "))
    hz0 = int(input("Frekuensi bit 0 (Hz): "))

    bits = audio_to_bits(infile, hz1, hz0)
    text = bits_to_text(bits)
    print("Decoded:", text)

else:
    print("Mode tidak valid.")
