#ifndef TEST_H
#define TEST_H

struct testr_t {
	int exitCode;
	char *err;
};

struct testr_t testErr(char *text);
struct testr_t testOk();
void runTest(struct testr_t func(), char *name);

#endif /* TEST_H */
