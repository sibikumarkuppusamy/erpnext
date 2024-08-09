from frappe import _


def get_data():
	return {
		"fieldname": "finance_book",
		"non_standard_fieldnames": {"Company": "default_finance_book"},
		"transactions": [
			{"items": ["Company"]},
			{"items": ["Journal Entry"]},
		],
	}
