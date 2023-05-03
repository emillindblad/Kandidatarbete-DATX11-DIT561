#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PASSWORD_FILE "password.txt"
#define FLAG_FILE "flag.txt"

int read_password_from_file(char *password, const char *filename, size_t buffer_size) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        return 1;
    }

    fgets(password, buffer_size, file);
    fclose(file);

    // Remove the newline character if it's present
    size_t len = strlen(password);
    if (len > 0 && password[len - 1] == '\n') {
        password[len - 1] = '\0';
    }

    return 0;
}

int main() {
    setbuf(stdout, NULL); // Add this line to disable output buffering
    char input[64];
    char flag[64];
    char password[64];
    int is_authenticated = 0;

    if (read_password_from_file(password, PASSWORD_FILE, sizeof(password))) {
        printf("Error: Cannot open password file.\n");
        return 1;
    }

    printf("Enter password: ");
    gets(input);

    if (strcmp(input, password) == 0) {
        is_authenticated = 1;
    }
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
