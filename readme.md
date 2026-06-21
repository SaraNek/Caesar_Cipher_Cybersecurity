# Caesar Cipher

A simple Python program that encrypts text using the classic Caesar cipher technique. This is my first project as I started learning cybersecurity.

## What is a Caesar Cipher?

The Caesar cipher is one of the oldest encryption techniques out there, supposedly used by Julius Caesar himself to send secret messages to his generals. The idea is simple: every letter in your message gets replaced by another letter, based on shifting the alphabet by a fixed number of positions (called the "key").

## How It Works

The program uses two versions of the alphabet:
- An original alphabet (A to Z)
- A shifted alphabet, where the letters are rotated anticlockwise based on the key

For example, with a key of 3, the shifted alphabet starts from D instead of A, and wraps back around to A, B, C at the end. Each letter in your input is then replaced by whatever letter sits in the same position in the shifted alphabet.

So "HELLO" with key 3 becomes "KHOOR".

## The Algorithm

Here's the basic logic of the code:

1. Make a normal alphabet array (A-Z).
2. Make a second array that's a shifted version of the alphabet, rotated anticlockwise by the key, wrapping back to A once you go past Z.
3. Go through every character in the input string one by one.
4. If it's a space, just keep it as a space.
5. Otherwise, find that character's position in the original alphabet, and pick the letter from the same position in the shifted alphabet — that's the encrypted letter.
6. Keep adding each encrypted letter to a final string as you go.
7. Print the final encrypted string at the end.

## Usage

Run the script in your terminal:

```bash
python Caesar_Cipher.py
```

It'll ask for:
- The string you want to encrypt
- A shift key (0-25)

## Example

```
Enter the string you want to encrypt: Hii this is Sara
Enter the shift key: 4
LMM XLMW MW WEVE
```
 
---
 
## Status
 
- ✅ Encryptor — working
- 🔜 Decryptor — coming soon (the reverse lookup: same logic, opposite direction)
---
 
## A Personal Note

This is my very first project in cybersecurity. Even though I'm still learning, I feel excited to have worked on and debugged this project myself. It's a small start, but I'm looking forward to building more projects like this. Next week, I'll be working on the decryptor part — so stay tuned for it!
