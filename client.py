"""
abandoned-cart-recovery-skill: Client SDK
Builds customized, high-converting checkout recovery sequences based on cart properties.
"""
from __future__ import annotations
from typing import Optional


class AbandonedCartRecoveryClient:
    """
    SDK for creating abandoned cart recovery emails.
    """

    def generate_campaign(
        self,
        customer_name: str,
        cart_total: float,
        abandoned_items: list[str],
    ) -> dict:
        name = customer_name.split()[0] if customer_name else "there"
        item_str = abandoned_items[0] if abandoned_items else "items in your cart"
        
        # High value carts get incentives
        discount_code = "SAVE10" if cart_total >= 75.0 else None

        emails = []
        
        # Email 1: Gentle Reminder (1 Hour)
        emails.append({
            "step": 1,
            "send_delay": "1 hour",
            "subject": f"Hey {name}, you left something behind...",
            "body": f"Hi {name},\n\nWe noticed you left your {item_str} in your cart. We saved it for you, but inventory is running low. Click here to secure your order now."
        })

        # Email 2: Social Proof / Scarcity (24 Hours)
        emails.append({
            "step": 2,
            "send_delay": "24 hours",
            "subject": f"Still thinking about the {item_str}?",
            "body": f"Hi {name},\n\nOur community loves this item! Don't miss out on adding it to your routine. Restocks can take up to 4 weeks. Complete your order today."
        })

        # Email 3: Discount Incentive (48 Hours)
        discount_msg = f"Here is an exclusive code {discount_code} for 10% off to sweeten the deal!" if discount_code else "Shipping is on us if you complete your order in the next 12 hours!"
        emails.append({
            "step": 3,
            "send_delay": "48 hours",
            "subject": f"Your cart is expiring -- discount inside",
            "body": f"Hi {name},\n\nWe want to make this easy for you. {discount_msg}\n\nClick here to checkout instantly."
        })

        return {
            "cart_total": cart_total,
            "incentive_applied": "10% off" if discount_code else "Free shipping",
            "sequence": emails,
        }
