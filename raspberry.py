import RPi.GPIO as GPIO #ライブラリの導入
import time

# PIN番号の定義(名前をつける)
CONTROL_PIN = 18

def setup():
    """② 初期設定"""
    GPIO.setmode(GPIO.BCM)        # BCM（役割別）番号で指定
    GPIO.setup(CONTROL_PIN, GPIO.OUT) # 18番ピンを出力用に設定
    print("セットアップ完了。制御を開始します...")

def main_loop():
    """③ メインの制御ロジック"""
    while True:
        # 例：1秒おきにON/OFFを繰り返す（Lチカなど）
        GPIO.output(CONTROL_PIN, GPIO.HIGH) # ONにする
        print("機器を稼働中...")
        time.sleep(1.0)
        
        GPIO.output(CONTROL_PIN, GPIO.LOW)  # OFFにする
        print("機器を停止中...")
        time.sleep(1.0)
