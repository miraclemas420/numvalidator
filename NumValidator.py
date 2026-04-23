import requests
import time
from colorama import init, Fore, Style

init(autoreset=True)

API_KEY = "579288acbefff4a5e9c5e1e241952f22"
BASE_URL = "http://apilayer.net/api/validate"


def validate_phone_number(phone_number):
    params = {
        "access_key": API_KEY,
        "number": phone_number,
        "format": 1
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if not data.get("valid"):
            return {
                "number": phone_number,
                "valid": False
            }

        return {
            "number": data.get("international_format"),
            "valid": True,
            "country": data.get("country_name"),
            "location": data.get("location"),
            "line_type": data.get("line_type"),
            "carrier": data.get("carrier")
        }

    except Exception as e:
        return {
            "number": phone_number,
            "valid": False,
            "error": str(e)
        }


def main():
    print(Fore.CYAN + "\n📱 PHONE NUMBER VALIDATOR")
    print(Fore.CYAN + "Powered by NumVerify API\n")

    user_input = input(Fore.YELLOW + "👉 Enter number(s): ")

    numbers = [num.strip() for num in user_input.split(",") if num.strip()]

    print(Fore.GREEN + "\n🔍 Checking numbers...\n")

    for num in numbers:
        result = validate_phone_number(num)

        print(Fore.WHITE + "=" * 50)

        if not result.get("valid"):
            print(Fore.RED + f"❌ Invalid: {result['number']}")
            if "error" in result:
                print(Fore.RED + f"⚠️ Error: {result['error']}")
        else:
            print(Fore.GREEN + f"✅ Number: {result['number']}")
            print(Fore.CYAN + f"🌍 Country: {result.get('country')}")
            print(Fore.CYAN + f"📍 Location: {result.get('location')}")
            print(Fore.MAGENTA + f"📱 Line Type: {result.get('line_type')}")
            print(Fore.BLUE + f"📡 Carrier: {result.get('carrier')}")

        time.sleep(1)

    print(Fore.WHITE + "\n" + "=" * 50)
    print(Fore.LIGHTMAGENTA_EX + "🔥 Tool Developed by MAS")
    print(Fore.LIGHTMAGENTA_EX + "✔ Phone Validator System Complete")
    print(Fore.WHITE + "=" * 50 + "\n")


if __name__ == "__main__":
    main()