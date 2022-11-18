#import dependencies 
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

# Database Setup

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Starting from the most recent data point in the database. 
    most_recent_date = list(session.query(Measurement.date).order_by(Measurement.date.desc()).first())
    most_recent = most_recent_date[0]

    # Calculate the date one year from the last date in data set.
    last_year = dt.date(2017, 8 ,23) - dt.timedelta(days=365)
    
    # Query all precipitation
    scores = session.query(Measurement.date, Measurement.prcp).filter((Measurement.date > last_year) & (Measurement.date < most_recent))

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_precipitation = []
    for date, prcp in scores:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)  

#stations api
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    """Return a list of all stations"""
    # Starting from the most recent data point in the database. 
    stations = session.query(Station.station, Station.name).all()
    
    session.close()

    return jsonify(stations)  
    
# #tobs api
# @app.route("/api/v1.0/tobs")
# def tobs():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)
    
#     """Return a list of all tobs for most active station"""
#     # Starting from the most recent data point in the database. 
#     most_recent_date = list(session.query(Measurement.date).order_by(Measurement.date.desc()).first())
#     most_recent = most_recent_date[0]

#     # Calculate the date one year from the last date in data set.
#     last_year = dt.date(2017, 8 ,23) - dt.timedelta(days=365)
    
#     # Starting from the most recent data point in the database. 
#     station_7 = (session.query(Measurement.tobs).filter((Measurement.date > last_year) & (Measurement.date < most_recent(Station.id == 7) & (Measurement.station == Station.station)
    
#     session.close()
                                        
#     return jsonify(station_7)    
    
@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)
                                        
    start_only = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),func.avg(Measurement.tobs)).filter(Station.id == 7).filter(Measurement.station == Station.station).filter(Measurement.date >= start).all()
 
if __name__ == '__main__':
        app.run(debug=True)