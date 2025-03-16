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
bryophyta = Phylum("bryophyta", description="mosses. Not to be confused with Phylum bryophyta sensu lato which include hornworts and liverworts.")
anthocerotophyta = Phylum("anthocerotophyta", description="hornworts")
marchantiophyta = Phylum("marchantiophyta", description="liverworts")
takakiopsida = Class("takakiopsida")
sphagnopsida = Class("sphagnopsida")
andreaeopsida = Class("andreaeopsida")
andreaeobryopsida = Class("andreaeobryopsida")
oedipodiopsida = Class("oedipodiopsida")
polytrichopsida = Class("polytrichopsida")
tetraphidopsida = Class("tetraphidopsida")
bryopsida = Class("bryopsida")
bryophyta.add_class(takakiopsida)
bryophyta.add_class(sphagnopsida)
bryophyta.add_class(andreaeopsida)
bryophyta.add_class(andreaeobryopsida)
bryophyta.add_class(oedipodiopsida)
bryophyta.add_class(polytrichopsida)
bryophyta.add_class(tetraphidopsida)
haplomitriopsida = Class("haplomitriopsida")
calobryales = Order("calobryales")
treubiales = Order("treubiales")
haplomitriopsida.add_order(calobryales)
haplomitriopsida.add_order(treubiales)
marchantiopsida = Class("marchantiopsida")
jungermanniopsida = Class("jungermanniopsida")
marchantiophyta.add_class(haplomitriopsida)
marchantiophyta.add_class(marchantiopsida)
marchantiophyta.add_class(jungermanniopsida)
leiosporocerotopsida = Class("leiosporocerotopsida")
leiosporocerotales = Order("leiosporocerotales")
leiosporocerotopsida.add_order(leiosporocerotales)
anthocerotopsida = Class("anthocerotopsida")
anthocerotales = Order("anthocerotales")
dendrocerotales = Order("dendrocerotales")
notothyladales = Order("notothyladales")
phymatocerotales = Order("phymatocerotales")
anthocerotopsida.add_order(anthocerotales)
anthocerotopsida.add_order(dendrocerotales)
anthocerotopsida.add_order(notothyladales)
anthocerotopsida.add_order(phymatocerotales)
anthocerotophyta.add_class(leiosporocerotopsida)
anthocerotophyta.add_class(anthocerotopsida)
lycopodiophyta = Phylum("lycopodiophyta", description="Lycopods")
polypodiophyta = Phylum("polypodiophyta", description="Ferns")
lycopodiopsida = Class("lycopodiopsida", description="Lycopods, also Division Lycopodiophyta. Also called Lycopsida")
polypodiopsida = Class("polypodiopsida", description="Ferns, also Division Polypodiophyta")
lycopodiophyta.add_class(lycopodiopsida)
polypodiophyta.add_class(polypodiopsida)
isoetales = Order("isoetales")
lycopodiales = Order("lycopodiales")
selaginellales = Order("selaginellales")
lycopodiopsida.add_order(isoetales)
lycopodiopsida.add_order(lycopodiales)
lycopodiopsida.add_order(selaginellales)
cycadophyta = Phylum("cycadophyta", description="See cycadopsida")
ginkgophyta = Phylum("ginkgophyta", description="See ginkgoopsida")
gnetophyta = Phylum("gnetophyta", description="See gnetopsida")
pinophyta = Phylum("pinophyta", description="conifers")
angiospermae = Phylum("angiospermae", description="Flowering Plant")
plants.add_phylum(bryophyta)
plants.add_phylum(marchantiophyta)
plants.add_phylum(anthocerotophyta)
plants.add_phylum(lycopodiophyta)
plants.add_phylum(polypodiophyta)
plants.add_phylum(cycadophyta)
plants.add_phylum(ginkgophyta)
plants.add_phylum(gnetophyta)
plants.add_phylum(pinophyta)
plants.add_phylum(angiospermae)
dicots = Class("magnoliopsida", description="dicots")
monocots = Class("liliopsida", description="monocots")
cycadopsida = Class("cycadopsida", description="cycads")
cycadales = Order("cycadales", description="order cycadales, only living order of class cycadopsida")
cycadopsida.add_order(cycadales)
cycadaceae = Family("cycadaceae")
zamiaceae = Family("zamiaceae")
cycadales.add_family(cycadaceae)
cycadales.add_family(zamiaceae)
ginkgoopsida = Class("ginkgoopsida", description="ginkgo, there is only one living species of ginkgo, the ginkgo biloba")
ginkgoales = Order("ginkgoales", description="order ginkgoales, only living order of class ginkgoopsida. there is only one living species of ginkgo, the ginkgo biloba")
ginkgoopsida.add_order(ginkgoales)
ginkgoaceae = Family("ginkgoaceae", description="only one living species left in this family, ginkgo biloba")
ginkgoales.add_family(ginkgoaceae)
ginkgo = Genus("ginkgo", description="only one living species left")
ginkgoaceae.add_genera(ginkgo)
ginkgo_biloba = Species("biloba", description="only living member of the division ginkgophyta")
ginkgo.add_species(ginkgo_biloba)
gnetophytes = Class("gnetopsida", description="gnetophytes")
gnetales = Order("gnetales")
ephedrales = Order("ephedrales")
welwitschiales = Order("welwitschiales")
gnetophytes.add_order(gnetales)
gnetophytes.add_order(ephedrales)
gnetophytes.add_order(welwitschiales)
conifers = Class("pinopsida", description="conifers. also Division Pinophyta/Coniferophyta")
araucariales = Order("araucariales", description="araucariales, subclass cupressidae")
cupressales = Order("cupressales", description="cupressales, subclass cupressidae")
pinales = Order("pinales", description="pinales, subclass pinidae")
conifers.add_order(araucariales)
conifers.add_order(cupressales)
conifers.add_order(pinales)
magnoliidae = Class("magnoliidae", description="magnoliids. Officially classified as a subclass but has no official parent class.")
cycadophyta.add_class(cycadopsida)
ginkgophyta.add_class(ginkgoopsida)
gnetophyta.add_class(gnetophytes)
pinophyta.add_class(conifers)
angiospermae.add_class(dicots)
angiospermae.add_class(monocots)
angiospermae.add_class(magnoliidae)
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
canellales = Order("canellales")
piperales = Order("piperales")
laurales = Order("laurales")
magnoliales = Order("magnoliales")
magnoliidae.add_order(canellales)
magnoliidae.add_order(piperales)
magnoliidae.add_order(laurales)
magnoliidae.add_order(magnoliales)
chloranthales = Order("chloranthales")
ceratophyllales = Order("ceratophyllales")
dicots.add_order(chloranthales) # basal angio
dicots.add_order(ceratophyllales) # basal angio

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
