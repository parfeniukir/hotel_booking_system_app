"""
- користувач може переглянути список готелів,
- користувач може забронювати готель,
- користувач може отримати підтвердження бронювання або квиток(ticket),
як би ви це не називали, після того, як він забронював готель.
- добавити можливість оплати картою, валідацію картки.
    І якщо карта дійснa - дозволити бронювати готель.
"""

from services import Hotel, SecureCreditCard, ReservationTicket, df_hotels


def main():
    print(df_hotels)

    card_number = input("Enter your card number (4 digit): ")
    expiration_date = input("Enter your expiration date (MM/YY): ")
    cvc_code = input("Enter your CVC code: ")
    cardholder_name = input("Enter cardholder name: ")

    secure_credit_card = SecureCreditCard(
        number=card_number,
        expiration_date=expiration_date,
        cvc_code=cvc_code,
        holder_name=cardholder_name,
    )
    # validate will return True or False
    if secure_credit_card.validate():
        print("Your credit card was validated successfully!")
        password = input("Enter your password: ")
        if secure_credit_card.authencate(password):
            hotel_id = input("Enter the ID of the hotel: ")
            hotel = Hotel(hotel_id=hotel_id)

            if hotel.available():
                hotel.booking()
                customer_name = input(
                    "Enter your name. If you want to use cardholder name as your name press ENTER: "
                )
                if not customer_name:
                    customer_name = cardholder_name
                reservation_ticket = ReservationTicket(
                    customer_name=customer_name,
                    hotel_obj=hotel,
                )
                text = reservation_ticket.generate()
                reservation_ticket.generate_pdf(text)
            else:
                print("Sorry, the hotel is not available for booking.")
        else:
            print("Invalid passwords")
    else:
        print("Invalid credit card data")


if __name__ == "__main__":
    # перевірка чи запусткається безпосередньо файл main.py
    # якщо ні - то функція main() не буде викликана

    # for testing
    # hotel = Hotel(hotel_id="134")
    # ticket = ReservationTicket(customer_name="Ivanna", hotel_obj=hotel)
    # text_for_pdf = ticket.generate()
    # ticket.generate_pdf(text_for_pdf)
    main()
