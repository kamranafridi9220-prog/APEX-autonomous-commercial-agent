
# APEX AI - Lesson 8
# Integrated Commercial Intelligence Engine

from lead_scoring import calculate_lead_score
from ai_agent import analyse_company


def generate_commercial_report(company):

    print("=" * 55)
    print("APEX AI - INTEGRATED COMMERCIAL INTELLIGENCE")
    print("=" * 55)

    # Step 1: Calculate the numerical lead score
    score, priority = calculate_lead_score(
        contract_value=company["contract_value"],
        profit_margin=company["profit_margin"],
        industry_match=company["industry_match"],
        location_match=company["location_match"],
        contract_months=company["contract_months"]
    )

    print(f"\nCompany: {company['name']}")
    print(f"Lead Score: {score}/100")
    print(f"Priority: {priority}")

    # Step 2: Generate the AI assessment
    print("\nGenerating AI commercial assessment...\n")

    ai_report = analyse_company(company)

    print(ai_report)

    return {
        "company": company["name"],
        "score": score,
        "priority": priority,
        "ai_report": ai_report
    }


if __name__ == "__main__":

    company = {
        "name": "London Commercial Properties Ltd",
        "industry": "Commercial Real Estate",
        "contract_value": 150000,
        "profit_margin": 22,
        "industry_match": True,
        "location_match": True,
        "contract_months": 36
    }

    generate_commercial_report(company)
