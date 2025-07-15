.PHONY: init clean

init:
	@echo "Initializing vendor-specific guidelines..."
	@python3 vendor_guideline.py

clean:
	@echo "Cleaning generated guidelines..."
	@rm -rf .cursor
	@rm -rf .claude
	@rm -f claude.md 