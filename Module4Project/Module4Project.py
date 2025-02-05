#Dunn delivery class demonstrating core OOP concepts
#-Encapsulation: Data(menu, prices) and methods are bundled in the class
#-Abstraction: Complex delivery logic is hidden behind simple method calls

class DunnDelivery:
    def __init__(self):
        # class attributes demonstrate encapsulation
        # by keeping related data together
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Caramel Cooler",
            "Pumpkin Spice Latte", "Espresso Shaker"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # prices encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99, "Caramel Cooler": 5.99,
            "Pumpkin Spice Latte": 4.99, "Espresso Shaker": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        self.delivery_locations = {
            "Library": 10, #minutes
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    def show_menu(self, category=None):
        if category:
            print(f"\n=== {category} ===")
            for item in self.menu[category]:
                print(f"{item}: ${self.prices[item]:.2f}")
        else:
            for category in self.menu:
                print(f"\n=== {category} ===")
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")
    
    def under_price(self):
        ask = input("\nWould you like to search for all items under a certain price? (yes/no): ").lower()
        if ask == 'yes':
            budget = float(input("Enter a budget amount: "))
            print(f"Here are all the items under ${budget:.2f}:")
            for item in self.prices:
                if self.prices[item] < budget:
                    print(f"{item}: ${self.prices[item]:.2f}")
        else:
            print("Order whatever you'd like!")

    def calculate_total(self, items, has_student_id=False):
        total = sum(self.prices[item] for item in items)
        if has_student_id and total > 10:
            total *= 0.9
        return total

    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        base_time = self.delivery_locations[location]
        if (9 <= current_hour <=10) or (11<= current_hour <= 13):
            base_time += 5
        if priority_delivery == True:
            base_time -= 3
        return base_time

    #give a delivery rating
    def rate_delivery(self):
        qualify = input("\nWould you like to rate your delivery? (yes/no): ").lower()
        if qualify == 'yes':
            input("Please enter a rating (1-5 Stars): ")
            print("Thank you for your feedback!")
        else:
            print("See you next time!")
    
    def print_order(self, location, items, current_hour, has_student_id=False):
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems ordered:")
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")
        
        quick = input("\nWould you like to receive priority delivery to reduce time by 3 minutes for $2? (yes/no): ").lower()
        if quick == 'yes':
            delivery_time = self.estimate_delivery(location, current_hour, priority_delivery=True)
            total = (self.calculate_total(items, has_student_id)) + 2
        else:
            delivery_time = self.estimate_delivery(location, current_hour, priority_delivery=False)
            total = self.calculate_total(items, has_student_id)

        print(f"\nSubtotal: ${sum(self.prices[item] for item in items):.2f}")
        if has_student_id and total < sum(self.prices[item] for item in items):
            print("Student Discount Applied!")
        print(f"Total after after delivery fee and discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")
        self.rate_delivery()

#example usage
def main():
    delivery = DunnDelivery()
    delivery.under_price()
    delivery.show_menu("Coffee Drinks")

    #sample order at 9:30 AM (peak hours)
    order = ["Latte", "Bagel"]
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True)

if __name__ == "__main__":
    main()