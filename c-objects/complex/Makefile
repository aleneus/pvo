test: build
	@./main

build:
	@gcc test.c helpers.c complex.c main.c -o main -lm

format:
	@clang-format --style=GNU -i *.h *.c
