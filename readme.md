# Caesar Cipher

A simple Python program that encrypts and decrypts text using the classic Caesar cipher technique. This is my first project as I start learning cybersecurity.

## What is a Caesar Cipher?

The Caesar cipher is one of the oldest encryption techniques out there, supposedly used by Julius Caesar himself to send secret messages to his generals. The idea is simple: every letter in your message gets replaced by another letter, based on shifting the alphabet by a fixed number of positions (called the "key").

## How It Works

The program uses two versions of the alphabet:
- An original alphabet (A to Z)
- A shifted alphabet, where the letters are rotated anticlockwise based on the key

For example, with a key of 3, the shifted alphabet starts from D instead of A, and wraps back around to A, B, C at the end. Each letter in your input is then replaced by whatever letter sits in the same position in the shifted alphabet.

So "HELLO" with key 3 becomes "KHOOR".

## The Algorithm

### Encryption
1. Make a normal alphabet array (A-Z).
2. Make a second array that's a shifted version of the alphabet, rotated by the key.
3. Go through every character in the input string one by one.
4. If it's a space, keep it as a space.
5. Otherwise, find that character's position in the original alphabet, and pick the letter from the same position in the shifted alphabet — that's the encrypted letter.
6. Keep adding each encrypted letter to a final string as you go.
7. Print the final encrypted string.

### Decryption
1. Build the same shifted alphabet using the key.
2. Go through every character in the encrypted string.
3. If it's a space, keep it as a space.
4. Otherwise, find the character's position in the **shifted** alphabet, and pick the letter from the same position in the **original** alphabet — that's the decrypted letter.
5. Print the final decrypted string.

## Usage

Run the script in your terminal:

```bash
python Caesar_Cipher.py
```

It'll ask what you want to do:

```
What do you want to perform (Encryption/Decryption):
```

Then provide:
- The string you want to encrypt or decrypt
- A shift key (0-25)

## Examples

### Encryption
```
What do you want to perform (Encryption/Decryption): Encryption
Enter the data you want to Encrypt: Hii this is Sara
Enter the key: 4
LMM XLMW MW WEVE
```

### Decryption
```
What do you want to perform (Encryption/Decryption): Decryption
Enter the data you want to Decrypt: LMM XLMW MW WEVE
Enter the key: 4
HII THIS IS SARA
```

---

## Status

- ✅ Encryptor — working
- ✅ Decryptor — working (reverse lookup: searches in shifted alphabet, returns from original)

---

## A Personal Note

This is my very first project in cybersecurity. Even though I'm still learning, I feel excited to have built and debugged this project myself — both the encryptor and decryptor. It's a small start, but I'm looking forward to building more projects like this as I continue my cybersecurity journey!