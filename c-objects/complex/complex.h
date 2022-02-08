/* Complex numbers library. */

#ifndef COMPLEX_H
#define COMPLEX_H

// Representation of complex number.
struct cmpl_t
{
  double x;
  double y;
};

// Create new complex number.
struct cmpl_t *newCmpl (double x, double y);

// Return amplitude of complex number.
double cmpl_am (struct cmpl_t *c);

// Sum complex numbers.
void cmpl_add (struct cmpl_t *c, struct cmpl_t *other);

#endif /* COMPLEX_H */
