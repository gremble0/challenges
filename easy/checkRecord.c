#include <stdbool.h>

bool checkRecord(char* s) {
    int late_counter = 0;
    int days_absent = 0;

    for (char c = *s; c != '\0'; c = *++s) {
        if (c == 'L') { 
            if (late_counter == 2) return false;
            ++late_counter;
        } else {
            if (c == 'A') ++days_absent;
            late_counter = 0;
        }
    }
    if (days_absent >= 2) return false;
    return true;
}
