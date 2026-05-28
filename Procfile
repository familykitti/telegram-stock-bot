import os
import requests
import yfinance as yf
from datetime import datetime

# 1. ดึงค่าความลับ (Secrets) ที่คุณตั้งไว้ใน GitHub
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

def send_telegram_message(message):
    """ฟังก์ชันสำหรับส่งข้อความไปยัง Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown" # ทำให้ตัวหนา/เอียงได้
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("ส่งข้อความเข้า Telegram สำเร็จ!")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการส่งข้อความ: {e}")

def get_stock_data_and_alert():
    """ฟังก์ชันดึงราคาหุ้นและจัดรูปแบบข้อความ"""
    # กำหนดชื่อหุ้นที่ต้องการดึงข้อมูล (เปลี่ยนได้ตามต้องการ)
    symbol = "์NVDA" 
    
    print(f"กำลังดึงข้อมูลหุ้น {symbol}...")
    stock = yf.Ticker(symbol)
    
    # ดึงข้อมูลราคาวันล่าสุด
    todays_data = stock.history(period='1d')
    
    if not todays_data.empty:
        # ดึงราคาปิด (Close price) ของวันล่าสุด
        current_price = todays_data['Close'].iloc
        
        # จัดรูปแบบวันที่ปัจจุบัน
        today_date = datetime.now().strftime("%Y-%m-%d")
        
        # 2. จัดระเบียบข้อความที่จะส่งเข้า Telegram
        msg = (
            f"📈 *อัปเดตราคาหุ้นก่อนตลาดเปิด* ({today_date})\n\n"
            f"🔹 *หลักทรัพย์:* {symbol}\n"
            f"💲 *ราคาล่าสุด:* ${current_price:.2f}\n\n"
            f"ขอให้โชคดีในการลงทุนครับ! 🚀"
        )
        
        # เรียกใช้ฟังก์ชันส่งข้อความ
        send_telegram_message(msg)
    else:
        error_msg = f"⚠️ ไม่สามารถดึงข้อมูลของ {symbol} ได้ในขณะนี้"
        print(error_msg)
        send_telegram_message(error_msg)

if __name__ == "__main__":
    # ตรวจสอบว่าได้ตั้งค่า Token และ Chat ID หรือยัง
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("ข้อผิดพลาด: ไม่พบ TELEGRAM_TOKEN หรือ CHAT_ID ในระบบ")
    else:
        get_stock_data_and_alert()
