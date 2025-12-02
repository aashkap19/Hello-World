# come_fly_with_me.py
# "Come Fly with Me" airplane seat purchasing simulator

from dataclasses import dataclass, field
from typing import Dict, List, Optional

FIRST_CLASS_ROWS = {1, 2}        # rows charged a fee
EMERGENCY_ROWS = {4, 5}          # rows that require accepting responsibility
SEAT_LETTERS = ['A', 'B', 'C', 'D']  # 4 seats per row -> 5 rows * 4 = 20 seats
FIRST_CLASS_FEE = 100.00         # fee for any first-class seat

@dataclass
class Seat:
    row: int
    letter: str
    taken_by: Optional[str] = None  # customer name who took it, None if free

    def seat_id(self) -> str:
        return f"{self.row}{self.letter}"

    def is_first_class(self) -> bool:
        return self.row in FIRST_CLASS_ROWS

    def is_emergency(self) -> bool:
        return self.row in EMERGENCY_ROWS

@dataclass
class Plane:
    seats: Dict[str, Seat] = field(default_factory=dict)

    def __post_init__(self):
        for r in range(1, 6):
            for l in SEAT_LETTERS:
                s = Seat(row=r, letter=l)
                self.seats[s.seat_id()] = s

    def display_seating(self) -> None:
        print("\nCurrent seating (X = taken, O = available):")
        for r in range(1, 6):
            row_display = []
            for l in SEAT_LETTERS:
                sid = f"{r}{l}"
                mark = "X" if self.seats[sid].taken_by else "O"
                row_display.append(f"{sid}:{mark}")
            print("  " + "  ".join(row_display))
        print("")

    def is_valid_seat_id(self, seat_id: str) -> bool:
        return seat_id in self.seats

    def is_taken(self, seat_id: str) -> bool:
        return bool(self.seats[seat_id].taken_by)

    def purchase_seats(self, customer_name: str, seat_ids: List[str],
                       accept_emergency: Optional[Dict[str, bool]] = None) -> Dict[str, str]:
        """
        Attempts to purchase listed seat_ids for customer_name.
        accept_emergency: mapping seat_id->True/False for emergency seat acceptance (used for simulated runs).
        Returns a mapping seat_id -> result message.
        """
        results = {}
        total_cost = 0.0
        for sid in seat_ids:
            sid = sid.upper().strip()
            if not self.is_valid_seat_id(sid):
                results[sid] = "INVALID SEAT"
                continue
            seat = self.seats[sid]
            if seat.taken_by:
                results[sid] = f"ALREADY TAKEN by {seat.taken_by}"
                continue
            # handle emergency acceptance
            if seat.is_emergency():
                accepted = None
                if accept_emergency and sid in accept_emergency:
                    accepted = accept_emergency[sid]
                else:
                    # interactive prompt if not provided
                    ans = input(f"Seat {sid} is an emergency-row seat. Do you accept responsibility to help in an emergency? (yes/no): ")
                    accepted = ans.strip().lower().startswith('y')
                if not accepted:
                    results[sid] = "DECLINED EMERGENCY RESPONSIBILITY - NOT PURCHASED"
                    continue
            # calculate cost for first-class seats
            cost = 0.0
            if seat.is_first_class():
                cost += FIRST_CLASS_FEE
            # finalize purchase
            seat.taken_by = customer_name
            total_cost += cost
            price_info = f"PURCHASED"
            if cost > 0:
                price_info += f" (fee ${cost:.2f})"
            results[sid] = price_info
        if any(v.startswith("PURCHASED") for v in results.values()):
            purchased = [k for k,v in results.items() if v.startswith("PURCHASED")]
            print(f"\n{customer_name} successfully purchased: {', '.join(purchased)}")
            print(f"Total fees charged: ${total_cost:.2f}\n")
        return results

# Interactive main program function
def main_interactive():
    plane = Plane()
    print("Welcome to 'Come Fly with Me' seat purchasing simulator!")
    while True:
        plane.display_seating()
        name = input("Enter your name (or 'quit' to exit): ").strip()
        if not name:
            print("Please enter a name.")
            continue
        if name.lower() == 'quit':
            print("Goodbye!")
            break
        seats_input = input("Enter seat IDs to purchase (comma-separated, e.g. 1A,2B), or 'cancel' to abort: ").strip()
        if seats_input.lower() == 'cancel':
            continue
        seat_ids = [s.strip().upper() for s in seats_input.split(",") if s.strip()]
        # Build accept_emergency map interactively by asking user for each emergency seat in their request
        accept_map = {}
        for sid in seat_ids:
            if sid in plane.seats and plane.seats[sid].is_emergency():
                resp = input(f"Seat {sid} is emergency-row. Do you accept responsibility to assist in an emergency? (yes/no): ")
                accept_map[sid] = resp.strip().lower().startswith('y')
        results = plane.purchase_seats(customer_name=name, seat_ids=seat_ids, accept_emergency=accept_map)
        for sid, msg in results.items():
            print(f"{sid}: {msg}")
        cont = input("Would you like to make another purchase? (yes/no): ").strip().lower()
        if not cont.startswith('y'):
            print("Thank you for using the simulator. Final seating:")
            plane.display_seating()
            break

# For demonstration / automated tests we expose a function that simulates runs
def demo_runs():
    plane = Plane()
    print("DEMO RUNS\n")
    plane.display_seating()

    # 1) Successful purchase of an open regular seat (3A)
    print("Demo 1: Purchase open regular seat 3A by Alice")
    res1 = plane.purchase_seats(customer_name="Alice", seat_ids=["3A"])
    for k,v in res1.items():
        print(f"  {k}: {v}")
    plane.display_seating()

    # 2) Attempt to purchase a seat already taken (3A again) by Bob
    print("Demo 2: Attempt to buy seat 3A (already taken) by Bob")
    res2 = plane.purchase_seats(customer_name="Bob", seat_ids=["3A"])
    for k,v in res2.items():
        print(f"  {k}: {v}")
    plane.display_seating()

    # 3) Purchase multiple seats including first-class, emergency seats. Mixed accept/decline.
    print("Demo 3: Carol attempts to buy 1A (first-class), 4B (emergency), and 5C (emergency).")
    # Simulate: accept emergency for 4B, decline 5C
    accept_map = {"4B": True, "5C": False}
    res3 = plane.purchase_seats(customer_name="Carol", seat_ids=["1A","4B","5C"], accept_emergency=accept_map)
    for k,v in res3.items():
        print(f"  {k}: {v}")
    plane.display_seating()

    # 4) Show selecting multiple seats where one is already taken and others open
    print("Demo 4: Dave attempts to buy 1A (already taken by Carol), 2C (first-class open), and 3B (open regular).")
    res4 = plane.purchase_seats(customer_name="Dave", seat_ids=["1A","2C","3B"], accept_emergency={})
    for k,v in res4.items():
        print(f"  {k}: {v}")
    plane.display_seating()

if __name__ == "__main__":
    # Run demo runs to show expected behavior.
    demo_runs()