import phonenumbers
from phonenumbers import geocoder, timezone, carrier, is_valid_number, number_type
import os

COUNTRIES = {
    "1": ("United States", "US"), "2": ("Canada", "CA"), "3": ("United Kingdom", "GB"),
    "4": ("Australia", "AU"), "5": ("Germany", "DE"), "6": ("France", "FR"),
    "7": ("Turkey", "TR"), "8": ("India", "IN"), "9": ("China", "CN"),
    "10": ("Japan", "JP"), "11": ("Brazil", "BR"), "12": ("Russia", "RU"),
    "13": ("Mexico", "MX"), "14": ("Indonesia", "ID"), "15": ("Pakistan", "PK"),
    "16": ("Nigeria", "NG"), "17": ("Bangladesh", "BD"), "18": ("Egypt", "EG"),
    "19": ("Vietnam", "VN"), "20": ("Iran", "IR"), "21": ("South Korea", "KR"),
    "22": ("Spain", "ES"), "23": ("Italy", "IT"), "24": ("South Africa", "ZA"),
    "25": ("Argentina", "AR"),
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("=" * 65)
    print("       📞   P H O N E   N U M B E R   A N A L Y Z E R V1.0.1   📞")
    print("=" * 65)
    print()

def display_country_menu():
    print("--- Please Select a Country ---")
    items = list(COUNTRIES.items())
    max_len = len(items)
    col_len = (max_len + 2) // 3
    for i in range(col_len):
        line = ""
        for j in range(3):
            idx = i + j * col_len
            if idx < max_len:
                key, (name, code) = items[idx]
                line += f"{key:>2}. {name:<20}"
        print(line)
    print("-" * 60)

def display_phone_details(number_str, country_code, lang="en"):
    print("\n" + "=" * 60)
    print(f"Analyzing Number: {number_str} (Default Region: {country_code})")
    print("=" * 60)

    try:
        parsed_number = phonenumbers.parse(number_str, country_code)
    except phonenumbers.NumberParseException as e:
        print(f"[ERROR] Number parsing failed: {e}")
        print("Please ensure the number is in a valid national or international format.")
        return

    if not is_valid_number(parsed_number):
        print("[RESULT] INVALID PHONE NUMBER")
        print("Explanation: The number format does not match a valid phone number pattern.")
        return

    print("[RESULT] VALID PHONE NUMBER")
    print("\n--- Geographic & Carrier Information ---")

    country_cc = parsed_number.country_code
    print(f"Country Code (CC): +{country_cc}")

    location = geocoder.description_for_number(parsed_number, lang)
    print(f"Location/City: {location or 'Unknown'}")

    service_provider = carrier.name_for_number(parsed_number, lang)
    print(f"Service Provider: {service_provider or 'Unknown'}")

    time_zones = timezone.time_zones_for_number(parsed_number)
    time_zone = time_zones[0] if time_zones else "Unknown"
    print(f"Time Zone(s): {time_zone}")

    print("\n--- Number Type & Formatting ---")

    num_type = number_type(parsed_number)
    type_map = {
        phonenumbers.PhoneNumberType.MOBILE: "Mobile",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-Free",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        phonenumbers.PhoneNumberType.VOIP: "VoIP",
    }
    type_str = type_map.get(num_type, "Unknown")
    print(f"Number Type: {type_str}")

    print("\n--- Standard Formats ---")
    national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
    print(f"National Format: {national_format}")

    international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(f"International Format: {international_format}")

    e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    print(f"E.164 Format (for APIs): {e164_format}")

    print("-" * 60)

def main():
    while True:
        clear_screen()
        print_banner()
        display_country_menu()

        choice = input("Select a country by number (or 'q' to quit): ").strip()

        if choice.lower() == 'q':
            print("\nExiting application. Goodbye!")
            break

        if choice not in COUNTRIES:
            input("\n[ERROR] Invalid selection. Press Enter to try again.")
            continue

        country_name, country_code = COUNTRIES[choice]
        print(f"\nYou selected: {country_name}")

        number_input = input(f"Enter the phone number for '{country_name}': ").strip()

        if not number_input:
            input("\n[ERROR] You did not enter a number. Press Enter to try again.")
            continue

        display_phone_details(number_input, country_code)

        while True:
            another = input("\nAnalyze another number? (y/n): ").strip().lower()
            if another in ['y', 'n']:
                break
            print("[ERROR] Invalid input. Please enter 'y' (yes) or 'n' (no).")

        if another == 'n':
            print("\nExiting application. Goodbye!")
            break

if __name__ == "__main__":
    main()
