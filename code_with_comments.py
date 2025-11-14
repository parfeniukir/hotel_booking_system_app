# Імпортуємо бібліотеку pandas для роботи з даними у форматі таблиць (DataFrame).
# Вона часто використовується для читання та маніпулювання CSV, Excel та іншими файлами даних.
import pandas as pd

# -------------------------- Завантаження Даних --------------------------

# Читаємо файл "hotels.csv" і завантажуємо його вміст у DataFrame.
# dtype={"id": str} гарантує, що ID готелів інтерпретуються як рядки.
df_hotels = pd.read_csv("hotels.csv", dtype={"id": str})

# Читаємо файл "cards.csv" для валідації кредитних карток.
# dtype=str гарантує, що всі дані картки (номер, CVC тощо) читаються як рядки.
# .to_dict(orient="records") перетворює DataFrame на список словників.
# Кожен словник у цьому списку представляє одну дійсну картку у форматі ключ-значення.
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
# print(df_cards) # Коментар для налагодження: вивести список дійсних карток.

# ----------------------------- Клас Hotel -----------------------------


# Клас Hotel представляє окремий готель та його функціональність.
class Hotel:
    # Метод-конструктор.
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        # Знаходимо назву готелю в DataFrame df_hotels за його ID.
        self.name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

    # Метод для бронювання готелю.
    def booking(self):
        # Змінюємо статус доступності ("available") на "no" для вибраного готелю.
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        # Зберігаємо оновлений DataFrame назад у файл "hotels.csv" (без індексів).
        df_hotels.to_csv("hotels.csv", index=False)

    # Метод для перевірки доступності готелю.
    def available(self):
        """Check if the hotel is available"""  # Документуючий рядок.
        # Отримуємо значення колонки "available" для цього ID.
        available = df_hotels.loc[
            df_hotels["id"] == self.hotel_id, "available"
        ].squeeze()
        try:
            # Повертаємо True, якщо статус 'yes', і False, якщо 'no' (або інший).
            if available == "yes":
                return True
            else:
                return False
        except ValueError:
            # Обробка випадку, коли ID готелю не існує.
            print("This ID is not exist!")
            exit()


# -------------------------- Клас ReservationTicket --------------------------


# Клас для генерації підтвердження/квитка бронювання.
class ReservationTicket:
    # Конструктор приймає ім'я клієнта та об'єкт готелю.
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj

    # Метод для створення форматованого рядка квитка.
    def generate(self):
        # f-рядок для виведення даних бронювання.
        ticket = f"""
        Thank you for your reservation.
        Here is your booking data:
        Name: {self.customer_name}.
        Hotel name: {self.hotel_obj.name}
        """
        return ticket


# --------------------------- Клас CreditCard ---------------------------


# Новий клас для роботи з даними кредитної картки та її валідацією.
class CreditCard:
    # Конструктор приймає всі необхідні дані картки.
    def __init__(self, number, expiration_date, cvc_code, holder_name):
        self.number = number
        self.expiration_date = expiration_date
        self.cvc_code = cvc_code
        self.holder_name = holder_name

    # Метод для валідації картки проти завантаженого списку дійсних карток (df_cards).
    def validate(self):
        # Створюємо словник з даними поточної картки користувача для порівняння.
        card_data = {
            "number": self.number,
            "expiration": self.expiration_date,
            "cvc": self.cvc_code,
            "holder": self.holder_name,
        }
        # Перевіряємо, чи існує цей словник (тобто, чи збігаються всі дані) у списку df_cards.
        if card_data in df_cards:
            return True  # Валідація успішна.
        else:
            return False  # Валідація не пройдена.


# ------------------------------ Основна Логіка ------------------------------


# Головна функція, яка керує потоком виконання програми.
def main():
    # 1. Перегляд готелів: Виводимо список доступних готелів.
    print(df_hotels)

    # 2. Збір даних для оплати: Запитуємо дані кредитної картки.
    card_number = input("Enter your card number (4 digit): ")
    expiration_date = input("Enter your expiration date (MM/YY): ")
    cvc_code = input("Enter your CVC code: ")
    cardholder_name = input("Enter cardholder name: ")

    # Створюємо об'єкт CreditCard з введеними даними.
    credit_card = CreditCard(
        number=card_number,
        expiration_date=expiration_date,
        cvc_code=cvc_code,
        holder_name=cardholder_name,
    )

    # 3. Валідація картки.
    # validate will return True or False (Повертає True або False)
    if credit_card.validate():
        print("Your credit card was validated successfully!")

        # Якщо картка дійсна:
        # Запитуємо ID готелю.
        hotel_id = input("Enter the ID of the hotel: ")
        # Створюємо об'єкт Hotel.
        hotel = Hotel(hotel_id=hotel_id)

        # Перевіряємо доступність готелю.
        if hotel.available():
            # Якщо доступний:
            # Виконуємо бронювання (оновлюємо CSV-файл).
            hotel.booking()

            # Запитуємо ім'я клієнта (пропонуємо використати ім'я власника картки).
            customer_name = input(
                "Enter your name. If you want to use cardholder name as your name press ENTER: "
            )

            # Якщо користувач натиснув Enter (залишив поле порожнім), використовуємо ім'я власника картки.
            if not customer_name:
                customer_name = cardholder_name

            # Створюємо об'єкт ReservationTicket.
            reservation_ticket = ReservationTicket(
                customer_name=customer_name,
                hotel_obj=hotel,
            )
            # 4. Отримання підтвердження: Виводимо згенерований квиток.
            print(reservation_ticket.generate())
        else:
            # Готель недоступний.
            print("Sorry, the hotel is not available for booking.")
    else:
        # Валідація картки не пройшла. Бронювання неможливе.
        print("Invalid credit card data")


# Точка входу в програму.
if __name__ == "__main__":
    # перевірка чи запусткається безпосередньо файл main.py
    # якщо ні - то функція main() не буде викликана
    main()
