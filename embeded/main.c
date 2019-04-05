#include <stdio.h>
#include "uniform_energy.h"


int main() {
    double prices[] = {123.0, 123.0, 413.0, 1231.0, 120.0, 897.0};
    struct ue_time times[] = {(struct ue_time){2019,11,10,10},(struct ue_time){2019,11,10,11},(struct ue_time){2019,11,10,12},(struct ue_time){2019,11,10,13},(struct ue_time){2019,11,10,14},(struct ue_time){2019,11,10,15}};
    struct ue_prob_pdf pdf;

    ue_random_reset_set();
    ue_create_prob_pdf_price(&pdf, prices, times, 6);
    for(int i = 0; i < 100; i++) {
        struct ue_time wh = ue_next(&pdf);
        printf("%i/%i/%i:%i\n", wh.year, wh.month, wh.day, wh.hour);
    }
}