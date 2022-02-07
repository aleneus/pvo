#include <stdio.h>
#include "test.h"

struct testr_t testErr(char *text) {
	struct testr_t res = {1, text};

	return res;
}

struct testr_t testOk() {
	struct testr_t res = {0, ""};

	return res;
}

void runTest(struct testr_t func(), char *name) {
	struct testr_t res = func();

	printf("run %s: ", name);

	if (res.exitCode == 0) {
		printf("OK\n");

		return;
	}

	printf("FAIL: %s\n", res.err);
}
