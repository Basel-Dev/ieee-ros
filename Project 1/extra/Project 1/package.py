class Package:
    def __init__(self, package_id, weight, destination):
        self.id = package_id
        self.weight = weight
        self.destination = destination

    def __str__(self):
        return f"{self.id} | {self.weight} | {self.destination}" 
