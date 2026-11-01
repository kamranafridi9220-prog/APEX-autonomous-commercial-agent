
# APEX AI - Lesson 5
# Integrated Commercial Lead Intelligence

from lead_scoring import calculate_lead_score


def analyse_opportunity(company):

    print("\n" + "=" * 50)
    print("APEX AI - COMMERCIAL OPPORTUNITY ANALYSIS")
    print("=" * 50)

    score, priority = calculate_lead_score(
        contract_value=company["contract_value"],
        profit_margin=company["profit_margin"],
        industry_match=company["industry_match"],
        location_match=company["location_match"],
        contract_months=company["contract_months"]
    )

    print(f"Company: {company['name']}")
    print(f"Industry: {company['industry']}")
    print(f"Contract Value: £{company['contract_value']:,}")
    print(f"Estimated Profit Margin: {company['profit_margin']}%")
    print(f"Lead Score: {score}/100")
    print(f"Lead Priority: {priority}")

    if priority == "HIGH":
        recommendation = "Prepare a commercial proposal"
    elif priority == "MEDIUM":
        recommendation = "Conduct further qualification"
    else:
        recommendation = "Monitor opportunity"

    print(f"Recommendation: {recommendation}")

    return {
        "company": company["name"],
        "score": score,
        "priority": priority,
        "recommendation": recommendation
    }


def main():

    company = {
        "name": "London Commercial Properties Ltd",
        "industry": "Commercial Real Estate",
        "contract_value": 150000,
        "profit_margin": 22,
        "industry_match": True,
        "location_match": True,
        "contract_months": 36
    }

    analyse_opportunity(company)


if __name__ == "__main__":
    main()
