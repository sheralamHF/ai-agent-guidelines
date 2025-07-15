.PHONY: init clean install-deps

init: install-deps
	@echo "Initializing vendor-specific guidelines..."
	@python3 vendor_guideline.py

install-deps:
	@echo "Installing dependencies..."
	@pip3 install pyyaml --quiet

clean:
	@echo "Cleaning generated guidelines..."
	@rm -rf .cursor
	@rm -rf .claude
	@rm -f claude.md 