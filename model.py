"""Models for F1 drivers, races, and constructors."""

from xml.etree.ElementTree import ProcessingInstruction
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

### Modeling of Race related classes

class Race(db.Model):
    """A storage space."""

    __tablename__ = "races"

    race_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Datetime)
    circuit_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    name = db.Column(db.String)
    date = db.Column(db.Datetime)
    time = db.Column(db.Datetime) 

    # Is it better to use datetime or timestamp? Was thinking timestamp for race &
    # lap results?
    # Is it best practice to specificy that they can't be nullable?

    def __repr__(self):
        return f"<Race race_id={self.raceid} name={self.name}>"

class LapTime(db.Model):
    """A melon type."""

    __tablename__ = "lap_times"

    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    lap = db.Column(db.Integer)
    position = db.Column(db.Integer)
    time = db.Column(db.Timestamp)
    milliseconds = db.Column(db.Integer)
    # Is it okay to have a primary key that is also a foreign key?

    race = db.relationship("Race", back_populates="lap_times")
    race = db.relationship("Driver", back_populates="lap_times")

    ## is this correct even though it is many to one?

    def __repr__(self):
        return f"<LapTime race_id={self.race_id} time={self.time}>"

class Result(db.Model):
    """A melon."""

    __tablename__ = "results"

    result_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"))
    number = db.Column(db.Integer)
    grid = db.Column(db.Integer)
    position = db.Column(db.Integer)
    position_text = db.Column(db.String)
    position_order = db.Column(db.Integer)
    points = db.Column(db.Integer)
    laps = db.Column(db.Integer)
    time = db.Column(db.Timestamp)
    milliseconds = db.Column(db.Integer)
    fastest_lap = db.Column(db.Int)
    rank = db.Column(db.Integer)
    fastest_lap_time = db.Column(db.Timestamp)
    fastest_lap_speed = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey("status.status_id"))

    ## need to look in API docs to see if position text is a string and not an integer (looks like 
    # an int  in the CSV)
    # Using timestamp for time?

    driver = db.relationship("Driver", backref="results")
    constructor = db.relationship("Constructor", backref="results")
    status = db.relationship("Status", backref="results")

    def __repr__(self):
        return f"<Result result_id={self.result_id} race_id={self.race_id}>"


class SprintResult(db.Model):
    """A melon."""

    __tablename__ = "sprint_results"

    result_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"))
    number = db.Column(db.Integer)
    grid = db.Column(db.Integer)
    position = db.Column(db.Integer)
    position_text = db.Column(db.String)
    position_order = db.Column(db.Integer)
    points = db.Column(db.Integer)
    laps = db.Column(db.Integer)
    time = db.Column(db.Timestamp)
    milliseconds = db.Column(db.Integer)
    fastest_lap = db.Column(db.Int)
    fastest_lap_time = db.Column(db.Timestamp)
    status_id = db.Column(db.Integer, db.ForeignKey("status.status_id"))

    ## need to look in API docs to see if position text is a string and not an integer (looks like 
    # an int  in the CSV)
    # Using timestamp for time?

    race = db.relationship("Race", backref="sprint_results")
    driver = db.relationship("Driver", backref="sprint_results")
    constructor = db.relationship("Constructor", backref="sprint_results")
    status = db.relationship("Status", backref="sprint_results")

    def __repr__(self):
        return f"<Result result_id={self.result_id} race_id={self.race_id}>"


class QualifyingLap(db.Model):
    """A storage space."""

    __tablename__ = "qualifying_laps"

    qualify_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"))
    number = db.Column(db.Integer)
    position = db.Column(db.Integer)
    q1 = db.Column(db.Timestamp)
    q2 = db.Column(db.Timestamp)
    q3 = db.Column(db.Timestamp)  

    # Is it better to use datetime or timestamp? Was thinking timestamp for race &
    # lap results?
    # Is it best practice to specificy that they can't be nullable?
    
    race = db.relationship("Race", backref="qualifying_laps")
    driver = db.relationship("Driver", backref="qualifying_laps")
    constructor = db.relationship("Constructor", backref="qualifying_laps")
    status = db.relationship("Status", backref="qualifying_laps")

    def __repr__(self):
        return f"<QualifyingLap qualify_id={self.qualify_id} race_id={self.race_id}>"

class PitStop(db.Model):
    """A storage space."""

    __tablename__ = "pit_stops"

    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    stop = db.Column(db.Integer)
    lap = db.Column(db.Integer)
    time = db.Column(db.Timestamp)
    duration = db.Column(db.Integer)
    milliseconds = db.Column(db.Integer)

    race = db.relationship("Race", backref="pit_stops")
    driver = db.relationship("Driver", backref="pit_stops")

    def __repr__(self):
        return f"<PitStop race_id={self.race_id} driver_id={self.driver_id}>"


class Status(db.Model):
    """A storage space."""

    __tablename__ = "statuses"

    status_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)

    def __repr__(self):
        return f"<Status status_id={self.status_id} status={self.status}>"


class Driver(db.Model):
    """A storage space."""

    __tablename__ = "drivers"

    driver_id = db.Column(db.Integer, primary_key=True)
    driver_ref = db.Column(db.String)
    number = db.Column(db.Integer)
    forename = db.Column(db.String)
    surname = db.Column(db.String)
    date = db.Column(db.Datetime) 
    nationality = db.Column(db.String) 
    url = db.Column(db.String)

    # Is it better to use datetime or timestamp? Was thinking timestamp for race &
    # lap results?
    # Is it best practice to specificy that they can't be nullable?

    def __repr__(self):
        return f"<Driver driver_id={self.driver_id} surname={self.surname}>"


class DriverStanding(db.Model):
    """A storage space."""

    __tablename__ = "driver_standings"

    standings_id = db.Column(db.Integer, primary_key = True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    points = db.Column(db.Integer)
    position = db.Column(db.Integer)
    position_text = db.Column(db.String)
    wins = db.Column(db.Integer)
    
    race = db.relationship("Race", backref="driver_standings")
    driver = db.relationship("Driver", backref="driver_standings")

    def __repr__(self):
        return f"<DriverStanding standings_id={self.standings_id} driver_id={self.driver_id}>"


class Season(db.Model):
    """A storage space."""

    __tablename__ = "seasons"

    year = db.Column(db.Integer)
    url = db.Column(db.String)

    def __repr__(self):
        return f"<Season year={self.year} url={self.url}>"

class Constructor(db.Model):
    """Table for constructors"""

    __tablename__ = "constructors"

    constructor_id = db.Column(db.Integer, primary_key = True)
    constructor_ref = db.Column(db.String)
    name = db.Column(db.String)
    nationality = db.Column(db.String)
    url = db.Column(db.url)

    def __repr__(self):
        return f"<Constructor constructor_id={self.constructor_id} name={self.name}>"

class ConstructorResult(db.Model):
    """Table for constructors"""

    __tablename__ = "constructor_reuslts"

    constructor_result_id = db.Column(db.Integer, primary_key = True)
    race_id = db.Column(db.Integer), db.ForeignKey("races.race_id")
    constructor_id = db.Column(db.Integer), db.ForeignKey("constructors.constructor_id")
    points = db.Column(db.Integer)


    race = db.relationship("Race", backref="constructor_standings")
    driver = db.relationship("Constructor", backref="constructor_standings")

    def __repr__(self):
        return f"<ConstructorResult constructor_result_id={self.constructor_result_id} name={self.name}>"

class ConstructorStanding(db.Model):
    """Table for constructors"""

    __tablename__ = "constructor_standings"

    constructor_standing_id = db.Column(db.Integer, primary_key = True)
    race_id = db.Column(db.Integer), db.ForeignKey("races.race_id")
    constructor_id = db.Column(db.Integer), db.ForeignKey("constructors.constructor_id")
    points = db.Column(db.Integer)
    position = db.Column(db.Integer)
    position_text = db.Column(db.String)
    wins = db.Column(db.Integer)



    race = db.relationship("Race", backref="constructor_standings")
    driver = db.relationship("Constructor", backref="constructor_standings")

    def __repr__(self):
        return f"<ConstructorStandinf constructor_standing_id={self.constructor_standing_id} race_id={self.race_id}>"


class Circuit(db.Model):
    """Table for constructors"""

    __tablename__ = "constructors"

    circuit_id = db.Column(db.Integer, primary_key = True)
    circuit_ref = db.Column(db.String)
    name = db.Column(db.String)
    location = db.Column(db.String)
    country = db.Column(db.String)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    alt = db.Column(db.Integer)
    url = db.Column(db.String)

    def __repr__(self):
        return f"<Circuit circuit_id={self.circuit_id} name={self.name}>"