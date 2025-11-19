#!/usr/bin/env python3
"""
Example script demonstrating basic usage of SigmaXim Prospecter V3.

This script shows how to:
1. Initialize the prospecter
2. Create leads
3. Process and score leads
4. Display results

Run this script with:
    python scripts/example.py
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.prospecter import Lead, Prospecter
from src.utils.helpers import setup_logging


def main() -> None:
    """Run the example prospecter workflow."""
    # Setup logging
    logger = setup_logging("INFO")
    logger.info("Starting SigmaXim Prospecter V3 Example")

    # Initialize the prospecter
    prospecter = Prospecter()

    # Create sample leads
    leads = [
        Lead(
            name="Acme Corporation",
            email="contact@acme.com",
            industry="Technology",
            company_size=500,
            metadata={"website": "https://acme.com", "source": "LinkedIn"},
        ),
        Lead(
            name="Beta Industries",
            email="info@beta.com",
            industry="Manufacturing",
            company_size=150,
            metadata={"website": "https://beta.com", "source": "Referral"},
        ),
        Lead(
            name="Gamma Solutions",
            email="sales@gamma.com",
            industry="Consulting",
            company_size=25,
            metadata={"website": "https://gamma.com", "source": "Website"},
        ),
        Lead(
            name="Delta Enterprises",
            email="hello@delta.com",
            industry="Technology",
            company_size=1000,
            metadata={"website": "https://delta.com", "source": "Conference"},
        ),
        Lead(
            name="Epsilon Co",
            email="contact@epsilon.com",
            industry="Retail",
            company_size=75,
            metadata={"website": "https://epsilon.com", "source": "Cold Call"},
        ),
    ]

    # Run the prospecter workflow
    logger.info(f"Processing {len(leads)} leads...")
    results = prospecter.run(leads=leads, min_score=0.6)

    # Display results
    print("\n" + "=" * 70)
    print("PROSPECTING RESULTS")
    print("=" * 70)
    print(f"\nTotal Leads Processed: {results['total_processed']}")
    print(f"Qualified Leads (score >= 0.6): {results['total_qualified']}")
    print(f"Average Score: {results['average_score']:.2f}")

    print("\n" + "-" * 70)
    print("QUALIFIED LEADS")
    print("-" * 70)

    for lead in results["qualified_leads"]:
        print(f"\n{lead['name']}")
        print(f"  Email: {lead['email']}")
        print(f"  Industry: {lead['industry']}")
        print(f"  Company Size: {lead['company_size']}")
        print(f"  Score: {lead['score']:.2f}")
        if lead.get("metadata"):
            print(f"  Source: {lead['metadata'].get('source', 'N/A')}")

    print("\n" + "=" * 70)
    logger.info("Example completed successfully!")


if __name__ == "__main__":
    main()
