#include "complex.h"
#include <math.h>
#include <stdlib.h>

struct cmpl_t *
newCmpl (double x, double y)
{
  struct cmpl_t *c = malloc (sizeof (struct cmpl_t));

  c->x = x;
  c->y = y;

  return c;
}

double
cmpl_am (struct cmpl_t *c)
{
  return sqrt (c->x * c->x + c->y * c->y);
}

void
cmpl_add (struct cmpl_t *c, struct cmpl_t *other)
{
  c->x += other->x;
  c->y += other->y;
}
