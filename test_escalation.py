from escalation_policy import decide_action


test_cases = [
    ("Account_Security", 0.95),
    ("Payment_Refund", 0.90),
    ("Playback_Issue", 0.85),
    ("Downloads_Offline", 0.80),
    ("Music_Content", 0.35)
]


print("\nESCALATION POLICY TEST\n")
print("=" * 60)

for intent, confidence in test_cases:

    result = decide_action(intent, confidence)

    print(f"\nIntent: {intent}")
    print(f"Confidence: {confidence:.2%}")
    print(f"Decision: {result['action']}")
    print(f"Reason: {result['reason']}")