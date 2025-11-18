import pandas as pd
from fpdf import FPDF


df_hotels = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_card_security = pd.read_csv("card_security.csv", dtype=str)


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

    def generate_pdf(self, text):
        pdf = FPDF(orientation="P", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")
        # border=1
        pdf.cell(w=0, h=10, txt="Reservation Ticket", align="C", ln=1)
        pdf.set_font(family="Times", size=12)
        pdf.multi_cell(w=0, h=10, txt=text)
        pdf.output(f"{self.customer_name}_reservation.pdf")


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


class SecureCreditCard(CreditCard):

    def authencate(self, given_password):
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password:
            if password == given_password:
                return True
            else:
                return False
        else:
            print(f"No data for card {self.number} in database.")
