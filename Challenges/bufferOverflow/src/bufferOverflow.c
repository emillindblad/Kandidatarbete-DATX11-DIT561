#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PASSWORD "password123"
#define FLAG_FILE "flag.txt"

int main() {
    setbuf(stdout, NULL); // Add this line to disable output buffering
    char input[64];
    char flag[64];
    int is_authenticated = 0;

    printf("Enter password: ");
    gets(input);

    if (is_authenticated) {
        FILE *file = fopen(FLAG_FILE, "r");
        if (file == NULL) {
            printf("Error: Cannot open flag file.\n");
            return 1;
        }

        fgets(flag, sizeof(flag), file);
        fclose(file);

        printf("Access granted. Here is the flag: %s\n", flag);
    } else {
        printf("Access denied.\n");
    }

    return 0;
}

