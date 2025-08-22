# F1 Race Predictor Backend

This backend handles F1 race data collection, storage, and management using FastF1 API and PostgreSQL.

## Features

- ✅ **Duplicate Prevention**: Unique constraints prevent duplicate data entries
- ✅ **Progress Tracking**: Real-time progress bars and logging for data insertion
- ✅ **Error Handling**: Comprehensive error handling and recovery
- ✅ **Bulk Operations**: Efficient bulk data insertion for better performance
- ✅ **Database Indexing**: Optimized indexes for faster queries
- ✅ **Session Management**: Proper database session handling
- ✅ **Logging**: Detailed logging for debugging and monitoring

## Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the backend directory with your database credentials:

```env
INSTANCE_CONNECTION_NAME=your-project:your-region:your-instance
DB_USER=your-database-user
DB_PASS=your-database-password
DB_NAME=your-database-name
PRIVATE_IP=true  # or false for public IP
```

### 3. Database Migration

Run the migration script to set up the database schema:

```bash
python migrate_db.py
```

This will:
- Create tables if they don't exist
- Add new columns for session metadata
- Create indexes for better performance

## Usage

### Testing the Backend

Run the test script to verify everything is working:

```bash
python test_backend.py
```

This will test:
- Database connection
- Table accessibility
- Duplicate prevention functionality

### Populating the Database

To populate the database with F1 data:

```bash
python populate_db.py
```

By default, this will:
- Process the 2018 F1 season
- Limit to 1 event for testing (you can modify `max_events` parameter)
- Show progress bars for each operation
- Skip existing data to prevent duplicates
- Log all operations to `populate_db.log`

### Customizing Data Collection

You can modify the `populate_db.py` file to:

1. **Change the year**:
   ```python
   populator = DatabasePopulator(year=2023)  # Change to desired year
   ```

2. **Process more events**:
   ```python
   populator.populate_database(max_events=5)  # Process 5 events
   ```

3. **Process all events**:
   ```python
   populator.populate_database()  # Process all events
   ```

## Database Schema

### Tables

1. **Results**: Race and qualifying results
2. **Laps**: Individual lap times and data
3. **Weather**: Weather conditions during sessions
4. **Telemetry**: Car telemetry data
5. **SessionStatus**: Session status information
6. **TrackStatus**: Track status updates
7. **RaceControlMessages**: Race control messages

### Key Features

- **Unique Constraints**: Prevent duplicate entries based on session metadata
- **Indexes**: Optimized for common query patterns
- **Session Metadata**: Each record includes year, round, and session type
- **Error Recovery**: Graceful handling of insertion errors

## Monitoring and Logging

### Log Files

- `populate_db.log`: Main operation log
- Console output: Real-time progress and status

### Log Levels

- **INFO**: General operations and progress
- **WARNING**: Non-critical issues (e.g., duplicate data)
- **ERROR**: Critical errors that need attention

## Performance Optimizations

1. **Bulk Operations**: Uses `bulk_save_objects` for efficient insertion
2. **Chunked Processing**: Telemetry data is processed in chunks to avoid memory issues
3. **Database Indexes**: Optimized indexes for common query patterns
4. **Duplicate Checking**: Checks for existing data before insertion
5. **Connection Pooling**: Efficient database connection management

## Troubleshooting

### Common Issues

1. **Connection Errors**:
   - Verify your `.env` file has correct credentials
   - Check if your database instance is running
   - Ensure network connectivity

2. **Permission Errors**:
   - Verify database user has appropriate permissions
   - Check if tables can be created/modified

3. **Memory Issues**:
   - Reduce chunk size in telemetry processing
   - Process fewer events at once

4. **Duplicate Key Errors**:
   - This is expected behavior - the system prevents duplicates
   - Check logs for "skipping duplicates" messages

### Getting Help

1. Check the log files for detailed error messages
2. Run the test script to verify basic functionality
3. Ensure all dependencies are installed correctly

## API Integration

The backend is designed to work with the FastF1 Python library. It automatically:

- Loads session data from FastF1
- Handles data type conversions
- Manages database transactions
- Provides progress feedback

## Future Enhancements

- [ ] Data validation and cleaning
- [ ] Incremental updates
- [ ] Data compression for large datasets
- [ ] Real-time data streaming
- [ ] API endpoints for data access
- [ ] Data analytics and aggregation functions
