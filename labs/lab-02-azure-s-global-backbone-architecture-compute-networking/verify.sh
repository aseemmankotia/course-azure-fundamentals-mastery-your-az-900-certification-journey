#!/bin/bash
# Verification script for Lab 2: Azure's Global Backbone: Architecture, Compute & Networking
set -e
echo "🔍 Verifying Lab 2: Azure's Global Backbone: Architecture, Compute & Networking..."
[ -f "explore-azure-regions.py" ] && echo "✅ explore-azure-regions.py found" || echo "❌ explore-azure-regions.py missing"
[ -f "create-resource-group.py" ] && echo "✅ create-resource-group.py found" || echo "❌ create-resource-group.py missing"
echo ""
echo "✅ Lab 2 verification complete!"
