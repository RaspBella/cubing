output_dir=../docs
files=pbs comps
dirs=$(addprefix $(output_dir)/,$(files))

.PHONY: all clean

all: $(addsuffix /index.html,$(dirs))

$(output_dir)/%/index.html: %.py
	mkdir -p $(dir $@)
	python $<

clean:
	rm -rf $(dirs)
