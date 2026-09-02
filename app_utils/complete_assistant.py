from anthropic import Anthropic
import streamlit as st
from app_utils.complete_tools import *

# Get API key
api_key = st.secrets["ANTHROPIC_API_KEY"]

def complete_assistant(conversation):
    """
    Complete AI assistant that can calculate and search.
    Takes the full conversation (including any prior tool_use/tool_result blocks),
    mutates it with this turn's exchange, and returns (final_response_text, updated_conversation).
    """

    # Get Claude's initial response
    client = Anthropic(api_key=api_key)
    initial_response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=300,
        tools=complete_tools_list,
        messages=conversation
    )

    # Check if Claude needs a tool
    if initial_response.stop_reason != "tool_use":
        conversation.append({"role": "assistant", "content": initial_response.content})
        final_response_text = "".join(
            block.text for block in initial_response.content if block.type == "text"
        )
        return final_response_text, conversation

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

    # Append initial response tool use to conversation
    conversation.append({"role": "assistant", "content": initial_response.content})
    conversation.append({
        "role": "user",
        "content": [{
            "type": "tool_result",
            "tool_use_id": tool_use.id,
            "content": str(result)
        }]
    })
    
    # Get natural language response
    final_response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=400,
        tools=complete_tools_list,
        messages=conversation
    )

    conversation.append({"role": "assistant", "content": final_response.content})
    final_response_text = "".join(
        block.text for block in final_response.content if block.type == "text"
    )
    return final_response_text, conversation
