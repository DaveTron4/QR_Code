from datetime import datetime, timedelta
import pytz

def handle_date_time(date, time, timezone='UTC', duration=None):
    # Combine date and time
    raw_datetime = f"{date}T{time}"

    # Parse the input datetime
    dt_object = datetime.strptime(raw_datetime, "%Y-%m-%dT%H:%M")

    # Apply the user's selected timezone (convert local time to UTC)
    tz = pytz.timezone(timezone)
    localized_dt = tz.localize(dt_object)  # Localize the datetime to the selected timezone

    # Convert the localized time to UTC
    dtstart_utc = localized_dt.astimezone(pytz.UTC)

    # Calculate the end time if duration is provided
    if duration:
        # Duration is expected to be in a format like '1 hour' or '30 minutes'
        duration_parts = duration.lower().split()
        num = int(duration_parts[0])
        unit = duration_parts[1]

        # Map duration to timedelta
        if unit in ['hour', 'hours']:
            duration_timedelta = timedelta(hours=num)
        elif unit in ['minute', 'minutes']:
            duration_timedelta = timedelta(minutes=num)
        else:
            raise ValueError("Unsupported duration unit")

        # Calculate end time by adding the duration to the start time
        end_time_utc = dtstart_utc + duration_timedelta
    else:
        end_time_utc = dtstart_utc

    # Format the start and end times to the required iCalendar format (UTC time with 'Z')
    dtstart = dtstart_utc.strftime("%Y%m%dT%H%M%SZ")
    dtend = end_time_utc.strftime("%Y%m%dT%H%M%SZ")

    return dtstart, dtend
