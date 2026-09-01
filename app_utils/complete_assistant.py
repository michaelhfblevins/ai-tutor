from anthropic import Anthropic
import streamlit as st
from app_utils.complete_tools import *

# Get API key
api_key = st.secrets["ANTHROPIC_API_KEY"]

def complete_assistant(messages):
    """
    Complete AI assistant that can calculate and search.
    Always returns a natural language answer.
    """

    # Get Claude's initial response
    client = Anthropic(api_key=api_key)
    initial_response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=300,
        tools=complete_tools_list,
        messages=messages
    )

    # Check if Claude needs a tool
    if initial_response.stop_reason != "tool_use":
        # Some SDKs return plain dicts when running offline; fall back to repr
        # repr() returns a string representation of the object for debugging
        text_blocks = [
            getattr(block, "text", None)
            if not isinstance(block, dict)
            else block.get("text")
            for block in getattr(initial_response, "content", [])
        ]
        text_blocks = [item for item in text_blocks if item]
        return "".join(text_blocks).strip() or repr(initial_response)

    # Execute the requested tool
    tool_use = initial_response.content[-1]

    # Execute the appropriate function
    if tool_use.name == "parallax_to_distance":
        result = parallax_to_distance(tool_use.input['parallax_arcsec'])
    elif tool_use.name == "stellar_luminosity":
        result = stellar_luminosity(
            tool_use.input['radius_solar'],
            tool_use.input['temperature_k']
        )
    elif tool_use.name == "search_course_materials":
        result = search_course_materials(
            tool_use.input['question'],
            tool_use.input.get('max_results', 2)
        )
    else:
        result = {"error": f"Unknown function: {tool_use.name}"}

    # Get natural language response
    final_response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=400,
        tools=complete_tools_list,
        messages=[
            {"role": "user", "content": question},
            {"role": "assistant", "content": initial_response.content},
            {
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": str(result)
                }]
            }
        ]
    )

    text_blocks = [
        getattr(block, "text", None)
        if not isinstance(block, dict)
        else block.get("text")
        for block in getattr(final_response, "content", [])
    ]
    text_blocks = [item for item in text_blocks if item]
    if text_blocks:
        return "".join(text_blocks).strip()

    # As a fallback, provide the raw response so readers know to run locally
    return repr(final_response)
