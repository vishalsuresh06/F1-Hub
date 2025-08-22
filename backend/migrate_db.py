import logging
from sqlalchemy import text
from connection import connect_with_connector
from models import Base

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def migrate_database():
    """Migrate the database to add new columns and constraints"""
    engine = connect_with_connector()
    
    try:
        with engine.connect() as conn:
            # Add new columns to existing tables
            tables_to_migrate = [
                'results',
                'laps', 
                'weather',
                'telemetry',
                'session_status',
                'track_status',
                'race_control_messages'
            ]
            
            for table in tables_to_migrate:
                logger.info(f"Migrating table: {table}")
                
                # Add session metadata columns
                try:
                    conn.execute(text(f"""
                        ALTER TABLE {table} 
                        ADD COLUMN IF NOT EXISTS session_year INTEGER
                    """))
                    logger.info(f"Added session_year column to {table}")
                except Exception as e:
                    logger.warning(f"Could not add session_year to {table}: {e}")
                
                try:
                    conn.execute(text(f"""
                        ALTER TABLE {table} 
                        ADD COLUMN IF NOT EXISTS session_round INTEGER
                    """))
                    logger.info(f"Added session_round column to {table}")
                except Exception as e:
                    logger.warning(f"Could not add session_round to {table}: {e}")
                
                try:
                    conn.execute(text(f"""
                        ALTER TABLE {table} 
                        ADD COLUMN IF NOT EXISTS session_type VARCHAR
                    """))
                    logger.info(f"Added session_type column to {table}")
                except Exception as e:
                    logger.warning(f"Could not add session_type to {table}: {e}")
            
            # Create indexes for better performance
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_results_session 
                    ON results (session_year, session_round, session_type)
                """))
                logger.info("Created index for results table")
            except Exception as e:
                logger.warning(f"Could not create results index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_laps_session 
                    ON laps (session_year, session_round, session_type)
                """))
                logger.info("Created index for laps table")
            except Exception as e:
                logger.warning(f"Could not create laps index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_laps_driver 
                    ON laps (driver_number, session_year, session_round)
                """))
                logger.info("Created driver index for laps table")
            except Exception as e:
                logger.warning(f"Could not create laps driver index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_weather_session 
                    ON weather (session_year, session_round, session_type)
                """))
                logger.info("Created index for weather table")
            except Exception as e:
                logger.warning(f"Could not create weather index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_telemetry_session 
                    ON telemetry (session_year, session_round, session_type)
                """))
                logger.info("Created index for telemetry table")
            except Exception as e:
                logger.warning(f"Could not create telemetry index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_telemetry_source 
                    ON telemetry (source, session_year, session_round)
                """))
                logger.info("Created source index for telemetry table")
            except Exception as e:
                logger.warning(f"Could not create telemetry source index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_session_status_session 
                    ON session_status (session_year, session_round, session_type)
                """))
                logger.info("Created index for session_status table")
            except Exception as e:
                logger.warning(f"Could not create session_status index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_track_status_session 
                    ON track_status (session_year, session_round, session_type)
                """))
                logger.info("Created index for track_status table")
            except Exception as e:
                logger.warning(f"Could not create track_status index: {e}")
            
            try:
                conn.execute(text("""
                    CREATE INDEX IF NOT EXISTS idx_race_control_session 
                    ON race_control_messages (session_year, session_round, session_type)
                """))
                logger.info("Created index for race_control_messages table")
            except Exception as e:
                logger.warning(f"Could not create race_control_messages index: {e}")
            
            conn.commit()
            logger.info("Database migration completed successfully!")
            
    except Exception as e:
        logger.error(f"Error during migration: {e}")
        raise

def create_tables_if_not_exist():
    """Create tables if they don't exist"""
    try:
        engine = connect_with_connector()
        Base.metadata.create_all(engine)
        logger.info("Tables created successfully")
    except Exception as e:
        logger.error(f"Error creating tables: {e}")
        raise

if __name__ == "__main__":
    logger.info("Starting database migration...")
    
    # First create tables if they don't exist
    create_tables_if_not_exist()
    
    # Then run migration
    migrate_database()
    
    logger.info("Migration process completed!")
