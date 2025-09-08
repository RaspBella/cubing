all: ../docs/pbs/index.html ../docs/comps/index.html ../docs/recons

../docs/pbs/index.html: ../docs/pbs ../docs/pbs.json pbs.py
	python pbs.py

../docs/comps/index.html: ../docs/comps ../docs/comps.json comps.py
	python comps.py

../docs/pbs:
	mkdir -p $@

../docs/comps:
	mkdir -p $@

../docs/recons:
	make -C recons

clean:
	make -C recons clean
	rm -rf ../docs/pbs ../docs/comps
