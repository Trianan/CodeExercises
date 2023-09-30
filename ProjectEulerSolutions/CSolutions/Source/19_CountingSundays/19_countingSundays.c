// PROJECT EULER - PROBLEM 19 - COUNTING SUNDAYS

#include <stdio.h>

const int MAX_YEAR = 2000;
const int MAX_MONTH = 11; // December has index of 0 in months array.

int is_leapyear(int current_year) {
    // Returns 1 if current_year is a leap year, 0 otherwise:
    if (
        current_year % 400 == 0 ||
        (
            current_year % 4 == 0 &&
            !(current_year % 100 == 0)
        )
    ) {
        return 1;
    }
    return 0;
}

int main() {
    int months[12] = {31,28,31,30,31,30,31,31,30,31,30,31}; // Not constant as main() modifies months[1].
    int current_month = 0; // Index in months array.
    int current_year = 1901;
    int current_day = 1; // Calendar day, therefore doesn't start at 0.
    int total_days = 0;
    int total_sunday_1sts = 0; // Final answer.

    // This loop iterates for each day between the range of years provided:
    while(current_year <= MAX_YEAR) {

        // Handle February on leap year:
        if (is_leapyear(current_year)) { // This can be optimized to run only on Jan 1st of each year.
            months[1] = 29;
        } else {
            months[1] = 28;
        }

        /* printf(
            "current_year: %d\tcurrent_month: %d\tcurrent_day: %d\ttotal_days: %d\ttotal_sunday_1sts: %d\n\n",
            current_year, current_month, current_day, total_days, total_sunday_1sts
        ); UNCOMMENT FOR LOGGING */

        if (current_day == 1 && total_days % 7 == 0) {
            //UNCOMMENT FOR LOGGING printf("Sunday 1st found!\n\n");
            total_sunday_1sts++;
        }

        // Increment calendar day:
        current_day++;
        // Increment month:
        if (current_day > months[current_month]) {
            current_day = 1;
            current_month++;
            // Increment year:
            if (current_month > MAX_MONTH) {
                current_month = 0;
                current_year++;
            }
        }
        total_days++;
    }
    printf("Total days: %d\nTotal Sunday 1sts: %d\n", total_days, total_sunday_1sts);
    // Verified answer: 171    
}