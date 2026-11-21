# PassGuard v1.0 🔐

**PassGuard** is a beginner-friendly Python CLI tool that evaluates password strength based on length and character variety.

## Features

- Checks password length.
- Detects lowercase and uppercase letters.
- Checks for digits and special characters.
- Calculates a password strength score.
- Classifies passwords as Weak, Medium, or Strong.
- Provides recommendations to improve password strength.
- Uses `getpass` to hide password input while typing.

## Technologies Used

- Python 3
- `string` module
- `getpass` module

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/albertsec/PassGuard
   ```

2. Navigate to the project directory:

   ```bash
   cd PassGuard
   ```

3. Run the program:

   ```bash
   python passguard.py
   ```

4. Enter a sample password to check its strength.

## How It Works

PassGuard evaluates passwords using the following criteria:

- Length: up to 2 points.
- Lowercase letters: 1 point.
- Uppercase letters: 1 point.
- Digits: 1 point.
- Special characters: 1 point.

**Maximum score: 6 points.**

The result is classified as:

- Weak: 0–2 points.
- Medium: 3–4 points.
- Strong: 5–6 points.

## Ethical and Legal Notice

This project is designed for educational purposes and runs locally on your own machine.

Never scan, attack, or test systems that you do not own or have explicit permission to assess. Unauthorized security testing may be illegal.

**Important:** PassGuard provides a basic password-strength estimate. It does not verify whether passwords have been exposed in data breaches or guarantee password security.

## Project Status

Version 1.0 — Initial release.

Created as part of the SkillMe Cybersecurity Virtual Internship.