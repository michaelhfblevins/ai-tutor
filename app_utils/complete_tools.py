import numpy as np
from sentence_transformers import SentenceTransformer
from ..lectures import LLM_API_Basics_STIG.md


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


# **------------------------------ RAG Functions ------------------------------**

# Read in the lecture files
with open('LLM_API_Basics_STIG.md', 'r') as f:
    LLM_API_Basics_STIG = f.read()

# Define function to perform simple section-based chunking
def chunk_by_sections(text):
    """
    Split a document into chunks based on ## section headers.
    
    This function:
    1. Finds all the ## headers in the text
    2. Splits the document at these headers
    3. Keeps each section as a separate chunk
    4. Preserves the section header with its content
    """
    # Split on section headers
    # We use '\n## ' to ensure we're splitting on headers at line starts
    sections = text.split('\n## ')
    
    chunks = []
    for i, section in enumerate(sections):
        # The first section doesn't have '## ' removed (it wasn't split)
        if i == 0:
            chunk_text = section
        else:
            # Add back the '## ' that was removed during split
            chunk_text = '## ' + section
        
        # Only keep chunks with substantial content (at least 100 characters)
        if len(chunk_text.strip()) > 100:
            chunks.append({
                'text': chunk_text.strip(),
                'length': len(chunk_text),
                'chunk_id': i
            })
    
    return chunks

# Create chunks from LLM_API_Basics_STIG.md
lecture_chunks = chunk_by_sections(LLM_API_Basics_STIG)

# Create text embeddings using SentenceTransformer
# Load a pre-trained embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Create embeddings
chunk_embeddings = []

for chunk in lecture_chunks:
    # Create embedding for this chunk's text
    # The encode() method converts text to a vector
    embedding = embedding_model.encode(chunk['text'])
    chunk_embeddings.append(embedding)

# Define function to search through chunks
def search_chunks(query, top_k=3):
    """
    Find the most relevant chunks for a query using vectorized operations.
    
    This function:
    1. Converts the query to an embedding (384 numbers)
    2. Calculates similarity with all chunk embeddings using vectorized NumPy
    3. Returns the top-k most similar chunks
    
    Parameters:
    - query: The search question
    - top_k: How many results to return
    """
    # Convert query to embedding (same 384-dimensional space as chunks)
    query_embedding = embedding_model.encode(query)
    
    # Vectorized similarity calculation - much faster than a loop!
    # Convert list of embeddings to NumPy array for vectorized operations
    chunk_matrix = np.array(chunk_embeddings)
    
    # Calculate dot products with all chunks at once
    similarities = np.dot(chunk_matrix, query_embedding)
    
    # Find the indices of top-k highest similarities
    # argsort() returns indices that would sort the array
    # [-top_k:] takes the last k elements (highest values)
    # [::-1] reverses to get descending order
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    
    # Return the top chunks with their similarities
    results = []
    for idx in top_indices:
        results.append({
            'chunk': lecture_chunks[idx],
            'similarity': similarities[idx]
        })
    
    return results

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
