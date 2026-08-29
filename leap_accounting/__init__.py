# Leap Accounting — meta module; uninstall removes the bundled apps.


BUNDLE_MODULES = (
    'leap_accounting_kit',
    'leap_l10n_sa_edi',
    'leap_account_budget',
)


def uninstall_hook(env):
    """Uninstall the bundled modules when Leap Accounting is removed."""
    modules = env['ir.module.module'].search([
        ('name', 'in', list(BUNDLE_MODULES)),
        ('state', '=', 'installed'),
    ])
    if modules:
        # Mark only — immediate uninstall is not allowed during registry reload
        modules.button_uninstall()
