/* Simple test tools. */

#ifndef TEST_H
#define TEST_H

// Representation of the test case result.
struct testr_t
{
  int exitCode;
  char *err;
};

// Create testr_t instance representing error.
struct testr_t testErr (char *text);

// Create testr_t instance representing success.
struct testr_t testOk ();

// Run test case.
void runTest (struct testr_t func (), char *name);

#endif /* TEST_H */
