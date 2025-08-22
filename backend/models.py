from sqlalchemy import Column, Integer, String, Float, Interval, Boolean, DateTime, UniqueConstraint, Index
from sqlalchemy.types import TIMESTAMP as Timestamp
from sqlalchemy.orm import declarative_base, Session
from connection import connect_with_connector

Base = declarative_base()

class Results(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True)
    
    # Add unique constraint to prevent duplicates
    driver_number = Column(String)
    broadcast_name = Column(String)
    full_name = Column(String)
    abbreviation = Column(String)
    team_name = Column(String)
    team_color = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    headshot_url = Column(String)
    country_code = Column(String)
    position = Column(Float)
    classified_position = Column(String)
    grid_position = Column(String)
    q1 = Column(Interval)
    q2 = Column(Interval)
    q3 = Column(Interval)
    time = Column(Interval)
    status = Column(String)
    points = Column(Float)
    laps = Column(Float)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('driver_number', 'session_year', 'session_round', 'session_type', name='unique_result'),
        Index('idx_results_session', 'session_year', 'session_round', 'session_type'),
    )

class Laps(Base):
    __tablename__ = "laps"
    id = Column(Integer, primary_key=True)

    time = Column(Interval)
    driver = Column(String)
    driver_number = Column(String)
    lap_time = Column(Interval)
    lap_number = Column(Float)
    stint = Column(Float)
    pit_out_time = Column(Interval)
    pit_in_time = Column(Interval)
    sector_1_time = Column(Interval)
    sector_2_time = Column(Interval)
    sector_3_time = Column(Interval)
    s1_session_time = Column(Interval)
    s2_session_time = Column(Interval)
    s3_session_time = Column(Interval)
    speed_s1 = Column(Float)
    speed_s2 = Column(Float)
    speed_fl = Column(Float)
    speed_st = Column(Float)
    is_personal_best = Column(Boolean)
    compound = Column(String)
    tyre_life = Column(Float)
    fresh_tyre = Column(Boolean)
    team = Column(String)
    lap_start_time = Column(Interval)
    lap_start_date = Column(Timestamp)
    track_status = Column(String)
    position = Column(Float)
    deleted = Column(Boolean)
    deleted_reason = Column(String)
    fast_f1_generated = Column(Boolean)
    is_accurate = Column(Boolean)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('driver_number', 'lap_number', 'session_year', 'session_round', 'session_type', name='unique_lap'),
        Index('idx_laps_session', 'session_year', 'session_round', 'session_type'),
        Index('idx_laps_driver', 'driver_number', 'session_year', 'session_round'),
    )

class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True)

    time = Column(Interval)
    air_temp = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
    rain_fall = Column(Boolean)
    track_temp = Column(Float)
    wind_direction = Column(Integer)
    wind_speed = Column(Float)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('time', 'session_year', 'session_round', 'session_type', name='unique_weather'),
        Index('idx_weather_session', 'session_year', 'session_round', 'session_type'),
    )

class Telemetry(Base):
    __tablename__ = "telemetry"
    id = Column(Integer, primary_key=True)

    time = Column(Interval)
    session_time = Column(Interval)
    date = Column(DateTime)
    source = Column(String)
    speed = Column(Float)
    rpm = Column(Float)
    n_gear = Column(Integer)
    throttle = Column(Float)
    brake = Column(Boolean)
    drs = Column(Integer)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)
    status = Column(String)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('time', 'source', 'session_year', 'session_round', 'session_type', name='unique_telemetry'),
        Index('idx_telemetry_session', 'session_year', 'session_round', 'session_type'),
        Index('idx_telemetry_source', 'source', 'session_year', 'session_round'),
    )

class SessionStatus(Base):
    __tablename__ = "session_status"
    id = Column(Integer, primary_key=True)

    time = Column(Interval)
    status = Column(String)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('time', 'session_year', 'session_round', 'session_type', name='unique_session_status'),
        Index('idx_session_status_session', 'session_year', 'session_round', 'session_type'),
    )

class TrackStatus(Base):
    __tablename__ = "track_status"
    id = Column(Integer, primary_key=True)

    time = Column(Interval)
    status = Column(String)
    message = Column(String)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('time', 'session_year', 'session_round', 'session_type', name='unique_track_status'),
        Index('idx_track_status_session', 'session_year', 'session_round', 'session_type'),
    )

class RaceControlMessages(Base):
    __tablename__ = "race_control_messages"
    id = Column(Integer, primary_key=True)

    time = Column(Timestamp)
    category = Column(String)
    message = Column(String)
    status = Column(String)
    flag = Column(String)
    scope = Column(String)
    sector = Column(Integer)
    racing_number = Column(String)
    lap = Column(Integer)
    
    # Add session metadata for duplicate prevention
    session_year = Column(Integer)
    session_round = Column(Integer)
    session_type = Column(String)
    
    # Create unique constraint to prevent duplicates
    __table_args__ = (
        UniqueConstraint('time', 'category', 'message', 'session_year', 'session_round', 'session_type', name='unique_race_control'),
        Index('idx_race_control_session', 'session_year', 'session_round', 'session_type'),
    )