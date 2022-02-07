#ifndef COMPLEX_H
#define COMPLEX_H

struct cmpl_t {
	double x;
	double y;
};

struct cmpl_t *newCmpl(double x, double y);
double cmpl_am(struct cmpl_t *c);
void cmpl_add(struct cmpl_t *c, struct cmpl_t *other);

#endif /* COMPLEX_H */
