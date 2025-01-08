#dictionaries 
#the initialisation startzs with {"<key>": "<value>"}
#value can have any data type
#score_dict = {}
#key vlue pair introduce
#score_dict["max"] = 100 # to -> {"max" : 100}
#call a value of a key
#score_max = score_dict["max"] #100

#print(f"{score_max}")

#score_dict["ana"] = 80 
#score_anna = [80]

# .items()
# for key in score_dict.keys(): # max & anna 
# for v in score_dict.values() : print(f"{v}") v= value
#for k, value in score_dict.items(:
#print(f"key:{k}, value:{value}")

#Classes
class Vehicles:
  #  def_init_(self, brand_name, vehicle_brand_name):
  #  self.name = "max"
  #  self.brand_name = vehicle_brand_name
   # my_vehicles = Vehicles()
  #  print( my_vehicles )
 #   def get_brand_name(self):
    #    return self.brand_name
  #  def get_description(self):
   #     return self.brand_name + "," + self.model_name
 #   def drive(self, km_driven)

class Vehicles:
    def __init__(
        self, vehicle_brand_name, vehicle_model_name, average_consumption_in_l
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven


my_vehicle = Vehicles("VW", "Golf", 10)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
