"""Core business logic for SigmaXim Prospecter.

This module contains the main Prospecter class that orchestrates the prospecting
workflow including lead scoring, analysis, and processing.

The Prospecter is designed to be:
- Platform-agnostic (works with multiple AI providers)
- Extensible (easy to add new features)
- Type-safe (uses type hints throughout)
- Well-documented (comprehensive docstrings)
- Testable (modular design for easy testing)

Example:
    >>> from src.core.prospecter import Prospecter
    >>> prospecter = Prospecter()
    >>> results = prospecter.run()
"""

import logging
from typing import Any, Dict, List, Optional

from src.config.settings import get_settings
from src.utils.helpers import setup_logging


class Lead:
    """Represents a prospect/lead in the system.

    Attributes:
        id: Unique identifier for the lead
        name: Company or contact name
        email: Contact email address
        industry: Industry classification
        company_size: Number of employees
        score: AI-calculated lead score (0.0 to 1.0)
        metadata: Additional custom data
    """

    def __init__(
        self,
        name: str,
        email: str,
        id: Optional[str] = None,
        industry: Optional[str] = None,
        company_size: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize a Lead instance.

        Args:
            name: Company or contact name
            email: Contact email address
            id: Unique identifier (auto-generated if not provided)
            industry: Industry classification
            company_size: Number of employees
            metadata: Additional custom data
        """
        self.id = id or self._generate_id()
        self.name = name
        self.email = email
        self.industry = industry
        self.company_size = company_size
        self.score: Optional[float] = None
        self.metadata = metadata or {}

    @staticmethod
    def _generate_id() -> str:
        """Generate a unique ID for the lead.

        Returns:
            str: Unique identifier
        """
        import uuid

        return str(uuid.uuid4())

    def to_dict(self) -> Dict[str, Any]:
        """Convert lead to dictionary representation.

        Returns:
            Dict[str, Any]: Dictionary representation of the lead
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "industry": self.industry,
            "company_size": self.company_size,
            "score": self.score,
            "metadata": self.metadata,
        }


class Prospecter:
    """Main prospecting orchestrator.

    This class coordinates the prospecting workflow including lead scoring,
    analysis, and processing. It's designed to work with multiple AI platforms
    and provides a clean, extensible API.

    Attributes:
        settings: Application settings
        logger: Configured logger instance
    """

    def __init__(self, settings: Optional[Any] = None) -> None:
        """Initialize the Prospecter.

        Args:
            settings: Optional settings override (uses default if not provided)
        """
        self.settings = settings or get_settings()
        self.logger = setup_logging(self.settings.log_level)
        self.logger.info("Prospecter initialized")

    def score_lead(self, lead: Lead) -> float:
        """Score a lead using AI-powered analysis.

        This is a placeholder implementation. In production, this would use
        AI models to analyze the lead and return a quality score.

        Args:
            lead: Lead instance to score

        Returns:
            float: Score between 0.0 and 1.0 indicating lead quality

        Example:
            >>> prospecter = Prospecter()
            >>> lead = Lead(name="Test Co", email="test@example.com")
            >>> score = prospecter.score_lead(lead)
            >>> print(f"Lead score: {score:.2f}")
        """
        # Placeholder scoring logic
        # In production, this would integrate with AI services
        score = 0.5

        # Basic scoring factors
        if lead.industry:
            score += 0.1
        if lead.company_size and lead.company_size > 50:
            score += 0.2
        if lead.email and "@" in lead.email:
            score += 0.1

        # Normalize score to 0-1 range
        score = min(1.0, max(0.0, score))

        lead.score = score
        self.logger.debug(f"Scored lead {lead.name}: {score:.2f}")

        return score

    def process_leads(self, leads: List[Lead]) -> List[Lead]:
        """Process a list of leads.

        Scores each lead and returns them sorted by score (highest first).

        Args:
            leads: List of Lead instances to process

        Returns:
            List[Lead]: Processed and sorted leads

        Example:
            >>> prospecter = Prospecter()
            >>> leads = [Lead(name=f"Company {i}", email=f"test{i}@example.com") for i in range(3)]
            >>> processed = prospecter.process_leads(leads)
        """
        self.logger.info(f"Processing {len(leads)} leads")

        # Score all leads
        for lead in leads:
            self.score_lead(lead)

        # Sort by score (highest first)
        sorted_leads = sorted(leads, key=lambda x: x.score or 0, reverse=True)

        self.logger.info(f"Processed {len(sorted_leads)} leads successfully")
        return sorted_leads

    def run(
        self,
        leads: Optional[List[Lead]] = None,
        min_score: float = 0.0,
    ) -> Dict[str, Any]:
        """Run the main prospecting workflow.

        This is the main entry point for the prospecting process.

        Args:
            leads: List of leads to process (generates sample if not provided)
            min_score: Minimum score threshold for filtering

        Returns:
            Dict[str, Any]: Results including processed leads and statistics

        Example:
            >>> prospecter = Prospecter()
            >>> results = prospecter.run(min_score=0.6)
            >>> print(f"Found {results['total_qualified']} qualified leads")
        """
        self.logger.info("Starting prospecting workflow")

        # Use provided leads or generate sample data
        if leads is None:
            leads = self._generate_sample_leads()

        # Process all leads
        processed_leads = self.process_leads(leads)

        # Filter by minimum score
        qualified_leads = [lead for lead in processed_leads if (lead.score or 0) >= min_score]

        results = {
            "total_processed": len(processed_leads),
            "total_qualified": len(qualified_leads),
            "min_score": min_score,
            "qualified_leads": [lead.to_dict() for lead in qualified_leads],
            "average_score": (
                sum(lead.score or 0 for lead in processed_leads) / len(processed_leads)
                if processed_leads
                else 0
            ),
        }

        self.logger.info(
            f"Workflow completed: {results['total_qualified']} qualified leads "
            f"from {results['total_processed']} total"
        )

        return results

    def _generate_sample_leads(self) -> List[Lead]:
        """Generate sample leads for testing.

        Returns:
            List[Lead]: Sample leads
        """
        return [
            Lead(
                name="Acme Corporation",
                email="contact@acme.com",
                industry="Technology",
                company_size=500,
            ),
            Lead(
                name="Beta Industries",
                email="info@beta.com",
                industry="Manufacturing",
                company_size=150,
            ),
            Lead(
                name="Gamma Solutions",
                email="sales@gamma.com",
                industry="Consulting",
                company_size=25,
            ),
        ]
