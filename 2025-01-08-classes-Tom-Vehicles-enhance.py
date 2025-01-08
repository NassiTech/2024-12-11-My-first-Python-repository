class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tank_size_in_l,
    ):

        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tank_size = tank_size_in_l

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def coverage_with_one_tank(self):
        coverage_with_one_tank = (
            self.average_consumption_in_l * self.tank_size_in_l / 100
        )
        return coverage_with_one_tank

    def get_number_of_tank_refill(self):
        number_of_tank_refill = self.km_driven / self.coverage_with_one_tank()
        return number_of_tank_refill


my_vehicle = Vehicles("VW", "Golf", 10)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
print(f"The total consumption is about: {my_vehicle.get_total_consumption()}")
print(f"the car can with: {my_vehicle.number_of_tank_refill} ")
