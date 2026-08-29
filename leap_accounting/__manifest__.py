# -*- coding: utf-8 -*-
{
    'name': 'Leap Accounting',
    'version': '19.0.1.2.0',
    'category': 'Accounting',
    'summary': 'Full Community accounting, budgets, and Saudi ZATCA Phase 2 in one app.',
    'description': """
Leap Accounting
===============
One-click bundle for Odoo 19 Community:

* Leap Accounting Kit (financial reports, assets, PDC, reconciliation)
* Leap Budget Management
* Leap Saudi Arabia E-invoicing (ZATCA Phase 2)

Technical modules included in the same store ZIP:

* leap_accounting_kit
* leap_account_budget
* leap_l10n_sa_edi
    """,
    'depends': [
        'leap_l10n_sa_edi',
        'leap_accounting_kit',
        'leap_account_budget',
    ],
    'author': 'Leap',
    'website': 'https://apps.odoo.com/apps/modules/19.0/leap_accounting',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
}
