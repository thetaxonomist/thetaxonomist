class Kingdom:
    def __init__(self, name, description=''):
        self.name = name
        self.phylums = set() # Empty set
        self.description = description
    
    def add_phylum(self, phylum):
        self.phylums.add(phylum)
        phylum.kingdom = self

class Phylum:
    def __init__(self, name, description=''):
        self.name = name
        self.kingdom = None
        self.classes = set()
        self.description = description

    def get_kingdom_name(self):
        return self.kingdom.name

    def add_class(self, class_):
        self.classes.add(class_)
        class_.phylum = self

class Class:
    def __init__(self, name, description=''):
        self.name = name
        self.phylum = None
        self.orders = set()
        self.description = description

    def get_phylum_name(self):
        return self.phylum.name

    def add_order(self, order):
        self.orders.add(order)
        order.class_ = self

class Order:
    def __init__(self, name, description=''):
        self.name = name
        self.class_ = None
        self.families = set()
        self.description = description

    def get_class_name(self):
        return self.class_.name

    def add_family(self, family):
        self.families.add(family)
        family.order = self

class Family:
    def __init__(self, name, description=''):
        self.name = name
        self.order = None
        self.genera = set()
        self.description = description

    def get_order_name(self):
        return self.order.name

    def add_genera(self, genus):
        self.genera.add(genus)
        genus.family = self

class Genus:
    def __init__(self, name, description=''):
        self.name = name
        self.family = None
        self.species = set()
        self.description = description

    def get_family_name(self):
        return self.family.name

    def add_species(self, species):
        self.species.add(species)
        species.genus = self

class Species:
    def __init__(self, name, description=''):
        self.name = name
        self.genus = None
        self.description = description

    def get_genus_name(self):
        return self.genus.name
    
plants = Kingdom("plantae", description="Plant Kingdom")
kingdoms = [plants]
bryophyta = Phylum("bryophyta", description="Non-vascular land plants")
pteridophyta = Phylum("pteridophyta", description="Vascular plants without true seeds")
spermatophyta = Phylum("spermatophyta", description="Seed plants")
plants.add_phylum(bryophyta)
plants.add_phylum(pteridophyta)
plants.add_phylum(spermatophyta)
dicots = Class("magnoliophyta", description="dicots")
monocots = Class("liliophyta", description="monocots")
cycads = Class("cycadophyta", description="cycads")
ginkgo = Class("ginkgophyta", description="ginkgo")
gnetophytes = Class("gnetophyta", description="gnetophytes")
conifers = Class("pinophyta", description="conifers")
spermatophyta.add_class(cycads)
spermatophyta.add_class(ginkgo)
spermatophyta.add_class(gnetophytes)
spermatophyta.add_class(conifers)
spermatophyta.add_class(dicots)
spermatophyta.add_class(monocots)
rosales = Order("rosales")
fabales = Order("fabales")
lamiales = Order("lamiales")
asterales = Order("asterales")
dicots.add_order(rosales)
dicots.add_order(fabales)
dicots.add_order(lamiales)
dicots.add_order(asterales)
rosaceae = Family("rosaceae", description="rose family")
rosales.add_family(rosaceae)
rose = Genus("rosa", description="rose")
rosaceae.add_genera(rose)
chinarose = Species("chinensis", description="china rose")
rose.add_species(chinarose)

phylums = []
for kingdom in kingdoms:
    phylums += kingdom.phylums

classes = []
for phylum in phylums:
    classes += phylum.classes

orders = []
for class_ in classes:
    orders += class_.orders

families = []
for order in orders:
    families += order.families

genera = []
for family in families:
    genera += family.genera

species = []
for genus in genera:
    species += genus.species