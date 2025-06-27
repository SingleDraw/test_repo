run once:
git update-index --chmod=+x dynamic_inventory.py
git commit -m "Set executable bit on dynamic_inventory.py"
git push origin main
git ls-tree HEAD ./dynamic_inventory.py