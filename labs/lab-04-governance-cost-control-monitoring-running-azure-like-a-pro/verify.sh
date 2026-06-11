#!/bin/bash
# Verification script for Lab 4: Governance, Cost Control & Monitoring: Running Azure Like a Pro
set -e
echo "🔍 Verifying Lab 4: Governance, Cost Control & Monitoring: Running Azure Like a Pro..."
[ -f "azure-resource-tags-management.py" ] && echo "✅ azure-resource-tags-management.py found" || echo "❌ azure-resource-tags-management.py missing"
echo ""
echo "✅ Lab 4 verification complete!"
