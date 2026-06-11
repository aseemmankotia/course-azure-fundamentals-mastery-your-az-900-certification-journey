#!/bin/bash
# Verification script for Lab 1: Cloud Computing Foundations: The 'Why' Behind the Cloud
set -e
echo "🔍 Verifying Lab 1: Cloud Computing Foundations: The 'Why' Behind the Cloud..."
[ -f "cloud-service-models-comparison.py" ] && echo "✅ cloud-service-models-comparison.py found" || echo "❌ cloud-service-models-comparison.py missing"
[ -f "capex-vs-opex-calculator.py" ] && echo "✅ capex-vs-opex-calculator.py found" || echo "❌ capex-vs-opex-calculator.py missing"
echo ""
echo "✅ Lab 1 verification complete!"
