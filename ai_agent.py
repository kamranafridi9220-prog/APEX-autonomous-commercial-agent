
# APEX AI - Lesson 7
# First AI-Powered Business Development Analyst

import os
from openai import OpenAI


def analyse_company(company):

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OpenAI API key is missing")

    client = OpenAI()

    prompt = f"""
    Analyse this fictional business opportunity:

    Company: {company['name']}
    Industry: {company['industry']}
    Estimated Contract Value: £{company['contract_value']:,}
    Estimated Profit Margin: {company['profit_margin']}%
    Contract Duration: {company['contract_months']} months

    Produce a concise commercial report covering:

    1. Business opportunity assessment
    2. Potential customer security requirements
    3. Commercial risks
    4. Recommended sales strategy
    5. Three practical next actions

    Clearly distinguish supplied facts from assumptions.
    Do not invent verified customer requirements.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are APEX AI, an expert B2B "
            "business development analyst specialising "
            "in corporate sales and commercial strategy. "
            "Identify uncertainty and avoid unsupported claims."
        ),
        input=prompt,
        max_output_tokens=700
    )

    return response.output_text


def main():

    company = {
        "name": "London Commercial Properties Ltd",
        "industry": "Commercial Real Estate",
        "contract_value": 150000,
        "profit_margin": 22,
        "contract_months": 36
    }

    print("APEX AI - BUSINESS DEVELOPMENT AGENT")
    print("=" * 45)

    report = analyse_company(company)
    print(report)


if __name__ == "__main__":
    main()
