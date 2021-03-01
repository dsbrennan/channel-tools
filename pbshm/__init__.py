import os
from flask import Flask

def create_app(test_config=None):
    #Create Flask App
    app = Flask(__name__, instance_relative_config=True)

    #Load Configuration
    app.config.from_mapping(
        PAGE_SUFFIX=" - PBSHM Automated Statistician",
        LOGIN_MESSAGE="Welcome to the Dynamics Research Group Automated Statistician, please enter your authentication credentials below.",
        FOOTER_MESSAGE="Automated Statistician V1.0, PBSHM Flask Core V1.0.2, © Dynamics Research Group 2020",
        NAVIGATION={
            "modules":{
                "Pathfinder": "pathfinder.population_list",
                "Cleanse": "cleanse.route_list",
                "Autostat": "autostat.population_list"
            }
        }
    )
    app.config.from_json("config.json", silent=True) if test_config is None else app.config.from_mapping(test_config)
    
    #Ensure Instance Folder
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Add Blueprints
    ## Initialisation
    from pbshm.initialisation import initialisation
    app.register_blueprint(initialisation.bp)
    ## Authentication
    from pbshm.authentication import authentication
    app.register_blueprint(authentication.bp, url_prefix="/authentication")
    ## Pathfinder
    from pbshm.pathfinder import pathfinder
    app.register_blueprint(pathfinder.bp, url_prefix="/pathfinder")
    ## Cleanse
    from pbshm.cleanse import routes as cleanse_routes
    app.register_blueprint(cleanse_routes.bp, url_prefix="/cleanse")
    ## Autostat
    from pbshm.autostat import autostat
    app.register_blueprint(autostat.bp, url_prefix="/autostat")

    #Set Root Page
    app.add_url_rule("/", endpoint="autostat.population_list")
    
    #Return App
    return app