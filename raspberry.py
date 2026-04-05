import RPi.GPIO as GPIO #ライブラリの導入
import time

# PIN番号の定義(名前をつける)
CONTROL_PIN = 18

def setup():
    """② 初期設定"""
    GPIO.setmode(GPIO.BCM)        # BCM（役割別）番号で指定
    GPIO.setup(CONTROL_PIN, GPIO.OUT) # 18番ピンを出力用に設定
    print("セットアップ完了。制御を開始します...")
