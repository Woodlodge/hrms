# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShiftTypeRounding(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		end: DF.Check
		from_time: DF.Time
		mid_in: DF.Check
		mid_out: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		point: DF.Int
		start: DF.Check
		to_time: DF.Time
		unit: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Shift Type Rounding"
