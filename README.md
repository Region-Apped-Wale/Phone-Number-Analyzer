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
1. **Run the Program**: 
   - Simply double-click the `start.bat` file (Windows) or execute the Python script directly (`python phone_analyzer.py` for other operating systems). 
   - The program will start by showing a menu of countries.
  
2. **Select a Country**: 
   - Choose a country by number (e.g., `1` for United States, `2` for Canada, etc.). This sets the default country code for your phone number analysis.
  
3. **Enter a Phone Number**: 
   - Enter the phone number you want to analyze, using the correct format (e.g., `+1XXXXXXXXXX` for the US).
   
4. **Analyze the Number**: 
   - The program will check if the phone number is valid. 
   - If valid, it will provide detailed information including:
     - **Location/City**: Geographical location of the phone number.
     - **Carrier**: Service provider for the phone number.
     - **Time Zone(s)**: Time zone(s) associated with the number.
     - **Phone Number Type**: Whether it's a mobile, fixed-line, toll-free, etc.
     - **Number Formatting**: Shows the phone number in national, international, and E.164 formats.

5. **Reanalyze or Exit**: 
   - After displaying the analysis results, you can choose to analyze another number or exit the program.

## Installation & Requirements
### Prerequisites
- **Python 3.0 or higher** is required. Make sure to install Python from [here](https://www.python.org/downloads/).
- Install the required dependencies using `pip`:

```bash
pip install phonenumbers
