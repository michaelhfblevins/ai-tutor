import numpy as np

# Define function to calculate distance given parallax
def parallax_to_distance(parallax_arcsec):
    """
    Convert stellar parallax to distance in parsecs.
    
    The fundamental equation: d = 1/p
    where d is distance in parsecs and p is parallax in arcseconds.
    """
    # Input validation - always check for invalid inputs!
    if parallax_arcsec <= 0:
        return {"error": "Parallax must be positive"}
    
    # Calculate distance using the parallax formula
    distance_pc = 1.0 / parallax_arcsec
    
    # Return as a dictionary for structured data
    # We round to 2 decimal places for readability
    return {"distance_parsecs": round(distance_pc, 2)}

# Define function to calculate stellar luminosity
def stellar_luminosity(radius_solar, temperature_k):
    """
    Calculate stellar luminosity using the Stefan-Boltzmann law.
    
    The energy radiated by a star depends on its surface area (4πR²)
    and how much energy each square meter emits (σT⁴).
    """
    # Physical constants
    stefan_boltzmann = 5.67e-8  # W m^-2 K^-4 (Stefan-Boltzmann constant)
    solar_radius = 6.96e8  # meters (Sun's radius)
    solar_luminosity = 3.83e26  # watts (Sun's total energy output)
    
    # Always validate inputs
    if radius_solar <= 0 or temperature_k <= 0:
        return {"error": "Radius and temperature must be positive"}
    
    # Convert stellar radius from solar units to meters
    radius_meters = radius_solar * solar_radius
    
    # Apply Stefan-Boltzmann law: L = 4πR²σT⁴
    luminosity_watts = 4 * np.pi * radius_meters**2 * stefan_boltzmann * temperature_k**4
    
    # Convert to solar luminosities for easier interpretation
    luminosity_solar = luminosity_watts / solar_luminosity
    
    return {
        "luminosity_solar": round(luminosity_solar, 3),
        "luminosity_watts": f"{luminosity_watts:.2e}"  # Scientific notation
    }

# Define function to search course materials
def search_course_materials(question, max_results=2):
    """
    Search tutorial materials and return relevant content.
    This function will be callable by Claude as a tool.
    """
    # Search for relevant chunks
    results = search_chunks(question, top_k=max_results)
    
    # Check if we found anything relevant
    if results[0]['similarity'] < 0.2:
        return {
            "status": "no_relevant_content",
            "message": "No relevant tutorial material found for this question"
        }
    
    # Format results for Claude
    content_parts = []
    for i, result in enumerate(results, 1):
        # Get section title
        lines = result['chunk']['text'].split('\n')
        title = lines[0] if lines else "No title"
        
        # Get content ending at complete sentence
        content_text = result['chunk']['text'][:1000]
        last_period = content_text.rfind('.')
        if last_period > 0:
            content_text = content_text[:last_period + 1]
        
        content_parts.append(f"Section {i} - {title}:\n{content_text}")
    
    # Return structured results
    return {
        "status": "found",
        "best_similarity": round(results[0]['similarity'], 3),
        "content": "\n\n".join(content_parts)
    }

# Complete tools list combining calculations and search
complete_tools = [
    {
        "name": "parallax_to_distance",
        "description": "Calculate stellar distance from parallax measurement",
        "input_schema": {
            "type": "object",
            "properties": {
                "parallax_arcsec": {
                    "type": "number",
                    "description": "Parallax in arcseconds"
                }
            },
            "required": ["parallax_arcsec"]
        }
    },
    {
        "name": "stellar_luminosity",
        "description": "Calculate stellar luminosity from radius and temperature",
        "input_schema": {
            "type": "object",
            "properties": {
                "radius_solar": {
                    "type": "number",
                    "description": "Radius in solar radii"
                },
                "temperature_k": {
                    "type": "number",
                    "description": "Temperature in Kelvin"
                }
            },
            "required": ["radius_solar", "temperature_k"]
        }
    },
    {
        "name": "search_course_materials",
        "description": "Search Part 1 tutorial notes for relevant content",
        "input_schema": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "Topic or question to search for"
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of results (default 2)",
                    "default": 2
                }
            },
            "required": ["question"]
        }
    }
]
