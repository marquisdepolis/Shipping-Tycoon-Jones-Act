import random

class Port:
    def __init__(self, name):
        self.name = name

class Ship:
    def __init__(self, name, ship_type, cost, speed, cargo_capacity):
        self.name = name
        self.ship_type = ship_type
        self.cost = cost
        self.speed = speed
        self.cargo_capacity = cargo_capacity

class Contract:
    def __init__(self, origin, destination, cargo_type, value):
        self.origin = origin
        self.destination = destination
        self.cargo_type = cargo_type
        self.value = value
        # Assuming all ports in this version are in the US for simplicity
        self.is_jones_compliant = True

class Game:
    def __init__(self):
        self.budget = 1000000  # Starting budget
        self.fleet = []
        self.contracts = []
        self.ports = [
            Port("Los Angeles"), Port("Seattle"), Port("Miami"), Port("New York")
        ]

    def start_game(self):
        self.budget = 1000000
        self.fleet = []
        print("Game started with budget:", self.budget)
        self.attempt_to_buy_ship()
    def attempt_to_buy_ship(self):
        # Simplified ship buying logic
        ship_cost = 200000  # Assuming a flat rate for simplicity
        if self.budget >= ship_cost:
            choice = input("Do you want to buy a ship for $200,000? (y/n): ")
            if choice.lower() == 'y':
                self.budget -= ship_cost
                new_ship = Ship(f"Ship {len(self.fleet)+1}", "General Cargo", ship_cost, 20, 1000)
                self.fleet.append(new_ship)
                print(f"Bought new ship: {new_ship.name}. Remaining budget: {self.budget}")
            else:
                print("You decided not to buy a ship.")
        else:
            print("Not enough budget to buy a ship.")

    def generate_contract(self):
        origin = random.choice(self.ports)
        destination = random.choice(self.ports)
        while destination == origin:
            destination = random.choice(self.ports)

        distance = self.calculate_distance(origin, destination)
        base_value = distance * 25  # $25 per distance unit - adjust as needed

        cargo_type = random.choice(["bulk goods", "containers"])
        value = base_value

        return Contract(origin, destination, cargo_type, value)

    def calculate_distance(self, port1, port2):
        # Placeholder - We'd ideally use real distances/shipping lanes
        return random.randint(500, 3000)

    def display_status(self):
        # Displaying current game status
        print(f"Current Budget: {self.budget}, Fleet Size: {len(self.fleet)}")

    def player_bid(self, contract):
        print(f"Contract: {contract.cargo_type} from {contract.origin.name} to {contract.destination.name}")
        print(f"Value: ${contract.value}, Jones Act Compliant: {contract.is_jones_compliant}")
        choice = input("Accept Contract? (y/n): ")
        return choice.lower() == 'y'

    def main_loop(self):
        self.display_status()
        if len(self.fleet) == 0:
            print("You need at least one ship in your fleet to accept contracts.")
            # Optionally, prompt the player to buy a ship here if budget allows
        else:
            new_contract = self.generate_contract()
            if self.player_bid(new_contract):
                print("Contract accepted!")
                # Add logic to handle contract acceptance (e.g., deducting costs, calculating delivery time)
            else:
                print("Contract rejected.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
    for _ in range(5):  # Run 5 iterations for demonstration
        game.main_loop()
