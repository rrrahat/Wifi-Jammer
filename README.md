# 📡 WiFi Jammer - Educational Purpose Only

এটি শুধুমাত্র শিক্ষামূলক উদ্দেশ্যে তৈরি করা হয়েছে।  
এই স্ক্রিপ্ট WiFi ইন্টারফেসকে মনিটর মোডে এনে কিছু সময়ের জন্য Jam করে।

## ⚙️ Requirements:
- Termux / Linux
- aircrack-ng installed
- Root permission (sudo)

## 🛠 Installation:

```bash
pkg update && pkg install git python aircrack-ng -y
git clone https://github.com/rrrahat/Wifi-Jammer.git
cd Wifi-Jammer
python wifi_jammer.py
```

## 🧪 Usage:
- স্ক্রিপ্ট চালানোর সময় নিজের ইন্টারফেসের নাম (যেমন wlan0) দিতে হবে।
- স্ক্রিপ্ট স্বয়ংক্রিয়ভাবে ৫ মিনিট WiFi Jam করবে এবং বন্ধ হয়ে যাবে।

## ⚠️ Warning:
শুধুমাত্র নিজের ব্যক্তিগত পরীক্ষার জন্য ব্যবহার করুন।  
অন্যের নেটওয়ার্কে Jam করা বেআইনি।
