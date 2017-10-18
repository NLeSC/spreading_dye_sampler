.PHONY: docs-clean
docs-clean:
	$(MAKE) -C docs clean

.PHONY: docs
docs:
	$(MAKE) -C docs html
