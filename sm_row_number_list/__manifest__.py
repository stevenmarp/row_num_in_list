{
    "name": "Row Number in List View",
    "version": "16.0.1.0.0",
    "summary": "Display automatic row numbers in all tree/list views",
    "category": "Technical",
    "description": """
Row Number in List View
========================

This module adds automatic row numbering to all list/tree views in Odoo.

Features:
---------
* Automatic row number column in all list views
* Clean and lightweight implementation
* Works with all models and views
* No configuration required
* Compatible with Odoo 16.0, 17.0, and 18.0 (Community and Enterprise)

Perfect for:
-----------
* Better data tracking and reference
* Easier communication about specific rows
* Professional list view presentation
* Enhanced user experience
    """,
    "depends": ["web"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "sm_row_number_list/static/src/xml/list_render.xml",
        ],
    },
    "images": ["static/description/banner.png", "static/description/icon.png"],
    "license": "AGPL-3",
    "author": "stevenmarp",
    "website": "https://github.com/stevenmarp",
    "maintainer": "stevenmarp",
    "support": "stevenmarp@github.com",
    "installable": True,
    "application": False,
    "auto_install": False,
}
