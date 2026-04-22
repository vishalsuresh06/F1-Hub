from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import fastf1


CACHE_DIR = Path(__file__).resolve().parents[1] / "fastf1_cache"
SESSION_TYPES = ("FP1", "FP2", "FP3", "Q", "R")
START_YEAR = 2019
END_YEAR = 2026
REQUEST_DELAY_SECONDS = 1


def populate_cache() -> None:
    fastf1.Cache.enable_cache(str(CACHE_DIR))
    fastf1.set_log_level("ERROR")

    for year in range(START_YEAR, END_YEAR + 1):
        try:
            event_schedule = fastf1.get_event_schedule(year)
        except Exception as exc:
            print(f"[{year}] Failed to fetch event schedule: {exc}")
            continue

        conventional_events = event_schedule[
            event_schedule["EventFormat"] == "conventional"
        ]

        if conventional_events.empty:
            print(f"[{year}] No conventional events found")
            continue

        for event in conventional_events["EventName"]:
            print(f"[{year}] Caching {event}")

            for session_type in SESSION_TYPES:
                try:
                    session = fastf1.get_session(year, event, session_type)
                    session.load()
                    print(f"  - {session_type}: ok")
                except Exception as exc:
                    print(f"  - {session_type}: skipped ({exc})")
                finally:
                    time.sleep(REQUEST_DELAY_SECONDS)


if __name__ == "__main__":
    populate_cache()
