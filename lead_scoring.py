
# APEX AI - Lesson 4
# Multi-Factor Lead Qualification Engine

def calculate_lead_score(
    contract_value,
    profit_margin,
    industry_match,
    location_match,
    contract_months
):
    score = 0

    # Contract value: maximum 25 points
    if contract_value >= 100000:
        score += 25
    elif contract_value >= 50000:
        score += 15
    else:
        score += 5

    # Profit margin: maximum 25 points
    if profit_margin >= 20:
        score += 25
    elif profit_margin >= 10:
        score += 15
    else:
        score += 5

    # Industry compatibility: maximum 20 points
    if industry_match:
        score += 20

    # Geographic compatibility: maximum 15 points
    if location_match:
        score += 15

    # Contract duration: maximum 15 points
    if contract_months >= 24:
        score += 15
    elif contract_months >= 12:
        score += 10
    else:
        score += 5

    if score >= 80:
        priority = "HIGH"
    elif score >= 50:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    return score, priority


if __name__ == "__main__":
    score, priority = calculate_lead_score(
        contract_value=150000,
        profit_margin=22,
        industry_match=True,
        location_match=True,
        contract_months=36
    )

    print("APEX AI - LEAD SCORING ENGINE")
    print(f"Lead Score: {score}/100")
    print(f"Lead Priority: {priority}")
