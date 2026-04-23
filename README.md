# 📱 Phone Number Validator (NumVerify API)

A simple yet powerful Python tool that validates phone numbers using the NumVerify API.  
It checks if a number is valid and returns useful information such as country, line type, and carrier.

Built with ❤️ by **MAS**

---

## 🚀 Features

- ✅ Validate multiple phone numbers at once  
- 📱 Detect line type (mobile, landline, VoIP, etc.)  
- 🌍 Get country and location information  
- 📡 Identify carrier/network provider   
- ⚡ Fast and lightweight CLI tool    

---

## 🔑 API Setup (IMPORTANT)

**Step 1**: Create a free account
Sign up here:  
https://numverify.com

**Step 2**: Get your API key
After signing up, you will receive a free API key from your dashboard.

**Step 3**: Add your API key to the code
Open `NumValidator.py` and locate:
Replace it with your actual API key:

API_KEY = "your_real_api_key_here"

---

📦 Installation
Install required dependencies:
pip install requests colorama

---

⚠️ Notes
Always use international format (with country code)
Free NumVerify accounts may have request limits
Some carrier or location data may be unavailable depending on region

```python
API_KEY = "YOUR_NUMVERIFY_API_KEY"
