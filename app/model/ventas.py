class Ventas:
	int id
	float price
	create_at = ""

	def __init__(self, int id, float price, create_at):
		self.id = id;
		self.price = price
		self.create_at = create_at
