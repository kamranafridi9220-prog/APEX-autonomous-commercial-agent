
# APEX AI - Lesson 9
# Tool-Calling Business Development Agent

import os
import json

from openai import OpenAI
from lead_scoring import calculate_lead_score


# Define the tool available to the AI model
lead_scoring_tool = {
    "type": "function",
    "name": "calculate_lead_score",
    "description": (
        "Calculate a commercial lead score using "
        "the company's business qualification rules."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "contract_value": {"type": "number"},
            "profit_margin": {"type": "number"},
            "industry_match": {"type": "boolean"},
            "location_match": {"type": "boolean"},
            "contract_months": {"type": "integer"}
        },
        "required": [
            "contract_value",
            "profit_margin",
            "industry_match",
            "location_match",
            "contract_months"
        ],
        "additionalProperties": False
    },
    "strict": True
}


def run_agent(company):
    client = OpenAI()

    prompt = (
        "Evaluate this fictional business opportunity. "
        "Use the lead scoring tool, then explain the "
        "result and recommend the next action.\n\n"
        + json.dumps(company)
    )

    # First API request: the model can request a tool
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are APEX, a B2B commercial analyst. "
            "Use the scoring tool for numerical scoring. "
            "Never invent missing company data."
        ),
        tools=[lead_scoring_tool],
        tool_choice="required",
        input=prompt
    )

    # Execute any tool calls requested by the model
    tool_outputs = []

    for item in response.output:
        if item.type == "function_call":
            if item.name != "calculate_lead_score":
                raise ValueError("Unknown tool requested")

            arguments = json.loads(item.arguments)

            score, priority = calculate_lead_score(
                **arguments
            )

            print(f"Tool executed: {item.name}")
            print(f"Score: {score}/100")
            print(f"Priority: {priority}")

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps({
                    "score": score,
                    "priority": priority
                })
            })

    if not tool_outputs:
        raise RuntimeError("Model did not request a tool")

    # Second API request: provide the tool result
    final_response = client.responses.create(
        model="gpt-4.1-mini",
        previous_response_id=response.id,
        input=tool_outputs,
        instructions=(
            "Explain the tool's actual score and priority. "
            "Provide a concise commercial recommendation. "
            "Do not invent verified customer requirements."
        ),
        tools=[lead_scoring_tool],
        tool_choice="none"
    )

    print("\nAPEX AI RECOMMENDATION")
    print("=" * 45)
    print(final_response.output_text)


def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing")

    company = {
        "name": "London Commercial Properties Ltd",
        "contract_value": 150000,
        "profit_margin": 22,
        "industry_match": True,
        "location_match": True,
        "contract_months": 36
    }

    print("APEX AI - TOOL-CALLING AGENT")
    print("=" * 45)

    run_agent(company)


if __name__ == "__main__":
    main()
