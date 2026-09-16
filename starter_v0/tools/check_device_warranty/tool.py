from __future__ import annotations

import json
from datetime import datetime
from typing import Any

from tools._shared import ROOT, err

ASSET_FILE = ROOT / "helpdesk_data" / "assets.json"


def check_device_warranty(asset_id: str = "") -> dict[str, Any]:
    """Check manufacturer warranty expiration date and support coverage for a company asset."""
    try:
        data = json.loads(ASSET_FILE.read_text(encoding="utf-8"))
        wanted_id = (asset_id or "").strip().upper()
        if not wanted_id:
            return {"tool": "check_device_warranty", "error": "missing_asset_id", "message": "asset_id is required"}

        device = next((item for item in data["assets"] if item["asset_id"] == wanted_id), None)
        if device is None:
            return {"tool": "check_device_warranty", "asset_id": wanted_id, "error": "asset_not_found"}

        purchase_date = device.get("purchase_date", "unknown")
        warranty_until = device.get("warranty_until", "unknown")

        is_active = True
        if warranty_until and warranty_until != "unknown":
            try:
                exp = datetime.fromisoformat(warranty_until)
                is_active = datetime.now() <= exp
            except Exception:
                is_active = True

        return {
            "tool": "check_device_warranty",
            "asset_id": wanted_id,
            "manufacturer": device.get("manufacturer"),
            "model": device.get("model"),
            "purchase_date": purchase_date,
            "warranty_until": warranty_until,
            "status": "active" if is_active else "expired",
            "support_tier": "Enterprise Onsite Support (NBD)",
        }
    except Exception as exc:
        return err("check_device_warranty", exc)
