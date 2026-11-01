
# APEX AI - Lesson 2
# Business Development Lead Qualification

def qualify_lead(company_name, industry, budget):

    print("\n--- LEAD QUALIFICATION REPORT ---")
    print(f"Company: {company_name}")
    print(f"Industry: {industry}")
    print(f"Estimated Contract Value: £{budget:,}")

    if budget >= 100000:
        priority = "HIGH"
        recommendation = "Prioritise for sales outreach"

    elif budget >= 50000:
        priority = "MEDIUM"
        recommendation = "Research further before outreach"

    else:
        priority = "LOW"
        recommendation = "Monitor for future opportunities"

    print(f"Lead Priority: {priority}")
    print(f"Recommendation: {recommendation}")


def main():

    print("APEX AI - AUTONOMOUS COMMERCIAL AGENT")

    qualify_lead(
        company_name="London Commercial Properties Ltd",
        industry="Commercial Real Estate",
        budget=150000
    )


if __name__ == "__main__":
    main()
