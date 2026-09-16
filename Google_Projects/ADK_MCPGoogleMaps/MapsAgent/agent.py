import os
import requests
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

import os
load_dotenv()
MAPS_API_KEY = os.getenv("MAPS_API_KEY")


def search_places_on_route(origin: str, destination: str, place_type: str) -> dict:
    """Search for places along the route between two locations near the route midpoint.

    Args:
        origin (str): Starting location address or landmark.
        destination (str): Destination address or landmark.
        place_type (str): Keyword or place type to search for (e.g., 'gas station', 'coffee', 'hotel').

    Returns:
        dict: Status and list of matching places found near the route midpoint.
    """
    if not MAPS_API_KEY:
        return {"status": "ERROR", "error": "MAPS_API_KEY environment variable is not set."}

    # 1. Get route directions to calculate midpoint
    try:
        dir_response = requests.get(
            "https://maps.googleapis.com/maps/api/directions/json",
            params={
                "origin": origin,
                "destination": destination,
                "key": MAPS_API_KEY,
            },
            timeout=20,
        )
        dir_response.raise_for_status()
        dir_data = dir_response.json()
    except Exception as e:
        return {"status": "ERROR", "error": f"Failed to fetch directions: {str(e)}"}

    if dir_data.get("status") != "OK" or not dir_data.get("routes"):
        return {
            "status": dir_data.get("status", "ERROR"),
            "error": dir_data.get("error_message", "Could not find a valid route between locations."),
        }

    # 2. Extract midpoint coordinates from the route steps
    try:
        steps = dir_data["routes"][0]["legs"][0]["steps"]
        mid_point = steps[len(steps) // 2]["end_location"]
        lat, lng = mid_point["lat"], mid_point["lng"]
    except (IndexError, KeyError):
        return {"status": "ERROR", "error": "Failed to parse route steps for midpoint location."}

    # 3. Query Places Nearby Search API around midpoint
    try:
        places_response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
            params={
                "location": f"{lat},{lng}",
                "radius": 5000,  # 5 km radius search
                "keyword": place_type,
                "key": MAPS_API_KEY,
            },
            timeout=20,
        )
        places_response.raise_for_status()
        places_data = places_response.json()
    except Exception as e:
        return {"status": "ERROR", "error": f"Failed to search nearby places: {str(e)}"}

    if places_data.get("status") not in ["OK", "ZERO_RESULTS"]:
        return {
            "status": places_data.get("status", "ERROR"),
            "error": places_data.get("error_message", "Place search query failed."),
        }

    # 4. Parse top results
    results = []
    for place in places_data.get("results", [])[:5]:
        results.append({
            "name": place.get("name"),
            "address": place.get("vicinity"),
            "rating": place.get("rating", "N/A"),
            "user_ratings_total": place.get("user_ratings_total", 0),
            "open_now": place.get("opening_hours", {}).get("open_now"),
        })

    return {
        "status": "OK",
        "origin": origin,
        "destination": destination,
        "search_keyword": place_type,
        "total_found": len(results),
        "places": results,
    }

# Google Maps - Directions API Call
def get_directions(origin: str, destination: str, mode: str = "driving") -> dict:
    """Get route summary using Google Directions API."""
    url = "https://maps.googleapis.com/maps/api/directions/json"
    
    try:
        r = requests.get(
            url,
            params={
                "origin": origin,
                "destination": destination,
                "mode": mode,
                "key": MAPS_API_KEY
            },
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()

        # Fix: Properly check status and routes presence
        if data.get("status") != "OK" or not data.get("routes"):
            return {
                "status": data.get("status", "ERROR"),
                "error": data.get("error_message", "No route found")
            }

        leg = data["routes"][0]["legs"][0]
        
        # Construct shareable Google Maps Web Link
        encoded_origin = requests.utils.quote(origin)
        encoded_dest = requests.utils.quote(destination)
        maps_link = f"https://www.google.com/maps/dir/?api=1&origin={encoded_origin}&destination={encoded_dest}&travelmode={mode}"

        return {
            "status": "OK",
            "origin": leg["start_address"],
            "destination": leg["end_address"],
            "distance": leg["distance"]["text"],
            "duration": leg["duration"]["text"],
            "maps_url": maps_link
        }

    except Exception as e:
        return {"status": "ERROR", "error": str(e)}


# Agent Setup
directions_tool = FunctionTool(get_directions)
places_tool = FunctionTool(search_places_on_route)

root_agent = LlmAgent(
    model="gemini-3.6-flash",
    name="Maps_Agent",    
    instruction=(
        "You are a helpful Maps assistant.\n"
        "Use appropriate tools to answer user's query:\n"
        "1) TOOL: Get directions between two locations\n"
        "2) TOOL: Search for nearby places along a route\n"
        "Always return a short answer + the Google Maps link if applicable"
    ),
    tools=[directions_tool, places_tool]
)