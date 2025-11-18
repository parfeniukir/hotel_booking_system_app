import pandas as pd

df_hotels = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

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


class CreditCard:
    def __init__(self, number, expiration_date, cvc_code, holder_name):
        self.number = number
        self.expiration_date = expiration_date
        self.cvc_code = cvc_code
        self.holder_name = holder_name

    def validate(self):
        card_data = {
            "number": self.number,
            "expiration": self.expiration_date,
            "cvc": self.cvc_code,
            "holder": self.holder_name,
        }
        if card_data in df_cards:
            return True
        else:
            return False
