"""Unit tests for the Prospecter core module.

These tests verify the functionality of the main Prospecter class and
related components. All external dependencies are mocked.
"""

import pytest

from src.core.prospecter import Lead, Prospecter


class TestLead:
    """Test cases for the Lead class."""

    def test_lead_initialization(self) -> None:
        """Test that Lead initializes with correct attributes."""
        lead = Lead(
            name="Test Company",
            email="test@example.com",
            industry="Technology",
            company_size=100,
        )

        assert lead.name == "Test Company"
        assert lead.email == "test@example.com"
        assert lead.industry == "Technology"
        assert lead.company_size == 100
        assert lead.score is None
        assert lead.id is not None

    def test_lead_to_dict(self) -> None:
        """Test Lead conversion to dictionary."""
        lead = Lead(name="Test Co", email="test@test.com")
        lead.score = 0.75

        lead_dict = lead.to_dict()

        assert lead_dict["name"] == "Test Co"
        assert lead_dict["email"] == "test@test.com"
        assert lead_dict["score"] == 0.75
        assert "id" in lead_dict

    def test_lead_generates_unique_ids(self) -> None:
        """Test that each Lead gets a unique ID."""
        lead1 = Lead(name="Company 1", email="test1@test.com")
        lead2 = Lead(name="Company 2", email="test2@test.com")

        assert lead1.id != lead2.id


class TestProspecter:
    """Test cases for the Prospecter class."""

    def test_prospecter_initialization(self) -> None:
        """Test that Prospecter initializes correctly."""
        prospecter = Prospecter()

        assert prospecter.settings is not None
        assert prospecter.logger is not None

    def test_score_lead_returns_valid_score(self) -> None:
        """Test that score_lead returns a value between 0 and 1."""
        prospecter = Prospecter()
        lead = Lead(
            name="Test Company",
            email="test@example.com",
            industry="Technology",
            company_size=100,
        )

        score = prospecter.score_lead(lead)

        assert 0 <= score <= 1
        assert lead.score == score

    def test_score_lead_without_optional_fields(self) -> None:
        """Test scoring a lead with minimal information."""
        prospecter = Prospecter()
        lead = Lead(name="Minimal Co", email="min@test.com")

        score = prospecter.score_lead(lead)

        assert 0 <= score <= 1

    def test_process_leads_sorts_by_score(self) -> None:
        """Test that process_leads returns leads sorted by score."""
        prospecter = Prospecter()
        leads = [
            Lead(name="Company A", email="a@test.com"),
            Lead(name="Company B", email="b@test.com", industry="Tech", company_size=200),
            Lead(name="Company C", email="c@test.com", industry="Finance"),
        ]

        processed = prospecter.process_leads(leads)

        # Verify all leads are scored
        for lead in processed:
            assert lead.score is not None

        # Verify sorted in descending order
        scores = [lead.score for lead in processed]
        assert scores == sorted(scores, reverse=True)

    def test_run_workflow_with_sample_data(self) -> None:
        """Test the complete workflow with sample data."""
        prospecter = Prospecter()

        results = prospecter.run(min_score=0.0)

        assert "total_processed" in results
        assert "total_qualified" in results
        assert "qualified_leads" in results
        assert "average_score" in results
        assert results["total_processed"] > 0
        assert results["total_qualified"] >= 0

    def test_run_workflow_with_custom_leads(self) -> None:
        """Test workflow with custom lead list."""
        prospecter = Prospecter()
        custom_leads = [
            Lead(name=f"Company {i}", email=f"test{i}@example.com") for i in range(5)
        ]

        results = prospecter.run(leads=custom_leads, min_score=0.5)

        assert results["total_processed"] == 5
        assert results["total_qualified"] <= 5

    def test_run_workflow_filters_by_min_score(self) -> None:
        """Test that min_score filtering works correctly."""
        prospecter = Prospecter()

        # Run with low threshold
        results_low = prospecter.run(min_score=0.0)

        # Run with high threshold
        results_high = prospecter.run(min_score=0.9)

        # High threshold should have fewer qualified leads
        assert results_high["total_qualified"] <= results_low["total_qualified"]
