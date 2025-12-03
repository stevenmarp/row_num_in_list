=======================
Row Number in List View
=======================

.. |badge1| image:: https://img.shields.io/badge/maturity-Production-green.png
    :target: https://odoo-community.org/page/development-status
    :alt: Production
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/Odoo-16.0%20|%2017.0%20|%2018.0-blue.png
    :alt: Odoo 16.0 | 17.0 | 18.0

|badge1| |badge2| |badge3|

This module adds automatic row numbering to all list/tree views in Odoo, making it easier to reference and track specific records.

**Key Features:**

* **Automatic Row Numbers**: Displays sequential row numbers in all list views
* **Zero Configuration**: Works immediately after installation
* **Universal Compatibility**: Applies to all models and custom views
* **Clean Integration**: Seamlessly integrates with Odoo's native list view
* **Lightweight**: Minimal performance impact with simple XML template inheritance
* **Multi-Version Support**: Compatible with Odoo 16.0, 17.0, and 18.0

**Use Cases:**

* Easier communication when discussing specific records ("check row 5")
* Better data tracking during reviews and audits
* Professional presentation for client-facing views
* Enhanced user experience with clear row references

**Table of contents**

.. contents::
   :local:

Installation
============

To install this module, simply:

1. Download or clone this module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install "Row Number in List View" from the Apps menu

No additional configuration or dependencies required beyond the base ``web`` module.

Configuration
=============

This module requires no configuration. Row numbers will automatically appear in all list views after installation.

Usage
=====

Once installed, row numbers will automatically appear as the first column in all list/tree views throughout Odoo.

**Features:**

* Row numbers appear before the checkbox column (if present)
* Numbering starts from 1 for each page
* Works with pagination - numbers adjust per page
* Compatible with all standard and custom list views

**Example:**

When viewing any list (customers, products, invoices, etc.), you'll see a "#" column showing:

::

    #  | Customer Name     | Email
    ---|-------------------|------------------
    1  | John Doe          | john@example.com
    2  | Jane Smith        | jane@example.com
    3  | Bob Johnson       | bob@example.com

Bug Tracker
===========

Bugs are tracked on GitHub Issues. In case of trouble, please check there if your issue has already been reported.

Credits
=======

Authors
~~~~~~~

* stevenmarp

Contributors
~~~~~~~~~~~~

* stevenmarp

Maintainers
~~~~~~~~~~~

This module is maintained by stevenmarp.

This module is part of a commitment to the Odoo community and open-source software.
