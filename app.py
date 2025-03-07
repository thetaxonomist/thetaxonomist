from flask import Flask, render_template, redirect
import database as db

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/kingdom/plantae")

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
        error = 1
    
    if error != 0:
        return render_template("kingdom.html", name=name, error=error)

    phylum_names = [i.name for i in kingdom.phylums]
    return render_template("kingdom.html", name=name, error=error, phylums=phylum_names, description=kingdom.description)

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
        error = 1
    
    if error != 0:
        return render_template("phylum.html", name=name, error=error)

    class_names = [i.name for i in phylum.classes]
    return render_template("phylum.html", name=name, error=error, classes=class_names, kingdom=phylum.kingdom.name, description=phylum.description)

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
        error = 1
    
    if error != 0:
        return render_template("class.html", name=name, error=error)

    order_names = [i.name for i in class_.orders]
    return render_template("class.html", name=name, error=error, orders=order_names, phylum=class_.phylum.name, description=class_.description)

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
        error = 1
    
    if error != 0:
        return render_template("order.html", name=name, error=error)
    family_names = [i.name for i in order.families]
    return render_template("order.html", name=name, error=error, families=family_names, class_=order.class_.name, description=order.description)

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
        error = 1
    
    if error != 0:
        return render_template("family.html", name=name, error=error)
    genus_names = [i.name for i in family.genera]
    return render_template("family.html", name=name, error=error, genera=genus_names, order=family.order.name, description=family.description)

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
        error = 1
    
    if error != 0:
        return render_template("genus.html", name=name, error=error)
    species_names = [i.name for i in genus.species]
    return render_template("genus.html", name=name, error=error, species=species_names, family=genus.family.name, description=genus.description)

@app.route("/species/<string:gen> <string:name>")
def species(gen, name):
    error = 0
    species = db.species
    specie = None
    for i in species:
        if f"{gen} {name}" == f"{i.genus.name} {i.name}":
            specie = i
            break
    else:
        error = 1
    
    if error != 0:
        return render_template("species.html", name=name, error=error)
    return render_template("species.html", name=name, error=error, genus=gen, family=specie.genus.family.name, description=specie.description)


if __name__ == "__main__":
    app.run(debug=True)