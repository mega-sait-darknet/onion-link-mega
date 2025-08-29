# reminder.py
import time

def main():
    print("⏰ Простая напоминалка")
    print("—" * 40)
    print("Я напомню тебе через указанное время.")
    
    try:
        minutes = float(input("Через сколько минут напомнить? "))
        if minutes < 0:
            print("⚠️ Время не может быть отрицательным. Установлено 1 минута.")
            minutes = 1

        seconds = minutes * 60
        message = input("Какое напоминание? (по умолчанию: 'Пора передохнуть!') ")
        if not message:
            message = "Пора передохнуть!"

        print(f"\n✅ Напоминание установлено на {minutes} мин.")
        print("Чтобы отменить — нажми Ctrl+C")

        time.sleep(seconds)

        print("\n" + "🔔 НАПОМИНАНИЕ!")
        print("—" * 40)
        print(f"❗ {message}")
        print("—" * 40)
        
        # Простое "оживание" — мигаем сообщением (в терминале)
        for _ in range(3):
            time.sleep(0.5)
            print("❗❗❗ БУДЬ ВНИМАТЕЛЕН! ❗❗❗")
            time.sleep(0.5)

    except ValueError:
        print("❌ Пожалуйста, вводи число минут.")
    except KeyboardInterrupt:
        print("\n\n👋 Напоминание отменено. Пока!")

if __name__ == "__main__":
    main()
