"""Models for F1 drivers, races, and constructors."""

from xml.etree.ElementTree import ProcessingInstruction
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    likes = db.relationship("User", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

### Modeling of Race related classes

class Like(db.Model):
    """Table storing all likes for individual users"""

    __tablename__ = "likes"

    like_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("seasons.year"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))


    user = db.relationship("User", back_populates="likes")
    driver = db.relationship("Driver", back_populates="likes")


class Race(db.Model):
    """F1 Race information"""

    __tablename__ = "races"

    race_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, db.ForeignKey("seasons.year"))
    circuit_id = db.Column(db.Integer, db.ForeignKey("circuits.circuit_id"))
    name = db.Column(db.String(255))
    date = db.Column(db.Datetime)
    time = db.Column(db.Datetime) 
    url = db.Column(db.String(255))

    season = db.relationship("Season", back_populates="race")
    circuit = db.relationship("Circuit", back_populates="race")
    lap_times = db.relationship("LapTime", back_populates="race")
    sprint_results = db.relationship("SprintResult", backref="race")
    qualifying_laps = db.relationship("QualifyingLap", backref="race")
    pit_stops = db.relationship("PitStop", backref="race")
    driver_standings = db.relationship("DriverStanding", backref="race")
    constructor_results = db.relationship("ConstructorResult", backref="race")
    constructor_standings = db.relationship("ConstructorStanding", backref="race")

    def __repr__(self):
        return f"<Race race_id={self.raceid} name={self.name}>"

class LapTime(db.Model):
    """A melon type."""

    __tablename__ = "lap_times"

    lap_time_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"), nullable = False)
    lap = db.Column(db.Integer, nullable = False)
    position = db.Column(db.Integer, nullable = True)
    time = db.Column(db.String(255), nullable = True)
    milliseconds = db.Column(db.Integer, nullable = True)

    race = db.relationship("Race", back_populates="lap_times")
    driver = db.relationship("Driver", back_populates="lap_times")

    def __repr__(self):
        return f"<LapTime race_id={self.race_id} time={self.time}>"

class Result(db.Model):
    """A melon."""

    __tablename__ = "results"

    result_id = db.Column(db.Integer, primary_key=True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"), nullable = False)
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"), nullable = False)
    number = db.Column(db.Integer, nullable = True)
    grid = db.Column(db.Integer, nullable = False)
    position = db.Column(db.Integer, nullable = True)
    position_text = db.Column(db.String(255), nullable = False)
    position_order = db.Column(db.Integer, nullable = False )
    points = db.Column(db.Integer, nullable = False)
    laps = db.Column(db.Integer, nullable = False)
    time = db.Column(db.String(255), nullable = True)
    milliseconds = db.Column(db.Integer, nullable = True)
    fastest_lap = db.Column(db.Integer, nullable = True)
    rank = db.Column(db.Integer)
    fastest_lap_time = db.Column(db.String(255))
    fastest_lap_speed = db.Column(db.String(255))
    status_id = db.Column(db.Integer, db.ForeignKey("status.status_id"), nullable = False)

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
    number = db.Column(db.Integer, nullable = True)
    grid = db.Column(db.Integer)
    position = db.Column(db.Integer, nullable = True)
    position_text = db.Column(db.String)
    position_order = db.Column(db.Integer)
    points = db.Column(db.Integer)
    laps = db.Column(db.Integer)
    time = db.Column(db.Timestamp, nullable = True)
    milliseconds = db.Column(db.Integer, nullable = True)
    fastest_lap = db.Column(db.Int, nullable = True)
    fastest_lap_time = db.Column(db.Timestamp, nullable = True)
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

    qualify_id = db.Column(db.Integer, primary_key=True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"), nullable = False)
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"), nullable = False)
    number = db.Column(db.Integer, nullable = False)
    position = db.Column(db.Integer, nullable = True)
    q1 = db.Column(db.String(255), nullable = True)
    q2 = db.Column(db.String(255), nullable = True)
    q3 = db.Column(db.String(255), nullable = True)  
    
    race = db.relationship("Race", backref="qualifying_laps")
    driver = db.relationship("Driver", backref="qualifying_laps")
    constructor = db.relationship("Constructor", backref="qualifying_laps")
    

    def __repr__(self):
        return f"<QualifyingLap qualify_id={self.qualify_id} race_id={self.race_id}>"

class PitStop(db.Model):
    """A storage space."""

    __tablename__ = "pit_stops"

    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), primary_key=True, nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"), nullable = False)
    stop = db.Column(db.Integer, nullable = False)
    lap = db.Column(db.Integer, nullable = False)
    time = db.Column(db.Datetime, nullable = False)
    duration = db.Column(db.String(255), nullable = True)
    milliseconds = db.Column(db.Integer, nullable = True)

    race = db.relationship("Race", backref="pit_stops")
    driver = db.relationship("Driver", backref="pit_stops")

    def __repr__(self):
        return f"<PitStop race_id={self.race_id} driver_id={self.driver_id}>"


class Status(db.Model):
    """A storage space."""

    __tablename__ = "statuses"

    status_id = db.Column(db.Integer, primary_key=True, nullable = False)
    status = db.Column(db.String(255), nullable = False)

    results = db.relationship("Result", backref="status")
    sprint_results = db.relationship("SprintResult", backref="status")

    def __repr__(self):
        return f"<Status status_id={self.status_id} status={self.status}>"


class Driver(db.Model):
    """A storage space."""

    __tablename__ = "drivers"

    driver_id = db.Column(db.Integer, primary_key=True, nullable = False)
    driver_ref = db.Column(db.String(255), unique = True)
    number = db.Column(db.Integer, nullable = True)
    code = db.Column(db.String(3), nullable = True)
    forename = db.Column(db.String(255), nullable = False)
    surname = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.Datetime, nullable = True) 
    nationality = db.Column(db.String(255), nullable = True) 
    url = db.Column(db.String(255), nullable = False)

    lap_times = db.relationship("LapTime", back_populates="driver")
    results = db.relationship("Result", back_populates="driver")
    sprint_results = db.relationship("SprintResult", backref="driver")
    qualifying_laps = db.relationship("QualifyingLap", backref="driver")
    pit_stops = db.relationship("PitStop", backref="driver")
    driver_standings = db.relationship("DriverStanding", backref="driver")
    constructor_results = db.relationship("ConstructorResult", backref="driver")
    constructor_standings = db.relationship("ConstructorStanding", backref="driver")
    likes = db.relationship("Like", back_populates="driver")

    def __repr__(self):
        return f"<Driver driver_id={self.driver_id} surname={self.surname}>"


class DriverStanding(db.Model):
    """A storage space."""

    __tablename__ = "driver_standings"

    driver_standings_id = db.Column(db.Integer, primary_key = True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"), nullable = False)
    points = db.Column(db.Integer, nullable = False)
    position = db.Column(db.Integer, nullable = True)
    position_text = db.Column(db.String(255), nullable = True)
    wins = db.Column(db.Integer, nullable = False)
    
    race = db.relationship("Race", backref="driver_standings")
    driver = db.relationship("Driver", backref="driver_standings")

    def __repr__(self):
        return f"<DriverStanding standings_id={self.standings_id} driver_id={self.driver_id}>"


class Season(db.Model):
    """A storage space."""

    __tablename__ = "seasons"

    year = db.Column(db.Integer, nullable = False)
    url = db.Column(db.String(255), nullable = False)

    race = db.relationship("Race", backref="season")

    def __repr__(self):
        return f"<Season year={self.year} url={self.url}>"

class Constructor(db.Model):
    """Table for constructors"""

    __tablename__ = "constructors"

    constructor_id = db.Column(db.Integer, primary_key = True, nullable = False)
    constructor_ref = db.Column(db.String(255), unique = True, nullable = False)
    name = db.Column(db.String(255), nullable = False)
    nationality = db.Column(db.String)
    url = db.Column(db.url, nullable = False)

    results = db.relationship("Result", backref="constructor")
    sprint_results = db.relationship("SprintResult", backref="constructor")
    qualifying_laps = db.relationship("QualifyingLap", backref="constructor")

    def __repr__(self):
        return f"<Constructor constructor_id={self.constructor_id} name={self.name}>"

class ConstructorResult(db.Model):
    """Table for constructors"""

    __tablename__ = "constructor_results"

    constructor_result_id = db.Column(db.Integer, primary_key = True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"), nullable = False)
    points = db.Column(db.Integer, nullable = True)
    status = db.Column(db.String(255), nullable = True)


    race = db.relationship("Race", backref="constructor_results")
    driver = db.relationship("Constructor", backref="constructor_results")

    def __repr__(self):
        return f"<ConstructorResult constructor_result_id={self.constructor_result_id} name={self.name}>"

class ConstructorStanding(db.Model):
    """Table for constructors"""

    __tablename__ = "constructor_standings"

    constructor_standing_id = db.Column(db.Integer, primary_key = True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"), nullable = False)
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"), nullable = False)
    points = db.Column(db.Integer, nullable = False)
    position = db.Column(db.Integer)
    position_text = db.Column(db.String(255))
    wins = db.Column(db.Integer, nullable = False)

    race = db.relationship("Race", backref="constructor_standings")
    driver = db.relationship("Constructor", backref="constructor_standings")

    def __repr__(self):
        return f"<ConstructorStandinf constructor_standing_id={self.constructor_standing_id} race_id={self.race_id}>"


class Circuit(db.Model):
    """Table for constructors"""

    __tablename__ = "constructors"

    circuit_id = db.Column(db.Integer, primary_key = True, nullable = False)
    circuit_ref = db.Column(db.String(255), nullable = False)
    name = db.Column(db.String(255), nullable = False)
    location = db.Column(db.String(255), nullable = True)
    country = db.Column(db.String(255), nullable = True)
    lat = db.Column(db.Integer, nullable = True)
    lng = db.Column(db.Integer, nullable = True)
    alt = db.Column(db.Integer, nullable = True)
    url = db.Column(db.String(255), nullable = False)

    race = db.relationship("Race", backref="circuit")

    def __repr__(self):
        return f"<Circuit circuit_id={self.circuit_id} name={self.name}>"