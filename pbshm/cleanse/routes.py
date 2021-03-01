from flask import Blueprint, render_template
from pbshm.authentication.authentication import authenticate_request
from pbshm.pathfinder.pathfinder import population_list
from pbshm.cleanse.population import timestamps, channels, missing, statistics, sterilise

#Create the Cleanse Blueprint
bp = Blueprint(
    "cleanse",
    __name__,
    template_folder = "templates"
)

#Timestamp JSON View
@bp.route("/populations/<population>/timestamps")
@authenticate_request("autostat-cleanse")
def route_timestamps(population):
    return timestamps(population=population)

#Structures Channels JSON View
@bp.route("/populations/<population>/channels")
@authenticate_request("autostat-cleanse")
def route_channels(population):
    return channels(population=population)

#Missing JSON View
@bp.route("/populations/<population>/missing", methods=("GET", "POST"))
@authenticate_request("autostat-cleanse")
def route_missing(population):
    return missing(population=population)

#Statistics JSON View
@bp.route("/populations/<population>/statistics", methods=("GET", "POST"))
@authenticate_request("autostat-cleanse")
def route_statistics(population):
    return statistics(population=population)

#Sterilise JSON View
@bp.route("/populations/<population>/sterilise/<destination>", methods=("GET", "POST"))
@authenticate_request("autostat-cleanse")
def route_sterilise(population, destination):
    return sterilise(population=population, destination=destination)

#List View
@bp.route("/populations")
@authenticate_request("autostat-cleanse")
def route_list():
    return population_list("cleanse.route_details")

#Details View
@bp.route("/populations/<population>")
@authenticate_request("autostat-cleanse")
def route_details(population):
    return render_template("details.html", population=population)
