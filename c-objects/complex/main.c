#include "helpers.h"
#include "complex.h"
#include "test.h"

struct testr_t test_newCmpl() {
	struct cmpl_t* c = newCmpl(10, 11);

	if (c->x != 10) {
		return testErr("wrong x");
	}

	if (c->y != 11) {
		return testErr("wrong y");
	}

	return testOk();
}

struct testr_t test_am00() {
	struct cmpl_t* c = newCmpl(0, 0);

	if (!equal(cmpl_am(c), 0)) {
		return testErr("");
	}

	return testOk();
}

struct testr_t test_am11() {
	struct cmpl_t* c = newCmpl(1, 1);

	if (!equal(cmpl_am(c), 1.414214)) {
		return testErr("");
	}

	return testOk();
}

struct testr_t test_add() {
	struct cmpl_t* c1 = newCmpl(1, 1);
	struct cmpl_t* c2 = newCmpl(0, 2);

	cmpl_add(c1, c2);

	if (!equal(c1->x, 1)) {
		return testErr("wrong x");
	}

	if (!equal(c1->y, 3)) {
		return testErr("wrong y");
	}

	if (!equal(cmpl_am(c1), 3.162278)) {
		return testErr("wrong amplitude");
	}

	return testOk();
}

int main() {
	runTest(test_newCmpl, "newCmpl");
	runTest(test_am00, "am00");
	runTest(test_am11, "am11");
	runTest(test_add, "add");

	return 0;
}
