#!/usr/bin/env bash
# READ ONLY - where is Odoo actually installed and how is it launched?
echo "== running process =="; ps -eo user:20,args= | grep '[o]doo' | head -5
echo; echo "== systemd unit =="; systemctl cat odoo19 2>/dev/null | grep -E 'ExecStart|User=' || echo "  no unit named odoo19"
echo; echo "== candidate launchers =="; ls -la /opt/odoo19/venv/bin/odoo* 2>/dev/null; ls -la /opt/odoo19/odoo-bin 2>/dev/null
find /opt /usr/local/bin /usr/bin -maxdepth 5 \( -name 'odoo-bin' -o -name 'odoo' \) -type f 2>/dev/null | head -10
echo; echo "READ ONLY - nothing modified."
