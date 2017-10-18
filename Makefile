.PHONY: docs-clean
docs-clean:
	$(MAKE) -C docs clean

.PHONY: docs
docs:
	$(MAKE) -C docs html

.PHONY: dist-clean
dist-clean:
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./spreading_dye_sampler.egg-info

.PHONY: dist
dist:
	python setup.py bdist_wheel --universal
	# Upload with
	# twine upload dist/*
	# after checking version numbers again!
