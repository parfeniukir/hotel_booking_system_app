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

df_hotels = pd.read_csv("hotels.csv", dtype={"id": str})
# print(df_hotels)
# print(type(df_hotels))


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()
        # print("HOTEL NAME", self.name)

    def booking(self):
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        # фільтрація хотелю по ID і отримання значення колонки available, по цьому IDa
        available = df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze()
        try:
            if available == "yes":
                return True
            else:
                return False
        except ValueError:
            print("This ID is not exist!")
            exit()
        # print(available)
        # print(type(available))


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj

    def generate(self):
        ticket = f"""
        Thank you for your reservation.
        Here is your booking data:
        Name: {self.customer_name}.
        Hotel name: {self.hotel_obj.name}
        """
        return ticket


def main():
    print(df_hotels)

    hotel_id = input("Enter the ID of the hotel: ")
    hotel = Hotel(hotel_id=hotel_id)

    if hotel.available():
        hotel.booking()
        customer_name = input("Enter you name: ")
        reservation_ticket = ReservationTicket(
            customer_name=customer_name,
            hotel_obj=hotel,
        )
        print(reservation_ticket.generate())
    else:
        print("Sorry, the hotel is not available for booking.")


if __name__ == "__main__":
    # перевірка чи запусткається безпосередньо файл main.py
    # якщо ні - то функція main() не буде викликана
    main()
