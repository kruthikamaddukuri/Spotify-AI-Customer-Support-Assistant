def decide_action(intent, confidence):
    """
    Decide whether a customer issue should be
    auto-handled or escalated to a human agent.
    """

    # High-risk issues that require human attention
    high_risk_intents = {
        "Account_Security",
        "Payment_Refund"
    }

    # Confidence threshold
    confidence_threshold = 0.60

    # Rule 1: Low confidence → Escalate
    if confidence < confidence_threshold:
        return {
            "action": "ESCALATE_TO_HUMAN",
            "reason": (
                "The AI model is not confident enough about the customer's issue, "
                "so human review is safer."
            )
        }

    # Rule 2: High-risk issues → Escalate
    if intent in high_risk_intents:
        return {
            "action": "ESCALATE_TO_HUMAN",
            "reason": (
                f"This issue belongs to {intent}, which may require "
                "account-specific verification or sensitive information."
            )
        }

    # Rule 3: Safe/common issues → Auto-handle
    return {
        "action": "AUTO_HANDLE",
        "reason": (
            "This appears to be a common support issue with a standard "
            "troubleshooting or informational response."
        )
    }