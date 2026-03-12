# Custom Exceptions
class FlightError(Exception):
    """Base exception for flight booking system."""
    pass


class SeatNotAvailableError(FlightError):
    """Raised when seats are not available."""
    pass


class InvalidPassengerDetailsError(FlightError):
    """Raised when passenger details are invalid."""
    pass


class PaymentFailedError(FlightError):
    """Raised when payment fails."""
    pass


# Flight Booking System
class FlightBookingSystem:

    def __init__(self):
        # Sample flight database
        self.flights = {
            "AI101": {"route": "Delhi -> Mumbai", "seats": 2, "price": 5000},
            "AI202": {"route": "Kolkata -> Bangalore", "seats": 5, "price": 6500},
            "AI303": {"route": "Chennai -> Hyderabad", "seats": 0, "price": 4000}
        }

        self.bookings = {}

    # Search flights
    def search_flights(self):
        print("\nAvailable Flights:")
        for flight_id, details in self.flights.items():
            print(f"{flight_id} | {details['route']} | Seats: {details['seats']} | Price: ₹{details['price']}")

    # Book flight
    def book_flight(self, flight_id, passenger_name, payment_success=True):

        # Validate passenger details
        if not passenger_name or not passenger_name.isalpha():
            raise InvalidPassengerDetailsError("Passenger name must contain only letters.")

        # Check flight existence
        if flight_id not in self.flights:
            raise ValueError("Invalid Flight ID")

        flight = self.flights[flight_id]

        # Check seat availability
        if flight["seats"] <= 0:
            raise SeatNotAvailableError("No seats available on this flight.")

        # Simulate payment
        if not payment_success:
            raise PaymentFailedError("Payment transaction failed.")

        # Book seat
        flight["seats"] -= 1
        booking_id = len(self.bookings) + 1

        self.bookings[booking_id] = {
            "flight": flight_id,
            "passenger": passenger_name
        }

        print(f"Booking successful! Booking ID: {booking_id}")

    # Cancel booking
    def cancel_booking(self, booking_id):

        if booking_id not in self.bookings:
            print("Invalid booking ID")
            return

        flight_id = self.bookings[booking_id]["flight"]

        # Restore seat
        self.flights[flight_id]["seats"] += 1

        del self.bookings[booking_id]

        print("Booking cancelled successfully.")


# Example usage
system = FlightBookingSystem()

try:
    system.search_flights()

    system.book_flight("AI303", "Rahul")   # seat not available
    system.book_flight("AI101", "Rahul123")  # invalid passenger

except SeatNotAvailableError as e:
    print("Seat Error:", e)

except InvalidPassengerDetailsError as e:
    print("Passenger Error:", e)

except PaymentFailedError as e:
    print("Payment Error:", e)

except Exception as e:
    print("General Error:", e)