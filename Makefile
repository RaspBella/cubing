output_dir=../docs
files=pbs comps
dirs=$(addprefix $(output_dir)/,$(files))

.PHONY: all clean

CFLAGS=-MMD

all: gen
	mkdir -p $(dirs)
	./gen

gen: gen.c
	cc $(CFLAGS) $< -o $@

-include gen.d

clean:
	rm -rf gen gen.d $(dirs) $(dirs).json
