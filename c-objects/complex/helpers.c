#include "helpers.h"
#include <stdlib.h>

int
equal (double a, double b)
{
  if (abs (a - b) < 0.00001)
    {
      return 1;
    }

  return 0;
}
