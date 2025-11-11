"""
- користувач може переглянути список готелів,
- користувач може забронювати готель,
- користувач може отримати підтвердження бронювання або квиток(ticket),
як би ви це не називали, після того, як він забронював готель.
"""

# Hotel, User, ReservationTicket
# class User:
# def view_hotels(self):
#     pass

import pandas as pd


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id

    def booking(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj

    def generate(self):
        pass


def main():
    df = pd.read_csv("hotels.csv")
    print(df)

    hotel_id = input("Enter the ID of the hotel")
    hotel = Hotel(hotel_id=hotel_id)

    if hotel.available():
        hotel.booking()
        customer_name = input("Enter you name: ")
        reservation_ticket = ReservationTicket(
            customer_name=customer_name,
            hotel_obj=hotel,
        )
        reservation_ticket.generate()
    else:
        print("Sorry, the hotel is not available for booking.")


if __name__ == "__main__":
    # перевірка чи запусткається безпосередньо файл main.py
    # якщо ні - то функція main() не буде викликана
    main()
