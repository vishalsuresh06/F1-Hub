import logging
from sqlalchemy.orm import Session
from sqlalchemy import text
from connection import connect_with_connector
from models import Results, Laps, Weather, Base

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_connection():
    """Test database connection"""
    try:
        engine = connect_with_connector()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("Database connection successful!")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False

def test_tables():
    """Test if tables exist and can be queried"""
    try:
        engine = connect_with_connector()
        
        # Test each table
        tables = [Results, Laps, Weather]
        
        for table in tables:
            with Session(engine) as session:
                count = session.query(table).count()
                logger.info(f"Table {table.__tablename__}: {count} records")
        
        logger.info("All tables accessible!")
        return True
    except Exception as e:
        logger.error(f"Table test failed: {e}")
        return False

def test_insert_and_duplicate_prevention():
    """Test duplicate prevention by trying to insert the same data twice"""
    try:
        engine = connect_with_connector()
        
        with Session(engine) as session:
            # Try to insert a test result
            test_result = Results(
                driver_number="TEST_DRIVER",
                broadcast_name="Test Driver",
                full_name="Test Driver Full",
                abbreviation="TST",
                team_name="Test Team",
                team_color="#FF0000",
                first_name="Test",
                last_name="Driver",
                headshot_url="",
                country_code="TST",
                position=1.0,
                classified_position="1",
                grid_position="1",
                q1=None,
                q2=None,
                q3=None,
                time=None,
                status="Finished",
                points=25.0,
                laps=50.0,
                session_year=9999,
                session_round=999,
                session_type="TEST"
            )
            
            session.add(test_result)
            session.commit()
            logger.info("First insert successful")
            
            # Try to insert the same data again (should fail due to unique constraint)
            try:
                duplicate_result = Results(
                    driver_number="TEST_DRIVER",
                    broadcast_name="Test Driver",
                    full_name="Test Driver Full",
                    abbreviation="TST",
                    team_name="Test Team",
                    team_color="#FF0000",
                    first_name="Test",
                    last_name="Driver",
                    headshot_url="",
                    country_code="TST",
                    position=1.0,
                    classified_position="1",
                    grid_position="1",
                    q1=None,
                    q2=None,
                    q3=None,
                    time=None,
                    status="Finished",
                    points=25.0,
                    laps=50.0,
                    session_year=9999,
                    session_round=999,
                    session_type="TEST"
                )
                
                session.add(duplicate_result)
                session.commit()
                logger.error("Duplicate insert should have failed!")
                return False
                
            except Exception as e:
                session.rollback()
                logger.info("Duplicate prevention working correctly!")
            
            # Clean up test data
            session.query(Results).filter_by(
                driver_number="TEST_DRIVER",
                session_year=9999,
                session_round=999,
                session_type="TEST"
            ).delete()
            session.commit()
            logger.info("Test data cleaned up")
            
        return True
    except Exception as e:
        logger.error(f"Duplicate prevention test failed: {e}")
        return False

def main():
    """Run all tests"""
    logger.info("Starting backend tests...")
    
    tests = [
        ("Database Connection", test_connection),
        ("Table Access", test_tables),
        ("Duplicate Prevention", test_insert_and_duplicate_prevention)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        logger.info(f"\n--- Running {test_name} Test ---")
        try:
            if test_func():
                logger.info(f"✅ {test_name} PASSED")
                passed += 1
            else:
                logger.error(f"❌ {test_name} FAILED")
        except Exception as e:
            logger.error(f"❌ {test_name} FAILED with exception: {e}")
    
    logger.info(f"\n--- Test Results ---")
    logger.info(f"Passed: {passed}/{total}")
    
    if passed == total:
        logger.info("🎉 All tests passed! Backend is working correctly.")
    else:
        logger.error("⚠️  Some tests failed. Please check the logs above.")

if __name__ == "__main__":
    main()
