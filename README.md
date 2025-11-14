# Phone Number Analyzer V1.0.1

![Phone Number Analyzer Banner](https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Phone_icon_%28black%29.svg/1024px-Phone_icon_%28black%29.svg.png) <!-- Example Random Image -->

## Overview
This Python project allows users to analyze phone numbers by validating them and retrieving detailed information such as geographic location, carrier, time zone, and number type. It uses the `phonenumbers` library to parse and validate phone numbers from various countries. The script provides a command-line interface (CLI) to make it easy to interact with the tool.

## Key Features
- **Country Selection**: Choose a country from a predefined list based on country code.
- **Phone Number Validation**: Validate if the provided phone number is correct and in the proper format.
- **Geographic & Carrier Information**: Retrieve details about the phone number's location, carrier, and time zone.
- **Number Type Classification**: Classifies the number as mobile, fixed-line, toll-free, etc.
- **Standard Formats**: Display the phone number in different formats: National, International, and E.164.

## How It Works
1. Select a country by its associated number.
2. Enter a phone number for validation and analysis.
3. The script will validate the number and show:
   - **Location** (country or city),
   - **Carrier** (service provider),
   - **Time Zone(s)**, 
   - **Phone Number Type** (e.g., mobile, toll-free),
   - **Formatted Numbers** (National, International, and E.164).

4. Optionally, analyze more numbers or exit the program.

## Installation & Requirements
### Prerequisites
- **Python 3.0 or higher** is required.
- Install the required dependencies using `pip`:

```bash
pip install phonenumbers
