"""
example_usage.py -- Demonstrates AbandonedCartRecoveryClient
"""
from client import AbandonedCartRecoveryClient

def main():
    client = AbandonedCartRecoveryClient()
    result = client.generate_campaign(
        customer_name="Alex Mercer",
        cart_total=89.50,
        abandoned_items=["Vitamin C Serum 30ml"]
    )
    print("[Abandoned Cart Recovery Sequence]")
    for e in result['sequence']:
        print(f"\n--- Step {e['step']} ({e['send_delay']}) ---")
        print(f"Subject: {e['subject']}")
        print(e['body'])

if __name__ == "__main__":
    main()
