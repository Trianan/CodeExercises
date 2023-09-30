// PROJECT EULER - PROBLEM 59 - XOR Decryption
#include <stdio.h>
#include <stdbool.h>


bool is_digit(char c) {
    if (
        (int)(c) >= (int)('0') && 
        (int)(c) <= (int)('9')
    ) {
        return true;
    }
    return false;
}

int digit_ctoi(char c) {
    // Returns integer representation of single digit char.
    return (int)(c) - (int)('0');
}

char* get_permutations(char * char_set) {
    // TO-DO
    printf("\nCHARSET: %s (%lu)\n", char_set, sizeof(*char_set));
    return char_set;
}


int main() {
    FILE* cipher_fp = fopen("0059_cipher.txt", "r");
    FILE* clear_fp  = fopen("0059_clear.txt", "w");
    if (cipher_fp && clear_fp) {
        printf("Files opened successfully.\n");
    } else {
        printf("Failed to open files!\n");
    }

    char c;
    int cipher_char;
    int clear_char;

    char key[] = "abc";
    int key_length = (int)sizeof(key) - 2; // Accounts for \0 character in string being counted + 0-index.
    int key_counter = 0;

    while ((c = fgetc(cipher_fp)) != EOF) {

        if (is_digit(c)) {
            // Reads in multidigit integers:
            cipher_char = digit_ctoi(c);
            while(is_digit((c = fgetc(cipher_fp)))) {
                cipher_char = (cipher_char * 10) + digit_ctoi(c);
            }
            // At this point; cipher_char is in correct integer representation and is XOR'd w. key:
            clear_char = cipher_char ^ (int)key[key_counter];
            fputc(clear_char, clear_fp);
            printf(
                "\n\tCIPHER CHAR: %d (%c)\n\tCLEAR CHAR: %d (%c)\n\tKEY CHAR: %d (%c)\n",
                cipher_char, cipher_char,
                clear_char, clear_char,
                key[key_counter], key[key_counter]
            );
            if (key_counter < key_length) {
                key_counter++;
            } else {
                key_counter = 0;
            }
        }
    }
    
    get_permutations("aaa");
    fclose(cipher_fp);
    return 0;
}