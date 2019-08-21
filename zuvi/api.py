from __future__ import unicode_literals

import frappe


@frappe.whitelist()
def calculate_contribution(self,mehtod):
    if not self.meta.get_field("sales_team"):
        return
    total = 0.0
    sales_team = self.get("sales_team")
    # my_allocated_percentage=100/(len(sales_team))
    for sales_person in sales_team:
        self.round_floats_in(sales_person)
        # sales_person.allocated_percentage=my_allocated_percentage
        sales_person.allocated_amount=1
        sales_person.incentives=1
        sales_person.commission_rate=1
    return