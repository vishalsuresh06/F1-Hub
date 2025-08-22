import fastf1
import pandas as pd
from tqdm import tqdm
import logging
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from connection import connect_with_connector
from models import Results, Laps, Weather, Telemetry, SessionStatus, TrackStatus, RaceControlMessages, Base

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('populate_db.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DatabasePopulator:
    def __init__(self, year: int = 2018):
        self.year = year
        self.engine = connect_with_connector()
        self.sessions = ["FP1", "FP2", "FP3", "Q", "R"]
        
    def create_tables(self):
        """Create all tables if they don't exist"""
        try:
            Base.metadata.create_all(self.engine)
            logger.info("Database tables created successfully")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise
    
    def check_existing_data(self, session_year: int, session_round: int, session_type: str) -> Dict[str, bool]:
        """Check if data already exists for a session"""
        with Session(self.engine) as db_session:
            existing = {}
            
            # Check Results
            count = db_session.query(Results).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['results'] = count > 0
            
            # Check Laps
            count = db_session.query(Laps).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['laps'] = count > 0
            
            # Check Weather
            count = db_session.query(Weather).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['weather'] = count > 0
            
            # Check Telemetry
            count = db_session.query(Telemetry).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['telemetry'] = count > 0
            
            # Check SessionStatus
            count = db_session.query(SessionStatus).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['session_status'] = count > 0
            
            # Check TrackStatus
            count = db_session.query(TrackStatus).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['track_status'] = count > 0
            
            # Check RaceControlMessages
            count = db_session.query(RaceControlMessages).filter_by(
                session_year=session_year,
                session_round=session_round,
                session_type=session_type
            ).count()
            existing['race_control_messages'] = count > 0
            
            return existing
    
    def insert_results(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert results data with progress bar"""
        if data.empty:
            logger.info("No results data to insert")
            return
        
        results_objects = []
        for _, row in tqdm(data.iterrows(), total=len(data), desc=f"Processing Results for {session_type}"):
            try:
                result = Results(
                    driver_number=row["DriverNumber"],
                    broadcast_name=row["BroadcastName"],
                    full_name=row["FullName"],
                    abbreviation=row["Abbreviation"],
                    team_name=row["TeamName"],
                    team_color=row["TeamColor"],
                    first_name=row["FirstName"],
                    last_name=row["LastName"],
                    headshot_url=row["HeadshotURL"],
                    country_code=row["CountryCode"],
                    position=row["Position"],
                    classified_position=row["ClassifiedPosition"],
                    grid_position=row["GridPosition"],
                    q1=row["Q1"],
                    q2=row["Q2"],
                    q3=row["Q3"],
                    time=row["Time"],
                    status=row["Status"],
                    points=row["Points"],
                    laps=row["Laps"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                results_objects.append(result)
            except Exception as e:
                logger.error(f"Error processing result row: {e}")
                continue
        
        if results_objects:
            try:
                db_session.bulk_save_objects(results_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(results_objects)} results")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some results already exist for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting results: {e}")
    
    def insert_laps(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert laps data with progress bar"""
        if data.empty:
            logger.info("No laps data to insert")
            return
        
        laps_objects = []
        for _, row in tqdm(data.iterrows(), total=len(data), desc=f"Processing Laps for {session_type}"):
            try:
                lap = Laps(
                    time=row["Time"],
                    driver=row["Driver"],
                    driver_number=row["DriverNumber"],
                    lap_time=row["LapTime"],
                    lap_number=row["LapNumber"],
                    stint=row["Stint"],
                    pit_out_time=row["PitOutTime"],
                    pit_in_time=row["PitInTime"],
                    sector_1_time=row["Sector1Time"],
                    sector_2_time=row["Sector2Time"],
                    sector_3_time=row["Sector3Time"],
                    s1_session_time=row["Sector1SessionTime"],
                    s2_session_time=row["Sector2SessionTime"],
                    s3_session_time=row["Sector3SessionTime"],
                    speed_s1=row["SpeedI1"],
                    speed_s2=row["SpeedI2"],
                    speed_fl=row["SpeedFL"],
                    speed_st=row["SpeedST"],
                    is_personal_best=row["IsPersonalBest"],
                    compound=row["Compound"],
                    tyre_life=row["TyreLife"],
                    fresh_tyre=row["FreshTyre"],
                    team=row["Team"],
                    lap_start_time=row["LapStartTime"],
                    lap_start_date=row["LapStartDate"],
                    track_status=row["TrackStatus"],
                    position=row["Position"],
                    deleted=row["Deleted"],
                    deleted_reason=row["DeletedReason"],
                    fast_f1_generated=row["FastF1Generated"],
                    is_accurate=row["IsAccurate"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                laps_objects.append(lap)
            except Exception as e:
                logger.error(f"Error processing lap row: {e}")
                continue
        
        if laps_objects:
            try:
                db_session.bulk_save_objects(laps_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(laps_objects)} laps")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some laps already exist for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting laps: {e}")
    
    def insert_weather(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert weather data with progress bar"""
        if data.empty:
            logger.info("No weather data to insert")
            return
        
        weather_objects = []
        for _, row in tqdm(data.iterrows(), total=len(data), desc=f"Processing Weather for {session_type}"):
            try:
                weather = Weather(
                    time=row["Time"],
                    air_temp=row["AirTemp"],
                    humidity=row["Humidity"],
                    pressure=row["Pressure"],
                    rain_fall=row["RainFall"],
                    track_temp=row["TrackTemp"],
                    wind_direction=row["WindDirection"],
                    wind_speed=row["WindSpeed"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                weather_objects.append(weather)
            except Exception as e:
                logger.error(f"Error processing weather row: {e}")
                continue
        
        if weather_objects:
            try:
                db_session.bulk_save_objects(weather_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(weather_objects)} weather records")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some weather data already exists for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting weather data: {e}")
    
    def insert_telemetry(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert telemetry data with progress bar"""
        if data.empty:
            logger.info("No telemetry data to insert")
            return
        
        # Process telemetry in chunks to avoid memory issues
        chunk_size = 1000
        total_chunks = len(data) // chunk_size + (1 if len(data) % chunk_size else 0)
        
        for chunk_idx in tqdm(range(total_chunks), desc=f"Processing Telemetry chunks for {session_type}"):
            start_idx = chunk_idx * chunk_size
            end_idx = min((chunk_idx + 1) * chunk_size, len(data))
            chunk_data = data.iloc[start_idx:end_idx]
            
            telemetry_objects = []
            for _, row in chunk_data.iterrows():
                try:
                    telemetry = Telemetry(
                        time=row["Time"],
                        session_time=row["SessionTime"],
                        date=row["Date"],
                        source=row["Source"],
                        speed=row["Speed"],
                        rpm=row["RPM"],
                        n_gear=row["NGear"],
                        throttle=row["Throttle"],
                        brake=row["Brake"],
                        drs=row["DRS"],
                        x=row["X"],
                        y=row["Y"],
                        z=row["Z"],
                        status=row["Status"],
                        session_year=session_year,
                        session_round=session_round,
                        session_type=session_type
                    )
                    telemetry_objects.append(telemetry)
                except Exception as e:
                    logger.error(f"Error processing telemetry row: {e}")
                    continue
            
            if telemetry_objects:
                try:
                    db_session.bulk_save_objects(telemetry_objects)
                    db_session.commit()
                    logger.info(f"Successfully inserted telemetry chunk {chunk_idx + 1}/{total_chunks} ({len(telemetry_objects)} records)")
                except IntegrityError:
                    db_session.rollback()
                    logger.warning(f"Some telemetry data already exists for chunk {chunk_idx + 1}, skipping duplicates")
                except Exception as e:
                    db_session.rollback()
                    logger.error(f"Error inserting telemetry chunk {chunk_idx + 1}: {e}")
    
    def insert_session_status(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert session status data"""
        if data.empty:
            logger.info("No session status data to insert")
            return
        
        status_objects = []
        for _, row in data.iterrows():
            try:
                status = SessionStatus(
                    time=row["Time"],
                    status=row["Status"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                status_objects.append(status)
            except Exception as e:
                logger.error(f"Error processing session status row: {e}")
                continue
        
        if status_objects:
            try:
                db_session.bulk_save_objects(status_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(status_objects)} session status records")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some session status data already exists for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting session status: {e}")
    
    def insert_track_status(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert track status data"""
        if data.empty:
            logger.info("No track status data to insert")
            return
        
        track_objects = []
        for _, row in data.iterrows():
            try:
                track = TrackStatus(
                    time=row["Time"],
                    status=row["Status"],
                    message=row["Message"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                track_objects.append(track)
            except Exception as e:
                logger.error(f"Error processing track status row: {e}")
                continue
        
        if track_objects:
            try:
                db_session.bulk_save_objects(track_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(track_objects)} track status records")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some track status data already exists for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting track status: {e}")
    
    def insert_race_control_messages(self, db_session: Session, data: pd.DataFrame, session_year: int, session_round: int, session_type: str):
        """Insert race control messages data"""
        if data.empty:
            logger.info("No race control messages data to insert")
            return
        
        message_objects = []
        for _, row in data.iterrows():
            try:
                message = RaceControlMessages(
                    time=row["Time"],
                    category=row["Category"],
                    message=row["Message"],
                    status=row["Status"],
                    flag=row["Flag"],
                    scope=row["Scope"],
                    sector=row["Sector"],
                    racing_number=row["RacingNumber"],
                    lap=row["Lap"],
                    session_year=session_year,
                    session_round=session_round,
                    session_type=session_type
                )
                message_objects.append(message)
            except Exception as e:
                logger.error(f"Error processing race control message row: {e}")
                continue
        
        if message_objects:
            try:
                db_session.bulk_save_objects(message_objects)
                db_session.commit()
                logger.info(f"Successfully inserted {len(message_objects)} race control message records")
            except IntegrityError:
                db_session.rollback()
                logger.warning(f"Some race control messages already exist for {session_type}, skipping duplicates")
            except Exception as e:
                db_session.rollback()
                logger.error(f"Error inserting race control messages: {e}")
    
    def process_session(self, session_year: int, session_round: int, session_type: str, event_name: str):
        """Process a single session with all data types"""
        logger.info(f"Processing {event_name} - {session_type} (Round {session_round})")
        
        try:
            # Load session data
            session = fastf1.get_session(session_year, session_round, session_type)
            session.load()
            
            # Check existing data
            existing_data = self.check_existing_data(session_year, session_round, session_type)
            
            with Session(self.engine) as db_session:
                # Process each data type
                if not existing_data.get('results', False):
                    self.insert_results(db_session, session.results, session_year, session_round, session_type)
                else:
                    logger.info(f"Results data already exists for {session_type}, skipping")
                
                if not existing_data.get('laps', False):
                    self.insert_laps(db_session, session.laps, session_year, session_round, session_type)
                else:
                    logger.info(f"Laps data already exists for {session_type}, skipping")
                
                if not existing_data.get('weather', False):
                    self.insert_weather(db_session, session.weather_data, session_year, session_round, session_type)
                else:
                    logger.info(f"Weather data already exists for {session_type}, skipping")
                
                if not existing_data.get('telemetry', False):
                    if hasattr(session, 'telemetry') and not session.telemetry.empty:
                        self.insert_telemetry(db_session, session.telemetry, session_year, session_round, session_type)
                    else:
                        logger.info(f"No telemetry data available for {session_type}")
                else:
                    logger.info(f"Telemetry data already exists for {session_type}, skipping")
                
                if not existing_data.get('session_status', False):
                    self.insert_session_status(db_session, session.session_status, session_year, session_round, session_type)
                else:
                    logger.info(f"Session status data already exists for {session_type}, skipping")
                
                if not existing_data.get('track_status', False):
                    self.insert_track_status(db_session, session.track_status, session_year, session_round, session_type)
                else:
                    logger.info(f"Track status data already exists for {session_type}, skipping")
                
                if not existing_data.get('race_control_messages', False):
                    self.insert_race_control_messages(db_session, session.race_control_messages, session_year, session_round, session_type)
                else:
                    logger.info(f"Race control messages already exist for {session_type}, skipping")
            
            logger.info(f"Successfully processed {event_name} - {session_type}")
            
        except Exception as e:
            logger.error(f"Error processing {event_name} - {session_type}: {e}")
    
    def populate_database(self, max_events: int = None):
        """Main method to populate the database"""
        logger.info(f"Starting database population for year {self.year}")
        
        # Create tables
        self.create_tables()
        
        # Get event schedule
        event_schedule = fastf1.get_event_schedule(self.year)
        event_schedule = event_schedule[event_schedule["EventFormat"] == "conventional"]
        
        if max_events:
            event_schedule = event_schedule.head(max_events)
        
        total_events = len(event_schedule)
        total_sessions = total_events * len(self.sessions)
        
        logger.info(f"Processing {total_events} events with {len(self.sessions)} sessions each ({total_sessions} total sessions)")
        
        session_count = 0
        for index, row in tqdm(event_schedule.iterrows(), total=total_events, desc="Processing Events"):
            event_name = row["EventName"]
            round_number = row["RoundNumber"]
            
            logger.info(f"Processing event {index + 1}/{total_events}: {event_name}")
            
            for session_type in self.sessions:
                session_count += 1
                logger.info(f"Processing session {session_count}/{total_sessions}: {session_type}")
                
                try:
                    self.process_session(self.year, round_number, session_type, event_name)
                except Exception as e:
                    logger.error(f"Failed to process {event_name} - {session_type}: {e}")
                    continue
        
        logger.info("Database population completed!")

def main():
    """Main function to run the database population"""
    try:
        # Initialize populator
        populator = DatabasePopulator(year=2018)
        
        # Populate database (limit to 1 event for testing)
        populator.populate_database(max_events=1)
        
    except Exception as e:
        logger.error(f"Fatal error during database population: {e}")
        raise

if __name__ == "__main__":
    main()


