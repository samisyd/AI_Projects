# 🗓️ Pretend this is Jeff's Calendar - mocking
FAKE_AVAILABILITY = {
    "2026-04-09": "Available from 4:00 PM to 6:00 PM",
    "2026-04-10": "Available from 10:00 AM to 12:00 PM",
    "2026-04-11": "Available from 11:00 AM to 12:00 PM",
    "2026-04-12": "Busy all afternoon (1:00 PM to 5:00 PM)",
    "2026-04-13": "Available all day",
}

# docstring for the tool function is very very important to help the agent understand how to use 
# the tool and what kind of input it expects and what kind of output it will return. This is 
# crucial for the agent to be able to effectively utilize the tool in its reasoning process 
# and provide accurate responses to user queries about Jeff's schedule.
def get_availability(date_str: str) -> dict[str, str]:
    """
    Simulates checking Jeff's availability on a specific date.

    Args:
        date_str (str): A date in 'YYYY-MM-DD' format.

    Returns:
        dict: A small JSON-like dictionary with availability info.
    """

    if not date_str:
        return {"status": "error", "message": "No date provided."}

    availability = FAKE_AVAILABILITY.get(date_str)

    if availability:
        return {
            "status": "completed",
            "message": f"On {date_str}, Jeff is {availability}.",
        }

    return {
        "status": "input_required",
        "message": f"He is not available on {date_str}. Please ask about another date.",
    }