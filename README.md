# genpark-abandoned-cart-recovery-skill

> **GenPark AI Agent Skill** -- Abandoned cart 3-step sequence builder.

## Quick Start

```python
from client import AbandonedCartRecoveryClient
client = AbandonedCartRecoveryClient()
res = client.generate_campaign("Emma", 45.00, ["Sunscreen SPF 50"])
print(res["sequence"][0]["subject"])
```
