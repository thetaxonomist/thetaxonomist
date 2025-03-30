from flask import Flask, render_template, request
import database as db
from math import floor

# TODO: Eliminate all duplication in the module

NOT_FOUND_ERROR = 404

app = Flask(__name__)

@app.route("/")
def index():
    phylums = len(db.phylums)
    classes = len(db.classes)
    species = len(db.species)
    return render_template("index.html", phylums=phylums, phylums_percentage=floor((int(phylums) / 14) * 100), classes=classes, classes_percentage=floor((int(classes) / 36) * 100), orders=len(db.orders), families=len(db.families), genera=len(db.genera), species=len(db.species), species_percentage=floor((int(species) / 400000) * 100))

@app.route("/kingdom/<string:name>")
def kingdom(name):
    error = 0
    kingdoms = db.kingdoms
    kingdom = None
    for i in kingdoms:
        if name == i.name:
            kingdom = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("kingdom.html", name=name, error=error)

    phylum_names = [i.name for i in kingdom.phylums]
    phylum_names.sort()
    return render_template("kingdom.html", name=name, error=error, phylums=phylum_names, description=kingdom.description, cladogram=kingdom.cladogram)

@app.route("/phylum/<string:name>")
def phylum(name):
    error = 0
    phylums = db.phylums
    phylum = None
    for i in phylums:
        if name == i.name:
            phylum = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("phylum.html", name=name, error=error)

    class_names = [i.name for i in phylum.classes]
    class_names.sort()
    return render_template("phylum.html", name=name, error=error, classes=class_names, kingdom=phylum.kingdom.name, description=phylum.description, cladogram=phylum.cladogram)

@app.route("/class/<string:name>")
def class_(name):
    error = 0
    classes = db.classes
    class_ = None
    for i in classes:
        if name == i.name:
            class_ = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("class.html", name=name, error=error)

    order_names = [i.name for i in class_.orders]
    order_names.sort()
    return render_template("class.html", name=name, error=error, orders=order_names, phylum=class_.phylum.name, kingdom=class_.phylum.kingdom.name, description=class_.description, cladogram=class_.cladogram)

@app.route("/order/<string:name>")
def order(name):
    error = 0
    orders = db.orders
    order = None
    for i in orders:
        if name == i.name:
            order = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("order.html", name=name, error=error)

    family_names = [i.name for i in order.families]
    family_names.sort()
    return render_template("order.html", name=name, error=error, families=family_names, class_=order.class_.name, phylum=order.class_.phylum.name, kingdom=order.class_.phylum.kingdom.name, description=order.description, cladogram=order.cladogram)

@app.route("/family/<string:name>")
def family(name):
    error = 0
    families = db.families
    family = None
    for i in families:
        if name == i.name:
            family = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("family.html", name=name, error=error)

    genus_names = [i.name for i in family.genera]
    genus_names.sort()
    return render_template("family.html", name=name, error=error, genera=genus_names, order=family.order.name, class_=family.order.class_.name, phylum=family.order.class_.phylum.name, kingdom=family.order.class_.phylum.kingdom.name, description=family.description, cladogram=family.cladogram)

@app.route("/genus/<string:name>")
def genus(name):
    error = 0
    genera = db.genera
    genus = None
    for i in genera:
        if name == i.name:
            genus = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("genus.html", name=name, error=error)

    species_names = [i.name for i in genus.species]
    species_names.sort()
    return render_template("genus.html", name=name, error=error, species=species_names, family=genus.family.name, order=genus.family.order.name, class_=genus.family.order.class_.name, phylum=genus.family.order.class_.phylum.name, kingdom=genus.family.order.class_.phylum.kingdom.name,  description=genus.description)

@app.route("/species/<string:gen>_<string:name>")
def species(gen, name):
    error = 0
    species = db.species
    specie = None
    for i in species:
        if f"{gen} {name}" == f"{i.genus.name} {i.name}":
            specie = i
            break
    else:
        error = NOT_FOUND_ERROR
    
    if error != 0:
        return render_template("species.html", name=name, error=error)
    return render_template("species.html", name=name, error=error, genus=gen, family=specie.genus.family.name, order=specie.genus.family.order.name, class_=specie.genus.family.order.class_.name, phylum=specie.genus.family.order.class_.phylum.name, kingdom=specie.genus.family.order.class_.phylum.kingdom.name, description=specie.description)

@app.route("/more_data")
def more_data():
    return render_template("more_data.html")

if __name__ == "__main__":
    app.run(debug=True)