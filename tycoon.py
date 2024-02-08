class Ship:
    def __init__(self, name, ship_type, cost, speed, cargo_capacity):
        self.name = name
        self.ship_type = ship_type
        self.cost = cost
        self.speed = speed
        self.cargo_capacity = cargo_capacity

class Contract:
    def __init__(self, origin, destination, cargo_type, urgency, reward):
        self.origin = origin
        self.destination = destination
        self.cargo_type = cargo_type
        self.urgency = urgency
        self.reward = reward

class Game:
    def __init__(self):
        self.budget = 1000000  # Starting budget
        self.fleet = []
        self.contracts = []
        self.reputation = 0
        self.current_time = 0

    def start_game(self):
        self.budget = 1000000
        self.fleet = []
        self.contracts = self.generate_initial_contracts()
        print("Game started with budget:", self.budget)

    def generate_initial_contracts(self):
        # Generating some initial contracts for demonstration
        return [
            Contract("Port A", "Port B", "Bulk", 2, 20000),
            Contract("Port C", "Port D", "Container", 3, 30000)
        ]

    def buy_ship(self):
        # Simplified ship purchase
        ship_type = "Bulk Carrier"
        cost = 200000
        if self.budget >= cost:
            new_ship = Ship(f"Ship {len(self.fleet)+1}", ship_type, cost, 20, 1000)
            self.fleet.append(new_ship)
            self.budget -= cost
            print(f"Bought new ship: {new_ship.name}. Remaining budget: {self.budget}")
        else:
            print("Not enough budget to buy this ship.")

    def display_status(self):
        # Displaying current game status
        print(f"Current Budget: {self.budget}, Fleet Size: {len(self.fleet)}, Contracts Available: {len(self.contracts)}")

    def main_loop(self):
        # Placeholder for main game loop for demonstration
        self.display_status()
        self.buy_ship()  # Example action

if __name__ == "__main__":
    game = Game()
    game.start_game()
    game.main_loop()
