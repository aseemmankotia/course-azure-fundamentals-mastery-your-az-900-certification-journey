#!/bin/bash
# Verification script for Lab 3: Data, Storage & Identity: Protecting What Matters Most
set -e
echo "🔍 Verifying Lab 3: Data, Storage & Identity: Protecting What Matters Most..."
[ -f "blob-storage-tiers-demo.py" ] && echo "✅ blob-storage-tiers-demo.py found" || echo "❌ blob-storage-tiers-demo.py missing"
echo ""
echo "✅ Lab 3 verification complete!"
