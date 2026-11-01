
# APEX AI - Lesson 6
# Multi-Company Opportunity Ranking

from lead_scoring import calculate_lead_score


def rank_opportunities(companies):
    results = []

    for company in companies:
        score, priority = calculate_lead_score(
            contract_value=company["contract_value"],
            profit_margin=company["profit_margin"],
            industry_match=company["industry_match"],
            location_match=company["location_match"],
            contract_months=company["contract_months"]
        )

        results.append({
            "name": company["name"],
            "score": score,
            "priority": priority
        })

    results.sort(
        key=lambda company: company["score"],
        reverse=True
    )

    return results


def main():
    companies = [
        {
            "name": "London Commercial Properties Ltd",
            "contract_value": 150000,
            "profit_margin": 22,
            "industry_match": True,
            "location_match": True,
            "contract_months": 36
        },
        {
            "name": "Metro Retail Group",
            "contract_value": 80000,
            "profit_margin": 15,
            "industry_match": True,
            "location_match": True,
            "contract_months": 12
        },
        {
            "name": "Northern Logistics Ltd",
            "contract_value": 200000,
            "profit_margin": 8,
            "industry_match": True,
            "location_match": False,
            "contract_months": 24
        },
        {
            "name": "City Hospitality Group",
            "contract_value": 45000,
            "profit_margin": 12,
            "industry_match": True,
            "location_match": True,
            "contract_months": 6
        },
        {
            "name": "Regional Manufacturing Ltd",
            "contract_value": 120000,
            "profit_margin": 25,
            "industry_match": False,
            "location_match": False,
            "contract_months": 36
        }
    ]

    ranked = rank_opportunities(companies)

    print("\nAPEX AI - OPPORTUNITY RANKING")
    print("=" * 50)

    for position, company in enumerate(ranked, start=1):
        print(
            f"{position}. {company['name']} | "
            f"Score: {company['score']}/100 | "
            f"Priority: {company['priority']}"
        )


if __name__ == "__main__":
    main()
