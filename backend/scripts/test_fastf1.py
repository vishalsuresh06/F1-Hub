import fastf1

def main():
    fastf1.Cache.enable_cache("fastf1_cache")

    session = fastf1.get_session(2024, "Bahrain", "R")
    session.load()

    print("Session:", session.event['EventName'])
    print("Drivers:", list(session.drivers)[:5])

    laps = session.laps
    print(laps[["Driver", "LapNumber", 'LapTime', 'Compound', 'Stint']].head())

if __name__ == "__main__":
    main()