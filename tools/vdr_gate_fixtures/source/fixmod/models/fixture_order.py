# Synthetic fixture source for the STATE03 candidate portable gate.
# Not Odoo code. Used only to prove pointer and anchor verification.


class FixtureOrder:
    STATES = ("draft", "confirmed", "cancelled")

    def __init__(self):
        self.state = "draft"

    def action_confirm(self):
        if self.state != "draft":
            raise ValueError("Only draft orders can be confirmed")
        self.state = "confirmed"

    def action_cancel(self):
        if self.state == "cancelled":
            raise ValueError("Order already cancelled")
        self.state = "cancelled"
