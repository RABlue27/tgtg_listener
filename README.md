# TGTG Client - README

## Overview

This README provides a brief overview of a Python script that uses the `tgtg` library to interact with the "Too Good To Go" (TGTG) API. The script retrieves information about available food items from nearby restaurants and continuously prints this information to the console.

## Requirements

Before running the script, make sure you have the following dependencies installed:

- Python (3.x recommended)
- The `tgtg` library
- The `dotenv` library

You can install the required libraries using `pip`:

```bash
pip install tgtg dotenv
```

## Configuration

To use this script, you need to set up environment variables in a `.env` file in the same directory as the script. The `.env` file should contain the following variables:

- `access_token`: Your TGTG access token
- `refresh_token`: Your TGTG refresh token
- `user_id`: Your TGTG user ID
- `cookie`: Your TGTG cookie

Make sure to obtain these credentials by registering and logging in to the TGTG platform.

## Usage

1. Create a `.env` file in the same directory as the script and populate it with your TGTG credentials as mentioned in the "Configuration" section.

2. Run the script using the following command:

```bash
python your_script_name.py
```

The script will continuously fetch information about available food items from nearby restaurants and print the item ID, description, and name to the console every 30 minutes (1800 seconds).

## Note

- Make sure your system is connected to the internet while running the script.

- Be cautious with your TGTG credentials, as they are sensitive information.

- This script is intended for educational purposes and should be used responsibly. Avoid violating TGTG's terms of service.
