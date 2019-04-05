#ifndef __UNIFORM__ENERGY__H__
#define __UNIFORM__ENERGY__H__
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct ue_time {
    int year;
    int month;
    int day;
    int hour;
};


struct ue_prob_pdf {
    double* point_values;
    struct ue_time* times;
    int n;
};

void ue_random_reset_set() {
    srand(time(NULL));
}

double ue_uniform_random() {
    return (double)rand() / (double)RAND_MAX; 
}

int __ue__invert_pdf(struct ue_prob_pdf* pdf, double* point_values, struct ue_time* times, int n) {
    for(int i = 0; i < n; i++) {
        point_values[i] = 1.0 - point_values[i];
    }

    pdf->point_values = point_values;
    pdf->times = times;
    pdf->n = n;
    return 1;
}

int ue_create_prob_pdf_price(struct ue_prob_pdf* pdf, double* prices, struct ue_time* times, int n) {
    double sum = 0;
    for(int i = 0; i < n; i++) {
        sum += prices[i];
    }

    for(int i = 0; i < n; i++) {
        prices[i] = prices[i] / sum;
    }

    return __ue__invert_pdf(pdf, prices, times, n);
}

struct ue_time ue_prob(struct ue_prob_pdf* pdf, double probability) {
    double p = 0;
    for(int i = 0; i < pdf->n; i++) {
        p += pdf->point_values[i];
        if(p >= probability) {
            return pdf->times[i];
        }
    }
    return pdf->times[pdf->n - 1];
}

struct ue_time ue_next(struct ue_prob_pdf* pdf) {
    return ue_prob(pdf, ue_uniform_random());
}

#endif
